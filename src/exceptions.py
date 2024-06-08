from fastapi import HTTPException, status


class EcommerceException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


def raise_http_exception(exception_class):
    raise HTTPException(
        status_code=exception_class.status_code, detail=exception_class.detail
    )


class ForbiddenException(EcommerceException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Forbidden"


class CardAlreadyConnectedWithOtherUserException(EcommerceException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Card is already connected to other user."


class UserProfileNotFoundException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User profile not found."


class CountriesNotFoundException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Countries not found."


class CountryNotFoundException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Country not found."


class WrongNameOrSurnameException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid First Name or Last Name."


class WrongCountryNameException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid country name."


class WrongRatingValueException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Rating value must be from 1 to 5."


class WrongUnitOrPostalCodeException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid Unit number or postal code."


class WrongStreetNumberException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid street number."


class UserAlreadyHasCartException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "User already has a cart."


class UserAlreadyHasProfileException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "User already has a profile."


class UserDoesNotHaveCartException(EcommerceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User does not have a cart."


class WrongProviderNameException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid Provider."


class WrongPriceException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid format of price."


class WrongQuantityException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid format of quantity."


class PriceLessOrEqualZeroException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Price should be more than zero."


class QuantityLessThanZeroException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Quantity should be more than zero."


class QuantityLessThanOneException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Quantity should be at least one."


class WrongAccountNumberException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid Account Number."


class ExpiredCardException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Your Card is Expired."


class InvalidCardException(EcommerceException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Card number should have 16 digits."


class UserProfileNotImplementedException(EcommerceException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Failed to add user profile."
