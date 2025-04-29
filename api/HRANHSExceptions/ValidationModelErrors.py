class InvalidPhoneNumberError(ValueError):
    message:str = "Phone number must start with '07' and be exactly 11 digits."