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


def sqlmapAttack(url):
    #if not option:
    #   option = "-F"
    import os
    import re
    command = 'python sqlmap.py -u "'+url+'" --batch --text-only'
    process = os.popen(command)
    results = str(process.read())
    start = results.find('---') + 3
    end = results.find('---', start)
    if(start > 3 and end > 3):
        return "\n Pronadjena rupa u sajtu sa SQL injection-om. \n Rezultat: \n" + results[start:end] + "\n \n"
    else:
        return "\n SQLMAP nije mogao da nadje slabu tacku u datoj adresi. \n Pokusajte da unesete drugaciju adresu. " \
               "Npr. adresu koja u sebi ima vise djelova. \n" \
               "Tipovi adresa koje mogu da prodju ovaj test su: https://nesto.com/nesto-drugo ili https://nesto.com?id=1234 "