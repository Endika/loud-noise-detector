from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from src.utils.config import Config


class BaseNotifier(ABC):

    @classmethod
    @abstractmethod
    def create_if_configured(
        cls,
        config: Config,
        **kwargs
    ) -> Optional['BaseNotifier']:
        raise NotImplementedError("Notifier must implement create_if_configured")

    @abstractmethod
    def notify(
        self,
        recordings: List[Dict[str, Any]],
        timestamp: str,
        normalized_rms: float,
        config: Config,
    ) -> bool:
        raise NotImplementedError("Notifier must implement notify")
