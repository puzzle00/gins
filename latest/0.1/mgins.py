import platform, subprocess, sys
try:
    import click
except ImportError:
    match platform.system():
        case "Windows":
            print("Installing click for Windows...")
            subprocess.run([sys.executable,"-m","install","click"])
        case "Darwin":
            print("Installing click for Mac...")
            subprocess.run([sys.executable,"-m","install","click","--break-system-packages"])
        case "Linux":
            print("Installing click for Linux...")
            subprocess.run([sys.executable,"-m","install","click","--break-system-packages"])
        case _:
            print("Can't automatically install click. Please globally PIP install click and rerun.")
            sys.exit()

    import click

@click.group()
def mgins():
    pass

@mgins.command()
@click.argument('packagename')
def remove(packageid):
    pass
