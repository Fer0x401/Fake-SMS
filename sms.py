#!/usr/bin/env python
#code by Fer0x401
#Modúlos
import time, os, requests

#COLORES
dr='\033[1;34m'
rd='\033[1;30m'
nv='\033[1;39m'
nh='\033[1;31m'

os.system("clear")
print(f"""{dr}
████▒  ▄▄▄       ██ ▄█▀▓█████     ██████  ███▄ ▄███▓  ██████
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀    ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███      ░ ▓██▄   ▓██    ▓██░░ ▓██▄
{rd}░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄      ▒   ██▒▒██    ▒██   ▒   ██
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒██████▒▒▒██▒   ░██▒▒██████▒▒
▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
░       ▒   ▒▒ ░░ ░{rd}code by {nv}@Fer0x401{rd}▒  ░ ░░  ░  ░░
░ ░     ░   ▒   ░ ░░ ░    ░      ░  ░  ░  ░      ░   ░  ░  ░
         ░  ░░  ░      ░  ░         ░         ░""")

num = input(f"""
{rd}┌══════════════════════┐
{rd}█ {dr}NUMERO DE LA VICTIMA{rd} █
{rd}└══════════════════════┘
┃
└═► {nv}""")

sms = input(f"""
{rd}┌════════════════════┐
{rd}█ {dr}ESCRIBE EL MENSAJE{rd} █
{rd}└════════════════════┘
┃
└═► {nv}""")

resp = requests.post('https://textbelt.com/text', {
 'phone': f'{num}',
  'message': f'{sms}',
  'apikey': 'textbelt',
  })

print(f"""
{rd}┌══════════════════┐
{rd}█ {dr}ENVIANDO SMS..👻{rd} █
{rd}└══════════════════┘""")
time.sleep(1.8)
input(f"""
{rd}┌════════════════════════════┐
{rd}█ {dr}SMS ENVIADO PRESIONA ENTER{rd} █
{rd}└════════════════════════════┘

""")

os.system("python sms.py")
