import os
from typing import Any, Dict, Generator
from unittest.mock import MagicMock, patch

import pytest

from src.notifiers.slack import SlackNotifier
from src.utils.config import Config

TEST_RECORDING = {"path": "/tmp/test_recording.wav", "format": "wav"}
TEST_RECORDINGS = [TEST_RECORDING]
TEST_TIMESTAMP = "timestamp"
TEST_THRESHOLD = 0.5


class TestSlackNotifier:
    @pytest.fixture
    def config(self) -> Config:
        config = Config()
        return config

    @pytest.fixture
    def notifier(self) -> SlackNotifier:
        return SlackNotifier()

    @pytest.fixture
    def env_with_slack_config(self) -> Generator[None, None, None]:
        with patch.dict(
            os.environ,
            {"SLACK_TOKEN": "test_token", "SLACK_CHANNEL": "test_channel"},
            clear=True,
        ):
            yield

    @pytest.fixture
    def mock_file_read(self) -> Generator[None, None, None]:
        mock_content = MagicMock()
        mock_content.read.return_value = b"content"

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_content
        mock_file.__exit__.return_value = None

        with patch("builtins.open", return_value=mock_file):
            yield

    @pytest.fixture
    def mock_successful_upload(
        self, mock_file_read: Generator[None, None, None]
    ) -> Generator[MagicMock, None, None]:
        mock_response = MagicMock()
        mock_response.json.return_value = {"ok": True}

        mock_post = MagicMock()
        mock_post.return_value = mock_response

        with patch("requests.post", mock_post):
            yield mock_post

    @pytest.fixture
    def mock_logger(self) -> MagicMock:
        return MagicMock()

    @pytest.fixture
    def config_with_logger(
        self, config: Config, mock_logger: MagicMock
    ) -> Generator[Config, None, None]:
        with patch.object(config, "logger", mock_logger):
            yield config

    @pytest.mark.parametrize(
        "env_vars,expected_result,error_count",
        [
            ({"SLACK_TOKEN": "test_token"}, False, 1),
            ({"SLACK_CHANNEL": "test_channel"}, False, 1),
            ({}, False, 1),
        ],
    )
    def test_notify_missing_config(
        self,
        notifier: SlackNotifier,
        config_with_logger: Config,
        mock_logger: MagicMock,
        env_vars: Dict[str, str],
        expected_result: bool,
        error_count: int,
    ) -> None:
        with patch.dict(os.environ, env_vars, clear=True):
            result = notifier.notify(
                [], TEST_TIMESTAMP, TEST_THRESHOLD, config_with_logger
            )

            assert result is expected_result
            assert mock_logger.error.call_count == error_count

    def test_notify_successful(
        self,
        notifier: SlackNotifier,
        config: Config,
        mock_successful_upload: MagicMock,
        env_with_slack_config: Generator[None, None, None],
    ) -> None:
        result = notifier.notify(TEST_RECORDINGS, "timestamp", 0.5, config)
        assert result is True

    @pytest.mark.parametrize(
        "response_data,expected_result,error_count",
        [
            ({"ok": False, "error": "some_error"}, False, 3),
            (Exception("Test error"), False, 3),
        ],
    )
    def test_notify_handles_api_errors_and_exceptions(
        self,
        notifier: SlackNotifier,
        config_with_logger: Config,
        mock_logger: MagicMock,
        response_data: Any,
        expected_result: bool,
        error_count: int,
        env_with_slack_config: Generator[None, None, None],
        mock_file_read: Generator[None, None, None],
    ) -> None:
        if isinstance(response_data, Exception):
            mock_post = MagicMock()
            mock_post.side_effect = response_data
        else:
            mock_response = MagicMock()
            mock_response.json.return_value = response_data
            mock_post = MagicMock()
            mock_post.return_value = mock_response

        with patch("requests.post", mock_post):
            result = notifier.notify(
                TEST_RECORDINGS,
                TEST_TIMESTAMP,
                TEST_THRESHOLD,
                config_with_logger,
            )

            assert result is expected_result
            assert mock_logger.error.call_count == error_count

    @pytest.mark.parametrize(
        "config_source,expected_token,expected_channel",
        [
            ("env", "test_token", "test_channel"),
            ("config", "config_token", "config_channel"),
            ("params", "param_token", "param_channel"),
        ],
    )
    def test_create_if_configured_sources(
        self,
        config: Config,
        config_source: str,
        expected_token: str,
        expected_channel: str,
    ) -> None:
        if config_source == "env":
            with patch.dict(
                os.environ,
                {"SLACK_TOKEN": "test_token", "SLACK_CHANNEL": "test_channel"},
                clear=True,
            ):
                notifier = SlackNotifier.create_if_configured(config)
        elif config_source == "config":
            config.notifier_options = {
                "slack": {"token": "config_token", "channel": "config_channel"}
            }
            notifier = SlackNotifier.create_if_configured(config)
        else:
            notifier = SlackNotifier.create_if_configured(
                config, token="param_token", channel="param_channel"
            )

        assert notifier is not None
        assert notifier.token == expected_token
        assert notifier.channel == expected_channel

    def test_notify_no_recordings(
        self,
        notifier: SlackNotifier,
        config_with_logger: Config,
        mock_logger: MagicMock,
        env_with_slack_config: Generator[None, None, None],
    ) -> None:
        result = notifier.notify(
            [], TEST_TIMESTAMP, TEST_THRESHOLD, config_with_logger
        )

        assert result is False
        assert mock_logger.error.call_count == 1

    def test_create_if_configured_no_config(self, config: Config) -> None:
        with patch.dict(os.environ, {}, clear=True):
            config.notifier_options = {}

            notifier = SlackNotifier.create_if_configured(config)

            assert notifier is None
