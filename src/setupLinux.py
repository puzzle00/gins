import sys, subproccess, tomllib, importlib.util
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
        cons.log("Can't find the GPTH.toml file. This project is incorrectly set up. Please contact the author.", style="danger")
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
    ...
def fix_dependencies(gpth):
    """ Run ginstall() or pipin() as per the gins. """
    ...
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
    """ For now it is a donothing. Should open the pa"""
