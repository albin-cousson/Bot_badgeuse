from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
from threading import Thread
import time

class Initialisation(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        while True:
            #connexion
            driver = webdriver.Chrome("/Users/albin/bin/chromedriver")
            driver.get("https://badgeuse.uha4point0.fr/")
            pseudo = driver.find_element_by_name("userMail")
            passwd = driver.find_element_by_name("password")
            pseudo.clear()
            passwd.clear()
            pseudo.send_keys("albincousson@icloud.com")
            passwd.send_keys("4b5fbehibxwtp2y6gp4kor")
            passwd.send_keys(Keys.RETURN)

            #ponitage 
            time.sleep(5)
            driver.find_element_by_tag_name("app-badger").click()
            time.sleep(5)
            driver.find_element_by_class_name("swal2-confirm").click()

            #deconnexion
            time.sleep(5)
            driver.close()

            #time sleep de 9h à 17h
            time.sleep(5)

            #connexion
            driver = webdriver.Chrome("/Users/albin/bin/chromedriver")
            driver.get("https://badgeuse.uha4point0.fr/")
            pseudo = driver.find_element_by_name("userMail")
            passwd = driver.find_element_by_name("password")
            pseudo.clear()
            passwd.clear()
            pseudo.send_keys("albincousson@icloud.com")
            passwd.send_keys("4b5fbehibxwtp2y6gp4kor")
            passwd.send_keys(Keys.RETURN)

            #déponitage 
            time.sleep(5)
            driver.find_element_by_tag_name("app-badger").click()
            time.sleep(5)
            textarea = driver.find_element_by_class_name("swal2-textarea")
            textarea.send_keys("super journée, très productive ! :)")
            time.sleep(5)
            driver.find_element_by_class_name("swal2-confirm").click()

            #deconnexion
            time.sleep(5)
            driver.close()

            #time sleep de 17h à 9h
            time.sleep(5)

class Interface(Frame):
    def __init__(self, fenetre, *args, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, *args, **kwargs)
        self.pack()
        self.titre = Label(fenetre, text="Bienvenue user, ici tu pourra automatiser tes tâches")
        self.titre.config(font=("Helvetica", 20))
        self.titre.pack()
        self.bouton = Button(fenetre, text="Start", command=self.start)
        self.bouton.config(relief=GROOVE)
        self.bouton.pack()
    def start(self):
        initialisation = Initialisation()
        initialisation.start()

fenetre = Tk()
fenetre.title("Bot badgeuse")

interface = Interface(fenetre)
interface.mainloop()
