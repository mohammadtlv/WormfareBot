from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: arsamtlv1
    API_HASH: str

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: int = 200

    ADD_SLAPS_ON_TURBO: int = 2500

    AUTO_UPGRADE_SLAP: bool = True
    MAX_SLAP_LEVEL: int = 10
    AUTO_UPGRADE_ENERGY: bool = True
    MAX_ENERGY_LEVEL: int = 10
    AUTO_UPGRADE_CHARGE: bool = True
    MAX_CHARGE_LEVEL: int = 5

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    RANDOM_SLAPS_COUNT: list[int] = [50, 200]
    SLEEP_BETWEEN_SLAP: list[int] = [20, 30]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
