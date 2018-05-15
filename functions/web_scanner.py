import os
from urllib2 import Request, OpenerDirector
import io
import whois

# note - you would need to pip install this (or add it with GUI in pycharm
# (file->settings->project->project interperter->install (a green "+" sign)
from tld import get_tld
#class web_scanner:


def create_dir(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def get_domain_name(url):
    from tld import get_tld
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://'+url
    domain_name = get_tld(url)
    return domain_name

# this is the linux version
def get_ip_address(domain):
    import socket
    results = socket.gethostbyname(domain)
    return "\n \n IP adresa: " + results + "\n \n"

# this is the windows version
# def get_ip_address(url):
#     command = "nslookup " + url
#     process = os.popen(command)
#     results = str(process.read())
#     # there's a problem - on some websites the ip will be on the 5th line (index 4) and some it will be on different
#     # so I just take everything
#     # marker = results.splitlines()[4]
#     return results

# this will work for linux automatically.
# Windows users need to download it from here: https://nmap.org/download.html
def get_nmap(option, domain):
    #if not option:
    #   option = "-F"
    import os
    command = "nmap --host-timeout 10 " + domain
    process = os.popen(command)
    results = str(process.read())
    return "\n \n NMAP: \n \n " + results + "\n \n"

def get_robots_txt(url):
    # if url.endswith('/'):
    #     path = url
    # else:
    #     path = url + '/'

    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    url_spitted = url.split("/")
    path = url_spitted[0] + "//" + url_spitted[2] + "/"
    import urllib2
    try:
        req = urllib2.urlopen(path + 'robots.txt', data=None)
        data = req
        return "Robots.txt: \n \n " + data.read() + "\n \n"
    except urllib2.HTTPError, e:
        return 'Nije moguce naci robots.txt - HTTPError = ' + str(e.code) + '\n\n'


# notice that the command in this function will only work on linux, while in windows you have to download whois
# https://technet.microsoft.com/en-us/sysinternals/whois.aspx
# You might have to add the directory path of where you unpack whois to the system variables
# if so, check:
# http://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them
def get_whois(domain):
    import os
    command = "whois " + domain
    process = os.popen(command)
    results = process.read()
    return "Detalji korisnika sajta (WhoIs): \n \n " + results + "\n \n"



# def gather_info(url):
#     domain_name = get_domain_name(url)
#     ip_address = get_ip_address(domain_name)
#     nmap = get_nmap(domain_name)  # ('-F', ip_address) - this is the linux version
#     robots_txt = get_robots_txt(url)
#     whois = get_whois(domain_name)
#     create_report(url, domain_name, ip_address, nmap, robots_txt, whois)

def create_report(sum_scanner):
    ROOT_DIR = 'Skenirani sajtovi'
    project_dir = ROOT_DIR
    create_dir(project_dir)
    write_file(project_dir + '/report.txt', sum_scanner)
    # write_file(project_dir + '/domain_name.txt', domain_name)
    # write_file(project_dir + '/ipaddress.txt', ip_address)
    # write_file(project_dir + '/nmap.txt', nmap)
    # write_file(project_dir + '/robots.txt', robots_txt)
    # write_file(project_dir + '/whois.txt', whois)

def print_u_rezultat(url):
    import tkMessageBox
    if url:
        #tkMessageBox.showwarning('alert title', 'Bad things happened!')
        domain_name = get_domain_name(url)
        nmap = get_nmap("-F", domain_name)
        robots_txt = get_robots_txt(url)
        whois = get_whois(domain_name)
        sum_scanner = domain_name + nmap + robots_txt + whois
        create_report(sum_scanner)
        ROOT_DIR = 'Skenirani sajtovi'
        create_dir(ROOT_DIR)
        return sum_scanner
#gather_info('thenewboston', 'https://www.thenewboston.com/')
#print_u_rezultat("https://www.github.com/")
