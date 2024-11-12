import os


def parse_env_variable(env_variable: str) -> str:
    value = os.environ.get(env_variable)
    if value is not None:
        return value
    else:
        raise Exception(f"{env_variable} was not found in the environment variables")
