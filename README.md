# soteria

Soteria is a mini framework for testing website's security, including sql injection and xss testing. It also includes website scanning like ports, ip address and whois (information about registration)
# Installation 

### Install python:
- `sudo apt-get install python`
### Install pip
- `sudo apt-get install python-pip python-dev build-essential`
### Install whois and nmap
- `sudo apt-get install whois`
- `sudo apt-get install nmap`
### Install pip packages
- `pip install numpy`
- `pip install Pillow`
- `pip install nmap`
- `pip install whois`
- `pip install tld`
- `pip install BeautifulSoup`
- `pip install pycurl`

If you can't install pycurl do these steps:
- `apt-cache depends python-pycurl`
- `sudo apt-get install libcurl4-gnutls-dev`

check if can now install _pycurl_
- `pip install pycurl`

If it is not working and throws error "Cannot create wheel" or similar go further with:
- `apt-cache search gnutl | grep dev`

Try:
- `sudo apt-get install libgnutls-dev`

and install _pycurl_
- `pip install pycurl`
