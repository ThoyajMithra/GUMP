import sys

from gump.ui.cli import GumpUi

def main():
    if len(sys.argv)>1 and sys.argv[1] in ["--version","-v"]:
        from importlib.metadata import version
        print(f"GUMP {version('gump')}")
        return
    entry=GumpUi()
    entry.start_gump()

if __name__=="__main__":
    main()