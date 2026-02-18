# gins
GitHub Install, a system for installing Python packages by `git clone`'ing them.
## Reasoning
> I own an Ubuntu computer, and am annoyed by the thing where you have to be in a venv to get packages, or use the lengthy `--break_system_packages` flag. This is for helping people with the same problem.
## Use
> If you wish to use gins, copy the `src` folder to your project repository and rename it `gins`. Then add a `gins.md` file next to the `gins` folder, and copy the Installation section of this file to it. In order to let GINS know where to find a file, make a `.GPTH` file, and put the path to your project files in it, from your project root. If you wish to download only specific files, put them on seperate lines. Usually, this will be something like
```
src/*.py
```
> You can use wildcards in `.GPTH`.
> A GINS-enabled project may look like:
```
project/-
        |- .GPTH
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
## Installation
> In order to install a GINS-downloaded project, `git clone` the repo to a directory you own. Then run the `setup_<Shell>` file corresponding to your shell. This file will create a new directory in your home directory (.gins) if it does not already exist and permanently edit your `PYTHONPATH` to add .gins to it, again, if that has not been done before. It then takes all files in the speFor Linux & MacOS users, this may involve changing your `.<Shell>rc` or `.<Shell>_profile` file in order for the changes to be permanent. The home directory is as follows:
> - For Linux users, this is `/home/username`.
> - For Mac users, this is `/Users/username`.
> - For Windows users, this is `C:\Users\username\`.
>
> ### Supported Shells
>> - PowerShell
>> - Bash
>> - Zsh
>> - Fish
>> - Windows Command Prompt
> ### Using your GINS-installed packages
>> Gins packages can be used like any Python package. Just `import` them.
