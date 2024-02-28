# enter venv

# Usage:
# . ev.sh

# Description:
# This script is used to enter the virtual environment in the current directory, adding the bin directory to the PATH.

function ev() {
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        echo "No virtual environment found in the current directory."
    fi
}

ev