from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="loud_noise_detector",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pyaudio>=0.2.11",
        "pyyaml>=5.1",
        "requests>=2.25.0",
    ],
    entry_points={
        "console_scripts": [
            "loud-noise-detector=src.main:main",
        ],
    },
    python_requires=">=3.6",
    author="Endika Iglesias",
    author_email="endika2@gmail.com",
    description="A system for detecting and recording loud noises",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="audio, detection, recording, notification",
    url="https://github.com/Endika/loud-noise-detector",
    project_urls={
        "Source Code": "https://github.com/Endika/loud-noise-detector",
        "Bug Tracker": "https://github.com/Endika/loud-noise-detector/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
