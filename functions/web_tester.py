# coding=utf-8
# import socket, sys, os
# print "][ Attacking " + sys.argv[1]  + " ... ]["
# print "injecting " + sys.argv[2];
# def attack():
#     #pid = os.fork()
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((sys.argv[1], 80))
#     print ">> GET /" + sys.argv[2] + " HTTP/1.1"
#     s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")
#     s.send("Host: " + sys.argv[1]  + "\r\n\r\n");
#     s.close()


def sqlmapAttack(url, tor, sens_info, attack_level):
    #if not option:
    #   option = "-F"
    import os
    import re
    import time
    if tor == 1 & attack_level == 1:
        command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --level=3 --risk=3'
    elif tor == 1 & attack_level == 0:
        command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor'
    elif tor == 0 & attack_level == 1:
        command = 'python sqlmap.py -u "'+url+'" --batch --text-only --level=3 --risk=3'
    else:
        command = 'python sqlmap.py -u "'+url+'" --batch --text-only'

    process = os.popen(command)
    results = str(process.read())
    start = results.find('---') + 3
    end = results.find('---', start)
    if(start > 3 and end > 3):
        if(sens_info == 1):
            return u"\n Pronađena rupa u sajtu sa SQL injection-om. \n Rezultat: \n" + results[start:end] + "\n \n"
        else:
            return u"\n Pronađena rupa u sajtu sa SQL injection-om. \n \n"
    else:
        return u"\n SQL Injection napad nije mogao da nađe slabu tačku u datoj adresi. \n Pokušajte da unesete drugačiju adresu (npr. adresu koja u sebi ima više djelova)" \
               u" ili da izaberete jači napad. \n" \
               u"Tipovi adresa koje mogu da prođu ovaj test su: https://nešto.com/nešto-drugo ili https://nešto.com?id=1234 "


def xsserAttack(url, tor, sens_info, attack_level):

    import os
    import re
    if tor == 1 & attack_level == 1:
        command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom '
    elif tor == 1 & attack_level == 0:
        command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 '
    elif tor == 0 & attack_level == 1:
        command = './xsser -u "' + url + '" -s --no-head --auto --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom '
    else:
        command = './xsser -u "' + url + '" -s --no-head --auto '
    # command = './xsser -u "' + url + '" -c 500 --Cw 1 --Cl -s --no-head --alive 3 --reverse-check --follow-redirects --follow-limit 10 --threads 5 --timeout 5 --auto --Coo --Xsa --Xsr --Dom --Dcp --Ind '
    import time
    process = os.popen(command)
    results = str(process.read())
    if sens_info == 1:
        start = results.find('List of possible XSS injections:') + 3
        end = results.find('---', start)
        if (start > 3):
            return "\nLis" + results[start:-1] + "\n \n"
        else:
            start = results.find('Statistic:') + 3
            end = results.find('---', start)
            if (start > 3):
                return "\nS" + results[start:-1] + "\n \n"
            else:
                return "\n\nXSS napad nije uspio. \n"

    else:
        start = results.find('Statistic:') + 3
        end = results.find('---', start)
        if (start > 3):
            return "\nS" + results[start:-1] + "\n \n"
        else:
            return "\n\nXSS napad nije uspio. \n"

