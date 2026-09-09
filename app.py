import sys
import os

# Add local directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quantum_ai.web_app import launch_web_app
from quantum_ai.gui import launch_gui
from quantum_ai.cli import launch_cli


def main():
    if "--cli" in sys.argv or "-c" in sys.argv:
        launch_cli()
    elif "--gui" in sys.argv:
        launch_gui()
    else:
        # Default mode: Native Standalone Web Desktop App (just like a webpage, no terminal required)
        launch_web_app()


if __name__ == "__main__":
    main()
