from abc import ABC, abstractmethod
from typing import Any

from src.utils.config import Config


class BaseRecorder(ABC):
    @abstractmethod
    def save(
        self,
        chunks: list[bytes],
        config: Config,
        timestamp: str,
        normalized_rms: float,
    ) -> dict[str, Any]:
        raise NotImplementedError("Recorder must implement save")

    @abstractmethod
    def remove_file(self, file_path: str, config: Config) -> bool:
        raise NotImplementedError("Recorder must implement remove_file")
