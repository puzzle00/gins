import sys, subproccess, tomllib, importlib.util, rich

""" ALL PACKAGES SHOULD GIVE GUI OUTPUT VIA A GLOBAL CONSOLE OBJECT!!! """

def parse_gpth():
    """ GPTH to dict stuff """
    ...
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
