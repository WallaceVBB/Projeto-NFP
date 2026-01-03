##### Bibliotecas
#Essa vai ser a janela do app
import customtkinter as ctk
import os
import leitor
import preenchedor

#Esse vai ser o preenchedor das informações no site da NFP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
import time
import urllib

##### Código
def back ():
    chrome_service = ChromeService('chromedriver')
    chrome_service.creationflags = CREATE_NO_WINDOW

    navegador = webdriver.Chrome(service=chrome_service)

    navegador.get("http://bit.ly/login-nfp")
    while len(navegador.find_elements (By.ID,"pnlAcessoRestrito"))< 1:
        time.sleep(1)
    time.sleep(3)
    navegador.execute_script('window.scrollBy(0, 502)')
    time.sleep(1)
    navegador.find_element(By.ID, "btnContinuar").click()
    navegador.get("https://www.nfp.fazenda.sp.gov.br/EntidadesFilantropicas/CadastroNotaEntidadeAviso.aspx")
    time.sleep(2)
    navegador.find_element(By.ID, "ctl00_ConteudoPagina_btnOk").click()
    time.sleep(10)


def add_fotos():
    os.startfile("QRcodes")

def add_fotos():
    os.startfile("QRcodes")

def chaves ():
    excel = os.system("chaves de acesso.xlsx")

def erros ():
    excel = os.system("erros.xlsx")



#janela inicial
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela._set_appearance_mode ("light")
janela.geometry("200x280")
janela.resizable(width=False, height=False)
janela.title("Leitor de QR para NFP")

#Título
titulo = ctk.CTkLabel(janela, text="Leitor de QR para NFP", font=("Arial",16), bg_color="transparent").place(x=20, y=10)

#Adicionar fotos
abrir_diretorio =ctk.CTkButton (janela, text="Adicionar fotos", command=add_fotos).place(x=30, y=60)

#Ler QR codes
ler = ctk.CTkButton (janela, text="Ler QR codes", command=leitor.back).place(x=30, y=100)

#Abrir planilha com chaves
planilha1 =ctk.CTkButton (janela, text="Chaves de acesso", command=chaves, fg_color="DarkSeaGreen4").place(x=30, y=160)

#Abrir planilha com erros
planilha2 =ctk.CTkButton (janela, text="Erros na leitura", command=erros, fg_color="tomato").place(x=30, y=200)

#Lançar os QR codes no site
preencher = ctk.CTkButton (janela, text="Lançar os QR codes", command=back, fg_color="sea green").place(x=30, y=240)

janela.mainloop ()