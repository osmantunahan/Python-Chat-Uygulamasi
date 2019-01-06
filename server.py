#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# Bir tane socket nesnesi oluşturulur.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Yerel makinenin ismi alınır.
host = socket.gethostname()
# Servis için bir tane port numarası belirlenir.
port = 12347
# Yerel makine ismi ile port numarası bağlanır.
s.bind((host, port))
# İstemci bağlantısı için port dinlemesi başlatılır.
s.listen(10)  # -> 10 istemci bağlanabilir.
# istemci ve adresi kabul edilir.
c, addr = s.accept()
# Bağlanan istemciye hoşgeldin mesajı gönderilir.
c.sendall(bytes("Merhaba!".encode("utf-8")))
# Bağlantı adresi sunucu ekranına bastırılır.
print('{} bağlandı.'.format(addr))
# Sunucunun sürekli açık kalması için sonsuz döngüye ihtiyacımız var.
# Veya mesaj adediyle veya başka parametrelerle döngü sonlu da olabilir...
while True:
    # İstemciden gelen, ara bellek boyutu 1024 olan,
    # byte tipindeki mesaj stringe dönüştürülür.
    # Bu string'in ilk elemanı hariç diğer elemanları data isminde
    # bir değişkene atanır.
    data = str(c.recv(1024))[1:]
    # Eğer istemciden mesaj gelmişse
    if data:
        # İstemcinin mesajını bastır.
        print("İstemci: {}".format(data))
        # İstemciye göndereceğimiz mesajı yazalım.
        respond = input("Sunucu: ").encode("utf-8")
        # Mesaj "q" ise programdan çıkalım.
        if respond == b"q":
            exit()
        # Diğer her türlü durumda mesajımız karşı tarafa gitsin.
        else:  # İstemciye mesaj byte verisi olarak gönderilir.
            c.sendall(bytes(respond))