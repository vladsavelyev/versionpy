# release

Small utility to version and release your tools

The tool keeps track of the version in a file `your_package/_version.py`. On first run, it will initiate this file.

## Usage:

Set version to 0.0.1 (finds `_version.py` or inititates this file in the main package):

```
release 0.0.1
```

Set version to 0.0.1 in the package `your_package`:

```
release 0.0.1 -p your_package
```

Increment bugfix version (0.0.1 -> 0.0.2):

```
release
```

Increment minor version (0.0.1 -> 0.1.0):

```
release minor
```

Allowed first arguments: bugfix, minor, major, or version in format *.*.*
