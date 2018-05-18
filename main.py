# coding=utf-8
#from functions.web_scanner import print_u_rezultat
import sys
from numpy.core.defchararray import splitlines
import os

command = "pip install whois"
process = os.popen(command)
results = str(process.read())
command = "pip install tld"
process = os.popen(command)
results = str(process.read())

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
        domain_name_res = "Domen: "+domain_name
        rezultat.insert(INSERT, domain_name_res)
        rezultat.see(END)

        # IP Adresa
        ip = web_scanner.get_ip_address(domain_name)
        rezultat.insert(INSERT, "\n \n " + ip + u" \n Molimo sačekajte... \n")
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
    is_checkedSens = sens_info.get()
    is_checkedLevel = attack_level.get()
    global br_post, br_cookie

    # Brisemo cookie i post ako niko nije kliknuo
    if br_post == 0:
        delete_txt_post(self=1)
    if br_cookie == 0:
        delete_txt_cookie(self=1)

    # Uzima se post i cookie
    post = post_lbl.get()
    cookie = cookie_lbl.get()

    # resetujemo br za post i cookie za sledeci put
    br_post = 0
    br_cookie = 0

    if sk != "":
        # sqlmap
        rezultat.insert(INSERT, u"\n SQL Injection napad u toku... \nOvo može da potraje nekoliko minuta...")
        rezultat.see(END)
        domain_name = web_tester.sqlmapAttack(sk, is_checkedTor, is_checkedSens, is_checkedLevel, post, cookie)
        rezultat.insert(INSERT, domain_name)
        rezultat.see(END)

        # xsser
        rezultat.insert(INSERT, u"\n\nXSS Injection napad u toku... \nOvo može da potraje nekoliko minuta. Sačekajte.....")
        rezultat.see(END)
        domain_name = web_tester.xsserAttack(sk, is_checkedTor, is_checkedSens, is_checkedLevel, post, cookie)
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

def toggle(self):
    checkbox = post_method.get()
    if not checkbox:
        post_txt.lift()
        post_lbl.lift()
        cookie_txt.lift()
        cookie_lbl.lift()
    else:
        post_txt.lower()
        post_lbl.lower()
        cookie_txt.lower()
        cookie_lbl.lower()

br_cookie = 0
br_post = 0

def delete_txt_cookie(self):
    global  br_cookie
    cookie_lbl.delete(0, END)
    br_cookie = 1

def delete_txt_post(self):
    global  br_post
    post_lbl.delete(0, END)
    br_post = 1

root = Tk()
root.resizable(0,0)
# Naslov
root.winfo_toplevel().title("Soteria")


# Pozadina
image1 = PhotoImage(file="1.gif")
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (w, h))

panel1 = Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')


# Labela za unos url-a
skenirano = StringVar()
url = Label(root, text="Unesite adresu za testiranje: ")
url_unos = Entry(root, textvariable=skenirano)
url.place(relx=.1, rely=.2, anchor="n")
url_unos.place(relx=.5, rely=.2, anchor="n", width=550)
url_unos.focus_set()

# Labela za unos POST-a
post = StringVar()
post_txt = Label(root, text="Unesite POST parametre: ")
post_txt.place(relx=.1, rely=.4, anchor="n")
post_lbl = Entry(root, textvariable=post_txt)
post_lbl.insert(0, "username=admin&password=admin123")
post_lbl.bind("<Button-1>", delete_txt_post)
post_lbl.place(relx=.33, rely=.4, anchor="n", width=250)

cookie = StringVar()
cookie_txt = Label(root, text="Unesite Cookie: ")
cookie_txt.place(relx=.55, rely=.4, anchor="n")
cookie_lbl = Entry(root, textvariable=cookie_txt)
cookie_lbl.insert(0, "PHPSESSID=75500c66d6ceb01107561afd24db0596")
cookie_lbl.bind("<Button-1>", delete_txt_cookie)
cookie_lbl.place(relx=.75, rely=.4, anchor="n", width=250)

# Sakrijemo ova polja...
post_txt.lower()
post_lbl.lower()
cookie_txt.lower()
cookie_lbl.lower()
# post_lbl.visible = False



# Dugme za pocetak napada
pocni = Button(root, text=u"Počni", bg="#2de810")
pocni.place(relx=.28, rely=.3, anchor="n", width=150)
pocni.bind("<Button-1>", attackWebPage)


# Textarea za ispis rezultata
rezultat = Text(root)
rezultat.place(relx=.5, rely=.50, anchor="n", width=900, height=250)

# Dugme za skeniranje sajta
skeniraj = Button(root, text="Skeniraj", bg="#2131fa")
skeniraj.place(relx=.5, rely=.3, anchor="n", width=150)
skeniraj.bind("<Button-1>", threadedInTextBox)

# Opcije
    # Tor
tor = IntVar()
Checkbutton(root, text="Tor", onvalue=1, offvalue=0, variable=tor).place(relx=.22, rely=.46, anchor="n")

    # Osjetljive informacije
sens_info = IntVar()
Checkbutton(root, text=u"Prikaži osjetljive informacije", onvalue=1, offvalue=0, variable=sens_info).place(relx=.4, rely=.46, anchor="n")


    # Jacina napada
attack_level = IntVar()
Checkbutton(root, text=u"Jači napad", onvalue=1, offvalue=0, variable=attack_level).place(relx=.6, rely=.46, anchor="n")

    # POST parametri
post_method = IntVar()
checkbutton = Checkbutton(root, text=u"POST i Cookie", onvalue=1, offvalue=0, variable=post_method)
checkbutton.place(relx=.75, rely=.46, anchor="n")
checkbutton.bind("<Button-1>", toggle)


root.mainloop()