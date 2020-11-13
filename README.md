# kiruna_barrel_flyover
This repo looks at the BARREL flyover the Kiruna all sky imager on 30 August 2016

## Installation
Run these shell commands to install the dependencies into a virtual 
environment and configure the BARREL and Kiruna ASI data paths:

```
# cd into the top project directory
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 -m kiruna_barrel_flyover init # and answer the promps.
```

Only tested with Python 3.8.