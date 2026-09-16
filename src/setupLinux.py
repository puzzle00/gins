import sys, subprocess, tomllib
from pathlib import Path
from shutil import rmtree, copy

try:
    from rich.console import Console
    from rich.theme import Theme
    from rich.prompt import Confirm
except ImportError:
    print("Rich package not found. Installing it now...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich", "--break-system-packages"]) # SYSTEM
    from rich.console impoort Console
    from rich.theme import Theme

""" ALL PACKAGES SHOULD GIVE GUI OUTPUT VIA A GLOBAL CONSOLE OBJECT!!! """
custom_theme = Theme(
{"info": "bold cyan", "warning": "yellow", "danger": "bold red", "success":"bold green"}
)
cons = Console(theme=custom_theme)
def parse_gpth():
    """ GPTH to dict stuff """
    cons.log("Parsing gpth file...", style="info")
    try:
        with open("../GPTH.toml", "rb") as f:
            parsed=tomllib.load(f)
    except FileNotFoundError:
        cons.log("Can't find the GPTH.toml file. This project is incorrectly set up, please contact the author.", style="danger")
        sys.exit()
    except:
        cons.log("Error parsing GPTH.toml file.", style="danger")
        sys.exit()
    else:
        cons.log("Successfully parsed GPTH.toml file.", style="success")
        return parsed

def ginstall(package_url):
    """ Get a package from github and GINS it. Best Practice: clone the file and use `subprocess.run(["python",f"../{name_of_package}/setup.py])` to run its setup."""
    cons.log(f"Getting gins package {package_url}...",style="info")
    cons.log("Cloning package...", style="info")
    subprocess.run(["git", "clone", f"https://github.com/{package_url}", "../package"]) # SYSTEM
    cons.log("Package cloned.", style="success")
    try:
        cons.log(f"Running setup.py file for {package_url}...", style="info")
        subprocess.run([sys.executable, "../package/gins/setupLinux.py", sys.argv[1], "-I"]) # SYSTEM
    except Exception as e:
        cons.log(f"An error occurred while running the dependency's setup file that was not caught: {e}",style='danger')
        sys.exit()
    else:
        cons.log(f"Installed gins package {package_url}!", style="success")
def pipin(package):
    """ Install a package from Pip """
    cons.log(f"Installing {package} from Pip...", style="info")
    try:
        exit_code=subprocess.run([sys.executable, "-m", "pip", 'install', package, "--break-system-packages"]) # SYSTEM
        if exit_code!=0:
            cons.log(f"Error while Pip installing {package}", style="danger")
            sys.exit()
        else:
            if do_we_have_it(package):
                cons.log(f'Successfully installed {package} from Pip', style='success')
            else:
                cons.log(f'Pip installed {package}, but it cannot be found.', style='danger')
                sys.exit()
    except Exception as e:
        cons.log(f"Exception while installing {package} from pip: {e}")
        sys.exit()

def fix_dependencies(deps):
    """ Run ginstall() or pipin() as per the gins. """
    cons.log("Looking up dependencies...")
    try:
        prefixes=[]
        names=[]
        for i in deps:
            prefixes.append(i.split(":")[0])
            packages.append(i.split(":")[1])
        for i in range(len(deps)):
            if prefixes[i]=="pip":
                pipin(packages[i])
            else:
                ginstall(packages[i])
    except Exception as e:
        cons.log(f"Error while checking and installing dependencies: {e}", style="danger")
        sys.exit()
    else:
        cons.log("Successfully looked up and installed dependencies.", style="success")

def do_we_have_it(package):
    """ Do we have it? """
    package = package.lower.replace("-","_")
    try:
        __import__(package)
    except ImportError:
        return False
    return True

def stuff(files, pname) # THIS WHOLE FUNCTION IS SYSTEM
    """Stuffs the package"""
    cons.log("Installing package...", style="info")
    try:
        inst_path=Path(f"~/.gins/{pname}")
        inst_path.mkdir(parents=True, exist_ok=True)
        if do_we_have_it(pname):
            if Confirm.ask(f"{pname} already exists. Reinstall?" , console=cons):
                rmtree(inst_path)
                inst_path.mkdir(parents=True, exist_ok=True)
        for i in files:
            copy(f"../{i}",inst_path / i.split("/")[-1])
    except Exception as e:
        cons.log(f"An error ocurred when installing: {e}", style="danger")
        sys.exit()

def edit_config(files, pname):
    """Edits the .pth files"""
    # NOTE use absolute path, site.getsitepackages, ginspaths.pth
def main():
    """Run all the functions in order using the gpth"""
