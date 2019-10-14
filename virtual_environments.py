
"""
Powershell

First time setup
1. Right click, run powershell as admin
2. set-executionpolicy remoteassigned
3. To undo this someday, you'll have to google the right command

Each time
1. Goto the folder in which you want the environment directory to be created
1. py -m venv nameofmyvirtualenvironmentgoeshere
2. Activate
    Windows:  nameofmyvirtualenvironmentgoeshere/Scripts/activate
    Mac/Lin:  source nameofvirtenv/bin/activate
3. To verify, terminal should have the virtual env name on the left
4. The command prompt should stay above the directory for the virt env, e.g. stay in PythonFundamentals
5. "deactivate" to shut down the virtual environment

Good practice is to open a new virt env each time, to start from a clean slate.


To install a new package:
1. Vocab: PIP = package installation tool
2. 

Check version
1. e.g.       pytest --version

"""

"""
        UPGRADING PIP

Successfully installed certifi-2019.9.11 chardet-3.0.4 idna-2.8 requests-2.22.0 urllib3-1.25.6
You are using pip version 19.0.3, however version 19.2.3 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
"""

#HW why do people get colds in the fall?

import requests

response = requests.get("https://api.spacexdata.com/v3/rockets")
data = response.json()
print(type(data))

for entry in data:
    print(entry.keys(), "\n")
    
for entry in data:
    print(entry["rocket_name"])


print()

#HW iotlab indy
#HW BLE bluetooth low energy
#HW or #? define endpoint

