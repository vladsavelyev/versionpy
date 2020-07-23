# Versionpy

![CI](https://github.com/vladsaveliev/versionpy/workflows/CI/badge.svg) [![Anaconda-Server Badge](https://anaconda.org/vladsaveliev/versionpy/badges/installer/conda.svg)](https://conda.anaconda.org/vladsaveliev/versionpy) [![PyPI version](https://badge.fury.io/py/versionpy.svg)](https://badge.fury.io/py/versionpy)

A small utility to version and release your python tools. Doesn't need any configuration files.

## Install

```
conda install -c vladsaveliev versionpy
```

## Usage

Set version to `0.1.2`, create a git tag and push:

```
$ bump 0.1.2
```

Increment the patch component (e.g. `0.1.2` -> `0.1.3`), create a tag and push:

```
$ bump
```

Increment the minor component (e.g. `0.1.3` -> `0.2`), create a git tag and push:

```
$ bump minor
```

Allowed first arguments: `major`, `minor`, `patch`/`bugfix`, or specific version following the format of 2 to 3 components with a possible pre-release component:

    - 1.0.0
    - 2.1
    - 2.0pre
    - 2.0.2a1
   
You can also check current version with a single command:

```
$ version
0.2.1
```


## Under the hood

Versionpy tracks the version number in a file `<your_package>/_version.py`.

When you execute `bump` for the first time, it will try to locate `*/_version.py`, and if it's not found, it will initialize it in the main package according to `setup.py`. If `setup.py` specifies multiple packages, it will not be able to derive the main package folder, so you can specify it with `-p`:

```
bump 0.0.1 -p your_package
```

If the version argument is ommited, versionpy will check for a file named `VERSION` or `VERSION.txt`, otherwise will set it to `0.1.0`.

The order of commands performed on `bump`:

```
#push any existing un-pushed commits:
$ git push

#update the version file:
>> version_file, new_version = increment_version(new_version, package_name)
$ git add {version_file}

#new commit named "Bump version":
$ git commit -m "Bump {new_version}"'

#new (annotated) tag pointing to the commit "Bump version"
#because only annotated tags can be pushed with a regular commit at the same time,
#see https://stackoverflow.com/questions/3745135/push-git-commits-tags-simultaneously
$ git tag -a {new_version} -m "Release {new_version}"'

#finally, push the commit and the tag together:
$ git push --follow-tags'
```

If you have CI set up, both the tag and the "Bump" commit will trigger the CI run, so you might wanna disable one of them. E.g. for GitHub workflows:

```
jobs:
  build-test-publish:
    # For tag pushes, we want to assure only the tag event triggers CI,
    # not the accompanying commit:
    if: "! startsWith(github.event.head_commit.message, 'Bump ') || startsWith(github.ref, 'refs/tags/')"
    steps:
       ...
```

You can check out [the full example here](https://github.com/vladsaveliev/versionpy/blob/master/.github/workflows/workflow.yml).


