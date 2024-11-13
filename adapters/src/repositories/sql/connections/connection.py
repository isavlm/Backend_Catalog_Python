from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def get_connection_string(self) -> str:
        raise NotImplementedError
