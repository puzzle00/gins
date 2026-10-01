# Short Design Document
(__NOTE:__ Integers are release versions, what most people would have as fractions - for example Gins `4.0` is like AnyProject `1.4`. All fractions are the in-development mini-milestones. What AnyProject `2.0` is in the Gins system would be E.G. Gins `4.0(E)`, which is a Final Release of a SDD, in this case SDD 1 "Package Management".)

***

**Current Milestone:** `Gins 0.1`

***

## Next Milestones:

### Gins `1.0` - Create uninstallation scripts
+ Gins `0.1` Make internal view (`-I` flag)
+ Gins `0.2` Create `mgins.py` (Gins manager) CLI tool and GREPO format for uninstalling GINS packages - command should be `python mgins.py remove <packagename>`
+ Gins `0.3` Crossplatformise new changes
+ Gins `1.0` Release Gins `1.0`

### Gins `2.0` - Create `GinsCheckUpdate`
+ Gins `1.1` Make the API for Ginsupdate that only shows the current Milestone (integer) version. Coding practice change: keep Fractionals in a different folder (`latest`) while they are not integers. (how?)
+ Gins `1.2` Edit Setup and `mgins` to check for updates when run
+ Gins `1.3` Crossplatformise new changes
+ Gins `2.0` Release Gins `2.0`

### Gins `3.0` - Create `GinsDoUpdate`
+ Gins `2.1` Create `mgins` command `python mgins.py update-installer </path/to/package/.gins/folder>`
+ Gins `2.2` Cause the command to remove the entire installer and replace it with a new one sourced off Github. It is important, then, to keep the installer static and not connected to anything the project devs change. Any of that should be in the `GPTH.toml`.
+ Gins `2.3` Crossplatformise new changes
+ Gins `3.0` Release Gins `3.0`

### Gins `4.0(E)` - Create `GinsPackageUpdater`
+ Gins `3.1` Remove old update-file system from setup file (`stuff` function)
+ Gins `3.2` Create `mgins` command `python mgins.py update-package <packagename>`
+ Gins `3.3` Make it so that command:
  1. Finds the package path by looking for the `packagename` in the GREPO file.
  2. Removes that path from the PTH files.
  3. Removes the entire package folder
  4. Removes the GREPO entry
  5. Reclones the installation directory
  6. Reruns setup file for correct OS
+ Gins `3.4` Add the new `mgins.py update-package` system to the setup file where the old update-file system was, or just add an info message and then an abort with code 0.
+ Gins `3.5` Crossplatformise new changes
+ Gins `4.0(E)` Release Gins `4.0(E)`

END SHORT DESIGN DOCUMENT. ANY 
