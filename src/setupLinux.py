import sys, subprocess, tomllib, importlib.util

try:
    from rich.console impoort Console
    from rich.theme import Theme
except ImportError:
    print("Rich package not found. Installing it now...")
    subprocess.run([sys.executable, "-m", "install", "rich", "--break-system-packages"])
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
    ...
def pipin(package):
    """ Install a package from Pip """
    cons.log(f"Installing {package} from Pip...", style="info")
    try:
        exit_code=subprocess.run([sys.executable, "-m", "pip", 'install', package, "--break-system-packages"])
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
            packages.append(i.split(":")[0])
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
def stuff_and_edit_config()
    """Stuffs and edits the config file for the current thing."""
def clean_up():
    """ Cleans up the temporary curr_install folder. Should just delete the entire folder + remake it, poss. issue (!)"""
def main():
    """Run all the functions in order using the gpth"""
