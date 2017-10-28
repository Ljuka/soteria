#from functions.web_scanner import print_u_rezultat
import sys
from numpy.core.defchararray import splitlines

sys.path.insert(0, 'functions/')
import web_scanner
import web_tester
import sys
import time
from PIL import ImageTk
import PIL.Image
import threading

try:
    # for Python2
    from Tkinter import *  ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    from tkinter import *  ## notice lowercase 't' in tkinter here

# class FullScreenApp(object):
    # def __init__(self, master, **kwargs):
    #     self.master=master
    #     pad=3
    #     self._geom='200x200+0+0'
    #     master.geometry("{0}x{1}+0+0".format(
    #         master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
    #     master.bind('<Escape>',self.toggle_geom)
    # def toggle_geom(self,event):
    #     geom=self.master.winfo_geometry()
    #     print(geom,self._geom)
    #     self.master.geometry(self._geom)
    #     self._geom=geom

# Za skeniranje sajta
def writeInTextBox():
    sk = skenirano.get()
    if sk != "":
        # Domen print
        domain_name = web_scanner.get_domain_name(sk)
        rezultat.insert(INSERT, domain_name)
        rezultat.see(END)

        # IP Adresa
        ip = web_scanner.get_ip_address(domain_name)
        rezultat.insert(INSERT, "\n \n " + ip + " \n Please wait... \n")
        rezultat.see(END)

        # NMAP print
        nmap = web_scanner.get_nmap("-F", domain_name)
        nmap_splited = nmap.split("\n")
        for line in nmap_splited:
            rezultat.insert(INSERT, line)
            rezultat.see(END)
            time.sleep(0.1)
            rezultat.insert(INSERT, "\n")
            rezultat.see(END)
            time.sleep(0.1)

        # ROBOTS print
        robots_txt = web_scanner.get_robots_txt(sk)
        robots_spitted = robots_txt.split("\n")
        for line in robots_spitted:
            rezultat.insert(INSERT, line)
            rezultat.see(END)
            time.sleep(0.1)
            rezultat.insert(INSERT, "\n")
            rezultat.see(END)
            time.sleep(0.1)

        # WHOIS print
        whois = web_scanner.get_whois(domain_name)
        whois_splited = whois.split("\n")
        for line in whois_splited:
            rezultat.insert(INSERT, line)
            rezultat.see(END)
            time.sleep(0.1)
            rezultat.insert(INSERT, "\n")
            rezultat.see(END)
            time.sleep(0.1)

# Za napad sajta
def fullAttacks():
    sk = skenirano.get()
    is_checkedTor = tor.get()
    if sk != "":
        # sqlmap
        rezultat.insert(INSERT, "\n SQL Injection napad u toku... \nOvo moze da potraje nekoliko minuta...")
        rezultat.see(END)
        domain_name = web_tester.sqlmapAttack(sk, is_checkedTor)
        rezultat.insert(INSERT, domain_name)
        rezultat.see(END)

        # xsser
        rezultat.insert(INSERT, "\n\nXSS Injection napad u toku... \nOvo moze da potraje nekoliko minuta. Sacekajte.....")
        rezultat.see(END)
        domain_name = web_tester.xsserAttack(sk, is_checkedTor)
        rezultat.insert(INSERT, domain_name)
        rezultat.see(END)


def threadedInTextBox(self):
    t1 = threading.Thread(target=writeInTextBox)
    t1.start()

# def ddosNapad():
#     web_tester.ddosAttack("http://www.portoweb.com.br/")

def attackWebPage(self):
    t2 = threading.Thread(target=fullAttacks)
    t2.start()


root = Tk()
root.resizable(0,0)


image1 = PhotoImage(file="1.gif")
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (w, h))

panel1 = Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')


skenirano = StringVar()
url = Label(root, text="Unesite adresu za testiranje: ")
url_unos = Entry(root, textvariable=skenirano)
url.place(relx=.1, rely=.2, anchor="n")
url_unos.place(relx=.5, rely=.2, anchor="n", width=550)
url_unos.focus_set()

pocni = Button(root, text="Pocni", bg="#2de810")
pocni.place(relx=.28, rely=.3, anchor="n", width=150)
pocni.bind("<Button-1>", attackWebPage)


rezultat = Text(root)
rezultat.place(relx=.5, rely=.4, anchor="n", width=900, height=250)
skeniraj = Button(root, text="Skeniraj", bg="#2131fa")
skeniraj.place(relx=.5, rely=.3, anchor="n", width=150)
skeniraj.bind("<Button-1>", threadedInTextBox)

tor = IntVar()
Checkbutton(root, text="Tor", onvalue=1, offvalue=0, variable=tor).place(relx=.823, rely=.2, anchor="n")

root.mainloop()