# ProjectShieldieDB
A sister project to [Bratah123](https://github.com/Bratah123)'s [SwordieDB project](https://github.com/Bratah123/SwordieDB).  
This project aims to document and test SwordieDB independently.

View API Docs: [here](https://kookiiestudios.github.io/ProjectShieldieDB/).

## How to use unit test
1. Clone the [SwordieDB project](https://github.com/Bratah123/SwordieDB) project, and follow the [instructions there](https://github.com/Bratah123/SwordieDB/wiki/Technical-Details) to set up the project & venv environment.
2. Use pip to install Pytest (see instructions for pip in [SwordieDB wiki](https://github.com/Bratah123/SwordieDB/wiki/Technical-Details))
3. Copy the contents of `ProjectShieldieDB/tests/` into `SwordieDB/`
4. Run **start_test.bat**

### Alternatively via PowerShell Core
1. Clone the [SwordieDB project](https://github.com/Bratah123/SwordieDB) project, and follow the [instructions there](https://github.com/Bratah123/SwordieDB/wiki/Technical-Details) to set up the project & venv environment.
2. Copy the contents of `ProjectShieldieDB/tests/` into `SwordieDB/`
3. Navigate to `SwordieDB/` in PowerShell
4. Use the command `venv/scripts/activate` to start the virtual environment
5. `pip install pytest` (first run only)
6. Use the command `py.test` to start automated unit tests.

## Progress

Automated unit tests for Character handling checks completed:  
![](https://i.imgur.com/aXl4kch.png)  

Automated unit tests for User handling checks pending...  
Automated unit tests for Inventory handling checks pending...  