# Short Design Document

**Current Milestone:** `Gins 0 Crossplatform`

## Next Milestones:

Gins `1.0` - Create uninstallation scripts
+ Gins `0.1` Make internal view (`-I` flag)
+ Gins `0.2` Create `mgins.py` (Gins manager) CLI tool and GREPO format for uninstalling GINS packages - command should be `python mgins.py remove [packagename]`
+ Gins `0.3` Crossplatformise new changes
+ Gins `1.0` Release Gins `1.0`

Gins `2.0` - Create `GinsCheckUpdate`
+ Gins `1.1` Make the API for Ginsupdate that only shows the current Milestone (integer) version. Coding practice change: keep Fractionals in a different folder (`latest`) while they are not integers. (how?)
+ Gins `1.2` Edit Setup and `mgins` to check for updates
+ Gins `1.3` Crossplatformise new changes
+ Gins `2.0` Release Gins `2.0`

Gins `3.0` - Create GinsDoUpdate
+ Gins `2.1` Make it so you can run `python mgins.py update-installer [installer .gins folder]` to update the installer to the current version of gins.
+ Gins `2.2`
