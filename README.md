# Instructions
experta does not support python 3.10, i suggest using pyenv to downgrade for 3.8.1 for this project
https://github.com/pyenv/pyenv

## Setup
Download the needed packages
```bash
pip install requirements.txt
```

## running
1. To run the API 
```bash
python3 -m flask --app server run
```
2. To run the interface 
```bash
xdg-open index.html
```