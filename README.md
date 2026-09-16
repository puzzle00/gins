# gins - SELF CONTAINED PACKAGE MANAGER
GitHub Install, a system for installing Python packages by `git clone`'ing them.
## Reasoning
> I own an Ubuntu computer, and am annoyed by the thing where you have to be in a venv to get packages, or use the lengthy `--break_system_packages` flag. This is for helping people with the same problem. Also, I am having trouble with uploading to PyPi.
## Use
> If you wish to use gins, copy the `src` folder to your project repository and rename it `gins`. Then add a `gins.md` file next to the `gins` folder, and copy the Installation section of this file to it. In order to let GINS know where to find a file, make a `GPTH.toml` file, and follow the template provided. The GPTH file needs to look like this:
```toml
[gins] # required
projectname="myproject" # Put your project's package name in here.
filenames=[ # required
"src/__init__.py",
"src/whatever.py",
"src/quokka/*.py" # Put your file list in here, wildcards are OK!
dependencies=[
"pip:yourproject", # For pip projects, prepend the project name (No PPAs for now) with "pip:"
"gins:username/reponame" # For gins projects, follow this syntax.
]
```
> After (or before) the `[gins]` header, you can put anything you want and GINS will ignore it. (Actually, all you need is for there to be a valid `[gins]` header and content)
>
> Your project should have a `__init__.py` file with a package import syntax in it (hehehe init/in it). If you are unfamiliar with `__init__.py` syntax, you put either `import .whatever` for `whatever.py` in the same folder as the `__init__.py` file, or `from .afolder import myfile` for `myfile.py` in `afolder` that is next to `__init__.py`.
> 
> A GINS-enabled project may look like:
```
project
        |- GPTH.toml
        |- .gins/-
        |        |- # gins files
        |
        |- src/-
        |      |- # your project
        |
        |- gins.md
        |- readme.md
```
> Copy the GINS header bar (md format) from this repo and put it at the top of your README.
>
## Installation
> In order to install a GINS-downloaded project, `git clone` the repo to a directory you own. Then run the `setup<OS>.py` file corresponding to your OS. For Linux or Mac users, one of these options must be added to the command:
```
-b - Bash shell
-c - C shell
-f - fish shell
-t - TCSH
-z - Z shell
-k - Korn Shell
```
> If your preferred shell isn't on here, go over to the Issues page and put on an issue!
> This file will create a new directory in your home directory (`.gins`) if it does not already exist and permanently edit your `PYTHONPATH` to add `.gins` to it, again, if that has not been done before. It then takes all files in the GPTH and puts them in their folder (named after the package name) in `.gins`For Linux & MacOS users, this may involve changing your `.<Shell>rc` or `.<Shell>_profile` file in order for the changes to be permanent. The home directory is as follows:
> - For Linux users, this is `/home/username`.
> - For Mac users, this is `/Users/username`.
> - For Windows users, this is `C:\Users\username\`.
> Then you can delete the installation folder.
> ### Supported OSs:
>> -  Windows
>> - Mac
>> - Linux
> ### Using your GINS-installed packages
>> Gins packages can be used like any Python package. Just `import` them.
