import sys, subprocess, tomllib, os, site
from pathlib import Path
from shutil import rmtree, copy
 
try:
    from rich.console import Console
    from rich.theme import Theme
    from rich.prompt import Confirm
except ImportError:
    print("Rich package not found. Installing it now...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich", "--break-system-packages"]) # SYSTEM
    from rich.console import Console
    from rich.theme import Theme

""" ALL PACKAGES SHOULD GIVE GUI OUTPUT VIA A GLOBAL CONSOLE OBJECT!!! """
custom_theme = Theme(
{"info": "bold cyan", "warning": "yellow", "danger": "bold red", "success":"bold green"}
)
cons = Console(theme=custom_theme)
internal=False
def printifnoti(*args,**kwargs):
    if not internal:
        cons.log(*args,**kwargs)
def parse_gpth():
    """ GPTH to dict stuff """
    printifnoti("Parsing gpth file...", style="info")
    try:
        with open("../GPTH.toml", "rb") as f:
            parsed=tomllib.load(f)
    except FileNotFoundError:
        printifnoti("Can't find the GPTH.toml file. This project is incorrectly set up, please contact the author.", style="danger")
        sys.exit(1)
    except:
        printifnoti("Error parsing GPTH.toml file.", style="danger")
        sys.exit(1)
    else:
        printifnoti("Successfully parsed GPTH.toml file.", style="success")
        return parsed

def ginstall(package_url):
    """ Get a package from github and GINS it. Best Practice: clone the file and use `subprocess.run(["python",f"../{name_of_package}/setup.py])` to run its setup."""
    printifnoti(f"Getting gins package {package_url}...",style="info")
    printifnoti("Cloning package...", style="info")
    subprocess.run(["git", "clone", f"https://github.com/{package_url}", "../package"]) # SYSTEM
    printifnoti("Package cloned.", style="success")
    try:
        printifnoti(f"Running setup.py file for {package_url}...", style="info")
        returncode=subprocess.run([sys.executable, "../package/gins/setupLinux.py", "-I"]).returncode# SYSTEM
        if returncode!=0:
            printifnoti(f"Error in setup.py file for {package_url}", style="danger")
            sys.exit(1)
    except Exception as e:
        printifnoti(f"An error occurred while running the dependency's setup file that was not caught: {e}",style='danger')
        sys.exit(1)
    else:
        printifnoti(f"Installed gins package {package_url}!", style="success")

def pipin(package):
    """ Install a package from Pip """
    printifnoti(f"Installing {package} from Pip...", style="info")
    try:
        exit_code=subprocess.run([sys.executable, "-m", "pip", 'install', package, "--break-system-packages"]).returncode # SYSTEM
        if exit_code!=0:
            printifnoti(f"Error while Pip installing {package}", style="danger")
            sys.exit(1)
        else:
            if do_we_have_it(package):
                printifnoti(f'Successfully installed {package} from Pip', style='success')
            else:
                printifnoti(f'Pip installed {package}, but it cannot be found.', style='danger')
                sys.exit(1)
    except Exception as e:
        printifnoti(f"Exception while installing {package} from pip: {e}")
        sys.exit(1)

def fix_dependencies(deps):
    """ Run ginstall() or pipin() as per the gins. """
    printifnoti("Looking up dependencies...", style="info")
    try:
        prefixes=[]
        names=[]
        for i in deps:
            prefixes.append(i.split(":")[0])
            names.append(i.split(":")[1])
        for i in range(len(deps)):
            if prefixes[i]=="pip":
                pipin(names[i])
            else:
                ginstall(names[i])
    except Exception as e:
        printifnoti(f"Error while checking and installing dependencies: {e}", style="danger")
        sys.exit(1)
    else:
        printifnoti("Successfully looked up and installed dependencies.", style="success")

def do_we_have_it(package):
    """ Do we have it? """
    package = package.lower().replace("-","_")
    try:
        __import__(package)
    except ImportError:
        return False
    return True

def stuff(files, pname): # THIS WHOLE FUNCTION IS SYSTEM
    """Stuffs the package"""
    printifnoti("Installing package...", style="info")
    try:
        inst_path=Path.home()/f".gins/{pname}"
        inst_path.mkdir(parents=True, exist_ok=True)
        if do_we_have_it(pname):
            if Confirm.ask(f"{pname} already exists. Reinstall?" , console=cons):
                rmtree(inst_path)
                inst_path.mkdir(parents=True, exist_ok=True)
        for i in files:
            copy(f"../{i}",inst_path / i.split("/")[-1])
    except Exception as e:
        printifnoti(f"An error ocurred when installing: {e}", style="danger")
        sys.exit(1)

def edit_config(files, pname):
    """Edits the .pth files"""
    spac=site.getusersitepackages()
    pathpath=os.path.join(spac,"ginspaths.pth")
    ginspath=os.path.abspath(Path.home()/".gins/")
    mode='a' if os.path.exists(pathpath) else 'w'
    with open(pathpath, mode, encoding="utf-8") as f:
        f.write(ginspath+"\n")
    
def main():
    global internal
    """Run all the functions in order using the gpth"""
    if sys.argv[1]=="-I":
        internal=True
    try:
        parsed=parse_gpth()
        for k in parsed.keys():
            if k=="gins":
                # We found it.
                printifnoti(f'Project {parsed["gins"]["projectname"]} beginning execution...', style='info')
                fix_dependencies(parsed["gins"]["dependencies"])
                stuff(parsed["gins"]["filenames"],parsed['gins']['projectname'])
                edit_config(parsed["gins"]["filenames"],parsed['gins']['projectname'])
                printifnoti(f"Succesfully installed {parsed['gins']['projectname']}", style="success")
                sys.exit()
            else:
                pass
    except Exception as e:
        printifnoti(f"Uncaught error during setup execution: {e}", style="danger")
        sys.exit(1)
    # Because there is a sys.exit in the if statement, the code won't get here unless there is no gpth.
    printifnoti("Can't find the [gins] header in the gpth file. This project is incorrectly set up, please contact the author.", style="danger")
    sys.exit(1)

# ifname

if __name__ == "__main__":
    main()
