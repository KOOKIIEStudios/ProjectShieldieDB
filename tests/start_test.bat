:: This script allows the user to launch the tests without needing use command line
@ECHO off
echo "This script will start the ProjectShieldieDB test sequence."
echo "Starting up virtual environment..."
call venv\scripts\activate.bat
echo "Attempting to test the capabilities of SowrdieDB..."
py.test
echo "Test concluded."
pause