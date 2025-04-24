class FieldNotExistException(Exception):
    """
    Exception raised when a specified field does not exist.
    """

    def __init__(self, field_name):
        self.field_name = field_name
        super().__init__(f"The field '{field_name}' does not exist.")