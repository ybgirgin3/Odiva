#!/usr/bin/env python3
# -*- coding: utf8 -*-
# filename: update_path_finder.py

# https://fileinfo.com/filetypes/text

import os
# from update_emailer import *

# dosya formatları
# text_formats = ['.txt', '.html', '.docx', '.xlsx', '.xml']
# image_formats = [
                    # '.jpg', '.png', '.jpeg', '.svg', '.tif', '.tiff', 
                    # '.bmp', '.gif', '.eps', '.raw', '.cr2', '.net', 
                    # '.orf', '.sr2', '.PSD', '.XCF', '.AI', '.CDR'
        # ]

pathlist = []

def path_finder(file_name):
    for kökdizin, altdizinler, dosyalar in os.walk('{}/'.format(os.path.expanduser('~'))):
        for dosya in dosyalar:
            if dosya == file_name:
                # bulunması istenen dosya gerçekten dosya mı diye kontrol et
                if os.path.isfile:
                    # hedef text dosyanın dizinine git
                    os.chdir(kökdizin)
                    # dosyanın adı ve dizini ile absolute bir path oluştur
                    file_path = os.path.abspath(os.path.join(kökdizin, dosya))
                    # print('dosya yolu:\n {}'.format(file_path))
                    pathlist.append(file_path)
                    # if os.path.splitext(file_path)[1]  in text_formats:
                        # print('dosya text formatlı')
                        # hedef text dosyasını oku ve içeriği döndür
                        # with open(dosya, 'r') as f:
                            # ret = f.read()
                            # print(ret)
                            # return ret
                            # text_sender(ret)

                    # elif os.path.splitext(file_path)[1] in image_formats:
                        # print('dosya imaj formatlı')
                        # imaj uzantılı dosyanın pathini döndür 
                        # bu emailer modülüne attachment olarak yollanacak olan
                        # dosyanın yerini bildirecek
                        # return file_path
                        # print(file_path)
                        # image_sender(file_path)

file_name = input('dosya adını gir: ')
path_finder(file_name)
from pprint import pprint
pprint(pathlist)
print('\n***** {} path found on {} *****'.format(len(pathlist), os.path.expanduser('~')))
# end file
