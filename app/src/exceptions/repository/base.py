class RepositoryException(Exception):
    def __init__(self, entity_type: str, method: str):
        message = f"Exception while executing {method} in {entity_type}"
        super().__init__(message)
