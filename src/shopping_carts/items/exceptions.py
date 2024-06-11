from fastapi import status

from src.exceptions import EcommerceException


class ShoppingCartItemNotFoundException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Shopping Cart Item not found."


class ShoppingCartItemsNotFoundException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Shopping Cart Items not found."


class QuantityLessThanOneException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Quantity should be at least one."


class ShoppingCartItemNotImplementedException(EcommerceException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Failed to add shopping cart item."
