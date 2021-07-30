# ChangeLog 
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] 2021-07-29
## Changed
- http.client to requests library

## Fixed
- case where Auth0 returns content that isn't parseable JSON

## [1.0.6] 2018-06-06
## Changed
- Support for python 3+ but also < 3.6

## [1.0.5] 2018-05-31
## Changed
- Fixed get_logs()
- Slightly less empty README and doc

## Added
- Support for automatically renewing access_token

## [1.0.4] 2018-04-23
## Changed
- Fixed get_users() and get_user()

## [1.0.3] 2018-03-31
## Changed
- Added support for creating auth0 clients

## [1.0.2] 2018-03-08
## Changed
- Test support removed from setup.py (supports auto test discovery)
- Fixed makefile targets to be consistent and make travis use them

## [1.0.1]  2018-03-08
### Added
- Support for create,update,delete,get clients in Auth0 library
- Basic tests cases

## Changed
- Moved library from https://github.com/mozilla-iam/auth0-scripts to https://github.com/mozilla-iam/authzerolib

## [1.0.0] - 2018-03-02
### Added
- This ChangeLog
- authzerolib support for client updates and basic rules loading

[Unreleased]: https://github.com/mozilla-iam/authzerolib/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.6...v1.1.0
[1.0.6]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.5...v1.0.6
[1.0.5]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.4...v1.0.5
[1.0.4]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.3...v1.0.4
[1.0.3]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.2...v1.0.3
[1.0.2]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/mozilla-iam/authzerolib/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v1.0.0