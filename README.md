# Loud Noise Detector

[![PyPI version](https://img.shields.io/pypi/v/loud-noise-detector.svg)](https://pypi.org/project/loud-noise-detector/)
[![Python Versions](https://img.shields.io/pypi/pyversions/loud-noise-detector.svg)](https://pypi.org/project/loud-noise-detector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/endika2i)

A Python system designed to detect and record significant noises in your home when you're away. Inspired by the need to monitor our pets when they're left alone at home for short periods, detecting barks or other sounds that might indicate distress or discomfort. It's also an ideal practical solution for parents who need to know if their baby is crying in another room. Perfect for any situation where you need to be informed about important sounds occurring in spaces where you can't be physically present.

## 🚀 Features

- Real-time detection of significant sounds (barking, crying, etc.)
- Customizable noise thresholds to match your needs
- Automatic recording when relevant sounds are detected
- Instant notification system
- Detailed event logging
- Easy to configure and customize

## 📋 Requirements

- Python 3.6 or higher
- PortAudio (for PyAudio) Ubuntu: `sudo apt install python3-dev portaudio19-dev`
- Working microphone

## 🔧 Installation

### From PyPI

```bash
pip install loud-noise-detector
```

### From Source

1. Clone the repository:

```bash
git clone https://github.com/Endika/loud-noise-detector.git
cd loud-noise-detector
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# On Windows
.\.venv\Scripts\activate
# On Unix or MacOS
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install development dependencies (optional):

```bash
pip install -r dev-requirements.txt
```

## ⚙️ Configuration

### Command Line Arguments

| Argument             | Default Value                | Description                          |
| -------------------- | ---------------------------- | ------------------------------------ |
| `--config`           | `config/default_config.yaml` | Path to configuration file           |
| `--verbose`, `-v`    | `False`                      | Enable verbose output                |
| `--output-dir`, `-o` | `data/recordings`            | Directory to save recordings         |
| `--threshold`, `-t`  | -                            | RMS threshold to trigger detection   |
| `--language`, `-l`   | `en`                         | Language for messages (`en` or `es`) |
| `--no-keep-files`    | `False`                      | Delete recording files after sending |

### Configuration File Options

| Parameter            | Default Value   | Description                                  |
| -------------------- | --------------- | -------------------------------------------- |
| `threshold`          | `0.1`           | Sound level threshold to trigger detection   |
| `cooldown_seconds`   | `5`             | Time to wait between detections              |
| `seconds_to_record`  | `5`             | Duration of recording after detection        |
| `pre_buffer_seconds` | `2`             | Seconds of audio to keep before detection    |
| `rate`               | `44100`         | Audio sampling rate                          |
| `channels`           | `1`             | Number of audio channels (1=mono, 2=stereo)  |
| `format`             | `8`             | Audio format (pyaudio.paInt16)               |
| `chunk_size`         | `1024`          | Size of audio chunks to process              |
| `keep_files`         | `True`          | Whether to keep recording files              |
| `verbose`            | `False`         | Enable detailed logging                      |
| `timestamp_format`   | `%Y%m%d_%H%M%S` | Format for timestamp in filenames            |
| `language`           | `en`            | Interface language (`en` or `es`)            |
| `notifier_options`   | `{}`            | Additional options for notification services |

## 🔐 Environment Setup

Generate your `.env` file with all necessary configurations:

```bash
# Generate .env file
cat > .env << EOL
# Slack configuration (required for Slack notifications)
SLACK_TOKEN=xoxb-your-token-here
SLACK_CHANNEL=CHANNEL-ID-HERE
EOL
```

#### Environment Variables Description

| Variable        | Required | Default | Description                                |
| --------------- | -------- | ------- | ------------------------------------------ |
| `SLACK_TOKEN`   | Yes      | -       | Your Slack bot token (starts with `xoxb-`) |
| `SLACK_CHANNEL` | Yes      | -       | Channel where notifications will be sent   |

> **Note**: For Slack notifications, you'll need to:
>
> 1. Create a Slack App in your workspace
> 2. Add `chat:write` and `files:write` OAuth scopes
> 3. Install the app to your workspace
> 4. Copy the Bot User OAuth Token to `SLACK_TOKEN`
> 5. Copy the Channel ID to `SLACK_CHANNEL`

### Configuration Examples

#### For Pet Monitoring

```yaml
threshold: 0.2 # Higher threshold for louder sounds like barking
cooldown_seconds: 30 # Longer cooldown to avoid too many notifications
seconds_to_record: 10 # Longer recording to capture context
pre_buffer_seconds: 3 # Capture sound before the bark
notifier_options:
  slack_channel: CHANNEL-ID-HERE
```

#### For Baby Monitoring

```yaml
threshold: 0.15 # Lower threshold to detect crying
cooldown_seconds: 10 # Shorter cooldown for more frequent checks
seconds_to_record: 5 # Shorter recording duration
pre_buffer_seconds: 1 # Less pre-recording needed
notifier_options:
  slack_channel: CHANNEL-ID-HERE
```

You can create a configuration file in either YAML or JSON format. Place it in the `config/` directory or specify its location using the `--config` argument.

## 🎯 Usage

### Basic Usage

```bash
# Start the noise detector with default settings
loud-noise-detector

# Start with custom configuration file
loud-noise-detector --config path/to/config.yml

# Run in debug mode
loud-noise-detector --debug
```

### As a Python Module

```shell
python -m src.main
```

## 📊 Development

### Running Tests

```bash
# Run all tests
make test
```

### Code Quality

```bash
# Run linting
make lint

# Run type checking
make quality
```

## 🤝 Contributing

This project uses [Semantic Release](https://python-semantic-release.readthedocs.io/) for versioning.

### Commit Message Format

Your commit messages must follow this format to trigger automatic version updates:

### Development Workflow

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit with appropriate message format
5. Push to your branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Built with Python and PyAudio
- Inspired by the need for reliable noise monitoring solutions

## 📫 Contact

Endika Iglesias - endika2@gmail.com

Project Link: [https://github.com/Endika/loud-noise-detector](https://github.com/Endika/loud-noise-detector)
