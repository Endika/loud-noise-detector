# Changelog

## [3.1.5](https://github.com/Endika/loud-noise-detector/compare/v3.1.4...v3.1.5) (2026-09-28)


### Bug Fixes

* keep listening when a notifier fails ([46fdb9d](https://github.com/Endika/loud-noise-detector/commit/46fdb9d5e846ac95522da34504469ac51310bce1))
* keep the recording when no notification got through ([c1003c2](https://github.com/Endika/loud-noise-detector/commit/c1003c249ce5a493d531a238eeed76aa5904c485))
* time out Slack requests ([71d939d](https://github.com/Endika/loud-noise-detector/commit/71d939dcd114cb4b6e0897ede1a42dea3e01729d))

## [3.1.4](https://github.com/Endika/loud-noise-detector/compare/v3.1.3...v3.1.4) (2026-09-28)


### Bug Fixes

* let the config file language apply unless --language is given ([cfb3e6f](https://github.com/Endika/loud-noise-detector/commit/cfb3e6f01813d6e188988396c1aad305b0ce8189))


### Performance Improvements

* read each translation file once instead of on every message ([1d9b5f0](https://github.com/Endika/loud-noise-detector/commit/1d9b5f04afde12c0b1b1e18eb988af7eba786261))

## [3.1.3](https://github.com/Endika/loud-noise-detector/compare/v3.1.2...v3.1.3) (2026-09-27)


### Bug Fixes

* let the Slack channel come from .env instead of a placeholder ([20c4d00](https://github.com/Endika/loud-noise-detector/commit/20c4d00e08737fc02c45ea8b62a6f43bd32e7d2e))

## [3.1.2](https://github.com/Endika/loud-noise-detector/compare/v3.1.1...v3.1.2) (2026-09-27)


### Documentation

* correct Python range, install steps, flags and Slack config in README ([1853dab](https://github.com/Endika/loud-noise-detector/commit/1853dab4f8c35f21707fa48bd75765d694e6bdb9))

## [3.1.1](https://github.com/Endika/loud-noise-detector/compare/v3.1.0...v3.1.1) (2026-09-17)


### Bug Fixes

* **mypy:** drop the python_version pin that broke on numpy stubs ([5917196](https://github.com/Endika/loud-noise-detector/commit/591719668310bec344dcb5311151da34d909aaf8))
* **tests:** give BenchmarkFixture protocols a statement body ([4f36d07](https://github.com/Endika/loud-noise-detector/commit/4f36d07529a52b579e530afee705c489b921f494))

## [3.1.0](https://github.com/Endika/loud-noise-detector/compare/v3.0.0...v3.1.0) (2026-09-16)


### Features

* **ci:** add CodeQL static analysis ([d12f33d](https://github.com/Endika/loud-noise-detector/commit/d12f33d292ffc69d83c75b2a86a0c216c4f432fe))
* **ci:** block PRs that introduce high-severity dependency advisories ([f487270](https://github.com/Endika/loud-noise-detector/commit/f4872708e577c19c383a70a9a4c74022e40ce840))

## [3.0.0](https://github.com/Endika/loud-noise-detector/compare/v2.1.0...v3.0.0) (2026-05-30)


### ⚠ BREAKING CHANGES

* minimum supported Python is now 3.10.

### Features

* drop end-of-life Python 3.9, require 3.10+ ([6d60623](https://github.com/Endika/loud-noise-detector/commit/6d60623e43b2459e41051ed5d3f05f6c287aa272))
* **typing:** ship py.typed marker ([0d64a74](https://github.com/Endika/loud-noise-detector/commit/0d64a74181970bc063fde97b6d98efd348a61b61))


### Bug Fixes

* **build:** exclude test files from the published package ([edc1030](https://github.com/Endika/loud-noise-detector/commit/edc1030ae553313bdbde60d6983dac612eee465c))

## [2.1.0](https://github.com/Endika/loud-noise-detector/compare/v2.0.2...v2.1.0) (2026-03-30)


### Features

* **release:** force new release ([8df5f05](https://github.com/Endika/loud-noise-detector/commit/8df5f05f2b88d4869116aa03301d977897590313))
