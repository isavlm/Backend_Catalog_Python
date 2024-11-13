from typing import Any


class RepositoryConfig:
    _REPOSITORY: str
    _AVAILABLE_REPOSITORIES: list[str]

    @classmethod
    def get_repository(cls) -> Any:
        if not cls._is_valid_repository():
            raise Exception("Requested repository not available.")

        repository_instances = cls._get_repository_instances()

        return repository_instances.get(cls._REPOSITORY)

    @classmethod
    def _is_valid_repository(cls) -> bool:
        return cls._REPOSITORY in cls._AVAILABLE_REPOSITORIES

    @classmethod
    def _get_repository_instances(cls) -> dict:
        raise NotImplementedError(
            "Subclasses must implement _create_repository_instances."
        )
