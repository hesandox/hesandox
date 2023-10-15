import requests
from bs4 import BeautifulSoup
import os
import time
from art import tprint





def out_red(text):
    print("\033[32m{}".format(text))
out_red("")
tprint("hesandox")

def out_red(text):
    print("\033[31m{}".format(text))
out_red("Channel - @hesandox")

def out_red(text):
    print("\033[31m{}".format(text))
out_red("Author- @hesans")

time.sleep(3)
def out_red(text):
    print("\033[32m{}".format(text))
out_red("Идет загрузка скрипта...")

time.sleep(4)
def out_red(text):
    print("\033[32m{}".format(text))
out_red("Идет загрузка базы данных...")

time.sleep(3)
def out_red(text):
    print("\033[32m{}".format(text))
out_red("Успешно!")

def out_red(text):
    print("\033[37m{}".format(text))
out_red("")


time.sleep(2)

if os.path.isfile('last.txt'):
    os.remove('last.txt')

phone = input("[*] Номер телефона: +")
service = "https://spravochnik.tel/phone/"
link = service + phone


def get_html(link, params=None):
    r = requests.get(link, params=params)
    return r




def parse():
    html = get_html(link)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('''Ошибка!
Вы ввели некорректный номер телефона!
Убедитесь, что введённый Вами номер, не содержит лишних символов.''')
        stop()


def out_red(text):
    print("\033[34m{}".format(text))
out_red("")
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('tbody')
    file = open("trash.tr", "w")
    file.write(result.text)
    file.close()
    with open("trash.tr") as a:
        with open("last.txt", 'a') as out:
            for line in filter(lambda x: x != '\n', a):
                out.write(line)
    os.remove('trash.tr')
    print("Номер:", phone)
    print("\n" + "Результат:" + "\n")
    file1 = open("last.txt", "r")
    while True:
        line = file1.readline()
        if not line:
            break
        print(line.strip())
    file1.close

    def out_red(text):
        print("\033[36m{}".format(text))

    out_red("")

    print('''
Напоминаем это BetaTest скоро лучше.''')


parse()