class BusinessException(Exception):
    pass


class NotFoundException(BusinessException):
    def __init__(self, entity_type: str, entity_id: str):
        message = f"The {entity_type} with the id '{entity_id}' does not exist."
        super().__init__(message)


class AlreadyExistsException(BusinessException):
    def __init__(self, entity_type: str, entity_id: str) -> None:
        message = f"The {entity_type} with the id '{entity_id}' already exists."
        super().__init__(message)


class NoneException(BusinessException):
    def __init__(self, entity_type: str) -> None:
        message = f"The {entity_type} is None."
        super().__init__(message)
