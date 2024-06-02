from fastapi import status

from src.products.items.responses import (
    PRODUCT_ITEM_NOT_FOUND,
    PRODUCT_ITEMS_NOT_FOUND,
)
from src.responses import (
    DELETED_RESPONSE,
    FORBIDDEN_RESPONSE,
    UNAUTHORIZED_RESPONSE,
)
from src.shopping_carts.responses import SHOPPING_CART_NOT_FOUND_RESPONSE


SHOPPING_CART_ITEM_NOT_FOUND_RESPONSE = {
    status.HTTP_404_NOT_FOUND: {
        "content": {
            "application/json": {
                "examples": {
                    "Shopping cart item not found.": {
                        "summary": "Shopping cart item not found.",
                        "value": {"detail": "Shopping cart item not found."},
                    },
                }
            }
        }
    },
}

UNAUTHORIZED_FORBIDDEN_PRODUCT_ITEM_OR_CART_NOT_FOUND_RESPONSE = {
    **UNAUTHORIZED_RESPONSE,
    **FORBIDDEN_RESPONSE,
    **PRODUCT_ITEM_NOT_FOUND,
    **SHOPPING_CART_NOT_FOUND_RESPONSE,
}

UNAUTHORIZED_FORBIDDEN_PRODUCT_ITEMS_OR_CART_OR_SHOPPING_CART_ITEM_NOT_FOUND_RESPONSE = {
    **UNAUTHORIZED_RESPONSE,
    **FORBIDDEN_RESPONSE,
    **PRODUCT_ITEMS_NOT_FOUND,
    **SHOPPING_CART_NOT_FOUND_RESPONSE,
    **SHOPPING_CART_ITEM_NOT_FOUND_RESPONSE,
}

UNAUTHORIZED_FORBIDDEN_PRODUCT_ITEMS_OR_CART_NOT_FOUND_RESPONSE = {
    **UNAUTHORIZED_RESPONSE,
    **FORBIDDEN_RESPONSE,
    **PRODUCT_ITEMS_NOT_FOUND,
    **SHOPPING_CART_NOT_FOUND_RESPONSE,
}

DELETED_UNAUTHORIZED_FORBIDDEN_CART_ITEMS_OR_CART_NOT_FOUND_RESPONSE = {
    **DELETED_RESPONSE,
    **UNAUTHORIZED_RESPONSE,
    **FORBIDDEN_RESPONSE,
    **SHOPPING_CART_ITEM_NOT_FOUND_RESPONSE,
    **SHOPPING_CART_NOT_FOUND_RESPONSE,
}
