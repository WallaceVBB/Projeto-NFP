#Esse vai ser o preenchedor das informações no site da NFP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
import time
import urllib


def back ():
    chrome_service = ChromeService('chromedriver')
    chrome_service.creationflags = CREATE_NO_WINDOW

    navegador = webdriver.Chrome(service=chrome_service)

    #Vamos fazer o login na NFP (ainda precisa substituir o By.ID por um da NFP)
    def logando ():
        navegador.get("https://www.nfp.fazenda.sp.gov.br/login.aspx?ReturnUrl=%2fInicio.aspx")
        while len(navegador.find_elements (By.ID,"side"))< 1:
            time.sleep(1)
        iniciando ()

    #def iniciando ():