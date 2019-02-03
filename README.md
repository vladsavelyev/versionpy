# VersionPy

Small utility to version and release your python tools. Doesn't need any configuration files.

## Install

```
conda install -c vladsaveliev versionpy
```

## Usage

Set version to `0.1.2`:

```
bump 0.1.2
```

Increment bugfix (patch) component (e.g. `0.1.2` -> `0.1.3`):

```
bump
```

Increment minor component (e.g. `0.1.3` -> `0.2`):

```
bump minor
```

Allowed first arguments: `major`, `minor`, `bugfix`/`patch`, or exact version in format of 2 or 3-component version 
with a possible pre-prerelease component:

    - 1.0.0
    - 2.1
    - 2.0pre
    - 2.0.2a1
   
For a tracked tool, you can check current version with:
    
```
version
```


## Under the hood

VersionPy tracks the version number in the file `your_package/_version.py`.

When you run it for the first time, VersionPy would try to locate `_version.py`, or `VERSION.txt`, and if needed initialize `_version.py` it in the main package.

If you have several packages in the project and want to store `_version.py` in a particular one, use `-p`:

```
bump 0.0.1 -p your_package
```

If the version argument is ommited, will set the version to `0.0`.
