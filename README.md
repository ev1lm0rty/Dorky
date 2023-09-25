# About
Dorky takes in a list containing google dorks and then extracts links from google search results.


# Requirements
* Google API key.
* Google Custom Search Engine id.
* File containing a list of dorks. ( I have included one. Used for finding responsible disclosure programs)

# Installation
1. Install pip
2. `pip install -r requirements.txt`

# Usage
```
usage: script.py [-h] -d DORK -a API -c CSI [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -d DORK, --dork DORK  List of dorks
  -a API, --api API     Google API key
  -c CSI, --csi CSI     Custom Search Id
  -o OUTPUT, --output OUTPUT Output file
                       
```

# Help
* [Follow this to get your api key](https://www.youtube.com/watch?v=IBhdLRheKyM)

# Todo
- [ ] Remove the 100 searches per day search limit.
- [ ] Include more than 10 results per search.