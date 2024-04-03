from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.dao import BaseDAO
from src.exceptions import (
    ForbiddenException,
    ProductCategoryNotFoundException,
    VariationAlreadyExistsException,
    raise_http_exception,
)
from src.permissions import has_permission
from src.products.categories.dao import ProductCategoryDAO
from src.utils.session import manage_session
from src.variations.models import Variation
from src.variations.utils import get_new_variation_data


class VariationDAO(BaseDAO):
    model = Variation

    @classmethod
    @manage_session
    async def add(cls, user, variation_data, session=None):
        variation_data = variation_data.model_dump()

        if not await has_permission(user):
            raise_http_exception(ForbiddenException)

        await cls._validate_category_by_id(variation_data["category_id"])

        existing_variation = await cls.find_one_or_none(**variation_data)

        if existing_variation:
            raise_http_exception(VariationAlreadyExistsException)

        return await cls._create(**variation_data)

    @classmethod
    @manage_session
    async def _validate_category_by_id(cls, category_id, session=None):
        product_category = await ProductCategoryDAO.find_by_id(category_id)

        if not product_category:
            raise_http_exception(ProductCategoryNotFoundException)

    @classmethod
    @manage_session
    async def find_by_id(cls, model_id, session=None) -> model:
        query = (
            select(cls.model)
            .options(joinedload(cls.model.category))
            .filter_by(id=model_id)
        )

        result = await session.execute(query)

        return result.unique().mappings().one_or_none()["Variation"]

    @classmethod
    @manage_session
    async def change(cls, variation_id, user, data, session=None):
        data = data.model_dump(exclude_unset=True)

        if not await has_permission(user):
            raise_http_exception(ForbiddenException)

        current_variation = await cls.validate_by_id(variation_id)

        if not current_variation:
            return None

        if not data:
            return current_variation

        if "category_id" in data:
            if not await ProductCategoryDAO.validate_by_id(
                data["category_id"]
            ):
                raise_http_exception(ProductCategoryNotFoundException)

        new_variation_data = get_new_variation_data(current_variation, data)

        existing_variation = await cls.find_one_or_none(**new_variation_data)

        if existing_variation:
            raise_http_exception(VariationAlreadyExistsException)

        return await cls.update_data(variation_id, data)

    @classmethod
    @manage_session
    async def delete(cls, user, variation_id, session=None):
        if not await has_permission(user):
            raise_http_exception(ForbiddenException)

        # Get current variation
        variation = await cls.validate_by_id(variation_id)

        if not variation:
            return None

        # Delete the variation
        await cls.delete_certain_item(variation_id)
