from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    redis_host: str = "foo"
    redis_password: str = "bar"
    redis_url: str = "baz"
