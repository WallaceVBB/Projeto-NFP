import glob
import os
import cv2
import pandas as pd
from qreader import QReader


def back ():

    df = pd.DataFrame(columns=['filename', 'qr'])
    files = glob.glob('QRcodes/*.jpeg')
    #files = glob.glob('*.jpeg')
    #cont_inicio = os.list(QRcodes)

    qreader = QReader()

    def read_qr_code(filename):
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        if value != "":
            return value
        else:
            img = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
            detect = qreader.detect_and_decode(image=img)
            return detect

    for file in files:
        chaves = read_qr_code(file)
        row = {'filename': file, 'chaves': chaves}

        if chaves == (None,):
           erros = pd.read_excel("Erros.xlsx")
           erros = erros.append(row, ignore_index=True)
           erros.to_excel("Erros.xlsx", index=False)
           #Mover imagem para pasta de erros...
           os.rename(file, f"Falhas na leitura - {file}")
        else:
            chave = pd.read_excel("Chaves de acesso.xlsx")
            chave.replace("\('CFe", "", regex=True, inplace=True)
            #chave['chaves'] = chave['chaves'].str.slice(0, 44)
            chave = chave.append(row, ignore_index=True)
            chave['chaves'] = chave['chaves'].str.slice(0, 44)
            chave.to_excel("Chaves de acesso.xlsx", index=False)
            # Apagar mover imagem para Leituras realizadas...
            #arquivo = file.replace("QRcode/", f"{file}")
            #os.rename(f"{file}", f"{arquivo}")
            os.rename(file, f"Lidos com sucesso - {file}")


