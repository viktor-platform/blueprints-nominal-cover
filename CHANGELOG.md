# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased] [dd/mm/yyyy]
### Added
None.

### Changed
None.

### Deprecated
None.

### Removed
None.

### Fixed
None.

### Security
None.

### Internal
- (#25) Changed application_name in viktor.config.toml to registered_name
- (#27) Changed viktor_submodule to gh_token in workflows

## [v0.0.1] [16/01/2025]
### Added
- (#3) Added functionality to fill in parameters needed for the calculation of the nominal concrete cover.
- (#5) Added implementation of table 4.3 and par. 4.4.1.2 and 4.4.1.3 constants according to NEN-EN 1992-1-1:2005+A1:2015+NB:2016+A1:2020
- (#9) Added functionality to fill in additional parameters like deltas, abrasion class, etc.
- (#11) Added webview to show the results of the nominal concrete cover calculation.
- (#15) Added an welcome/introduction tab to the application.

### Changed
- (#14) Changed app type to 'simple app'

### Fixed
- (#15) Fix wrong calculation of 75 years design working life
