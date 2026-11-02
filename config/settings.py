import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

class Settings:
    """
    Centraliza las variables de configuración del sistema.
    Evita exponer credenciales hardcodeadas en el código fuente.
    """
    API_BASE_URL: str = os.getenv("API_BASE_URL", "https://api.fda.gov/drug/label.json")
    API_KEY: str = os.getenv("API_KEY", "")
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "5"))
    ENABLE_OFFLINE_FALLBACK: bool = os.getenv("ENABLE_OFFLINE_FALLBACK", "True").lower() in ("true", "1", "yes")