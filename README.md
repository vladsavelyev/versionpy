# VersionPy

Small utility to version and release your tools.

Tracks the version using the file `your_package/_version.py`.

## Initialising

Set version to `0.0.1`:

```
bump 0.0.1
```

Versionpy either finds `_version.py`, or inititates it in the main package.

If the argument is ommited, will set the version to `0.0`.

If you have several packages in the project and want to store `_version.py` in a particular on, use `-p`:

```
bump 0.0.1 -p your_package
```

## Usage:

Increment bugfix (patch) component (`0.0` -> `0.0.1`):

```
bump
```

Increment minor component (0.0.1 -> 0.1):

```
bump minor
```

Allowed first arguments: major, minor, bugfix/patch, or exact version in format of 2 or 3-component version 
with a possible pre-prerelease component:

    - 1.0.0
    - 2.1
    - 2.0pre
    - 2.0.2a1
