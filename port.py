#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Чистење на екранот
subprocess.call('clear', shell=True)

# Прашање
remoteServer    = raw_input("Напиши го хостот кој сакаш да го скенираш: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Принт што ќе ти даде
print "-" * 60
print "Чекај, го скенирам хостот", remoteServerIP
print "-" * 60

# Време.Сега кога запошнува скенирањето
t1 = datetime.now()

# Скриптата скенира само од 1 до 1025 порта

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Порта {}:      Отворена".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Ти претисна Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Хостот неможе да се најде. Крај'
    sys.exit()

except socket.error:
    print "Грешка во конекцијата"
    sys.exit()

# Време.Проверка кога завршува
t2 = datetime.now()

# Колку време поминало од почетокот до крајот
total =  t2 - t1

# Принтање
print 'Скенирањето е комплетирано за: ', total
