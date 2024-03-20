from functools import wraps

from src.database import async_session_factory


def manage_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with async_session_factory() as session:
            kwargs["session"] = session
            return await func(*args, **kwargs)

    return wrapper


def add_is_default_to_every_user_address(user_data, subquery_result):
    address_data_with_is_default = []

    # Define whether is_default for current address is true or false
    for address in user_data.addresses:
        is_default = next(
            (
                item.is_default
                for item in subquery_result.scalars()
                if item.address_id == address.id
            ),
            False,
        )

        # Add is-default field to other fields in the dictionary
        address_data_with_is_default.append(
            {
                "id": str(address.id),
                "unit_number": address.unit_number,
                "street_number": address.street_number,
                "address_line1": address.address_line1,
                "address_line2": address.address_line2,
                "city": address.city,
                "region": address.region,
                "postal_code": address.postal_code,
                "country": {
                    "name": address.country.name,
                    "id": str(address.country.id),
                },
                "is_default": is_default,
            }
        )

    user_data_dict = {
        key: value
        for key, value in user_data.__dict__.items()
        if not key.startswith("_")
    }

    user_data_dict["addresses"] = address_data_with_is_default

    return user_data_dict


def get_new_address_data(current_address, address_data):
    current_address_data = {
        x.name: getattr(current_address, x.name)
        for x in current_address.__table__.columns
    }

    new_address_data = {**current_address_data, **address_data}

    new_address_data.pop("id")

    return new_address_data
