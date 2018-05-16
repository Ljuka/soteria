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


def sqlmapAttack(url, tor, sens_info, attack_level, post_method, cookie):
    #if not option:
    #   option = "-F"
    import os
    import re
    import time
    if post_method == "" and cookie == "":
        if tor == 1 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --level=3 --risk=5'
        elif tor == 1 and attack_level == 0:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor'
        elif tor == 0 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --level=3 --risk=5 --random-agent'
        else:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --random-agent'
    elif post_method != "" and cookie == "":
        if tor == 1 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --level=3 --risk=5 --method POST --data="'+post_method+'"'
        elif tor == 1 and attack_level == 0:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --method POST --data="'+post_method+'"'
        elif tor == 0 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --level=3 --risk=5 --random-agent --method POST --data="'+post_method+'"'
        else:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --random-agent --method POST --data="'+post_method+'"'
    elif post_method == "" and cookie != "":
        if tor == 1 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --level=3 --risk=5 --cookie="'+cookie+'"'
        elif tor == 1 and attack_level == 0:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --cookie="'+cookie+'"'
        elif tor == 0 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --level=3 --risk=5 --random-agent --cookie="'+cookie+'"'
        else:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --random-agent --cookie="'+cookie+'"'
    elif post_method != "" and cookie != "":
        if tor == 1 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --level=3 --risk=5 --method POST --data="'+post_method+'" --cookie="'+cookie+'"'
        elif tor == 1 and attack_level == 0:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --tor --method POST --data="'+post_method+'" --cookie="'+cookie+'"'
        elif tor == 0 and attack_level == 1:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --level=3 --risk=5 --random-agent --method POST --data="'+post_method+'" --cookie="'+cookie+'"'
        else:
            command = 'python sqlmap.py -u "'+url+'" --batch --text-only --random-agent --method POST --data="'+post_method+'" --cookie="'+cookie+'"'

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
        start = results.find('can\'t establish connection with the Tor') + 3
        end = results.find('[*] shutting down', start)
        if(start > 3 and end > 3):
            return u"\nSQL Injection nije uspio. \n\n Morate uključiti Tor mrežu ako hoćete da idete preko Tor mreže!. "
        else:
            return u"\n SQL Injection napad nije mogao da nađe slabu tačku u datoj adresi. \n Pokušajte da unesete drugačiju adresu (npr. adresu koja u sebi ima više djelova)" \
                u" ili da izaberete jači napad. \n" \
                u"Tipovi adresa koje mogu da prođu ovaj test su: https://nešto.com/nešto-drugo ili https://nešto.com?id=1234 "


def xsserAttack(url, tor, sens_info, attack_level, post_method, cookie):

    import os
    import re
    if post_method == "" and cookie == "":
        if tor == 1 and attack_level == 1:
            command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom '
        elif tor == 1 and attack_level == 0:
            command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 '
        elif tor == 0 and attack_level == 1:
            command = './xsser -u "' + url + '" -s --no-head --auto --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom '
        else:
            command = './xsser -u "' + url + '" -s --no-head --auto '
    elif post_method != "" and cookie == "":
        if tor == 1 and attack_level == 1:
            command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto'
        elif tor == 1 and attack_level == 0:
            command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 -p "'+post_method+'" --auto'
        elif tor == 0 and attack_level == 1:
            command = './xsser -u "' + url + '" -s --no-head --auto --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto'
        else:
            command = './xsser -u "' + url + '" -s --no-head --auto -p "'+post_method+'" --auto'
    elif post_method == "" and cookie != "":
            if tor == 1 and attack_level == 1:
                command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            elif tor == 1 and attack_level == 0:
                command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            elif tor == 0 and attack_level == 1:
                command = './xsser -u "' + url + '" -s --no-head --auto --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            else:
                command = './xsser -u "' + url + '" -s --no-head --auto -p "'+post_method+'" --auto --cookie="'+cookie+'"'
    elif post_method != "" and cookie != "":
            if tor == 1 and attack_level == 1:
                command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            elif tor == 1 and attack_level == 0:
                command = './xsser -u "' + url + '" -s --no-head --auto --proxy http://127.0.0.1:8118 -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            elif tor == 0 and attack_level == 1:
                command = './xsser -u "' + url + '" -s --no-head --auto --Cw=5 --reverse-check --Coo --Xsa --Xsr --Dcp --Dom -p "'+post_method+'" --auto --cookie="'+cookie+'"'
            else:
                command = './xsser -u "' + url + '" -s --no-head --auto -p "'+post_method+'" --auto --cookie="'+cookie+'"'

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

