class InvalidPhoneNumberError(ValueError):
    message:str = "Phone number must start with '07' and be exactly 11 digits."
    regex:str = r'^(0(1|2|3|7|8)\d{8,9})$'

class InvalidEmailError(ValueError):
    message:str = "Invalid email format."
class InvalidImageURL(ValueError):
    message:str = "Invalid image format, use http link."