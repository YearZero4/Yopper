
#-------------------------DEPENDENCY------------------------------#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from colorama import Fore, Style, init
from bs4 import BeautifulSoup as b
import time, requests, random, json, re, os, platform
#---------------------------------------------------------------#

# ------------------------- COLORS ---------------------------- #
GREEN=f"{Fore.GREEN}{Style.BRIGHT}"
RED=f"{Fore.RED}{Style.BRIGHT}"
WHITE=f"{Fore.WHITE}{Style.BRIGHT}"
# --------------------------------------------------------------#

link='https://www.facebook.com/recover/initiate/'
history=os.path.join('.', 'src', 'history.txt')
email_found=os.path.join('.', 'src', 'email_found.txt')
prcs = platform.architecture()[0]
users=[]
arr_history=[]

init(autoreset=True)

print(f'{GREEN}' + r'''
        __  __                           
        \ \/ /___  ____  ____  ___  _____
         \  / __ \/ __ \/ __ \/ _ \/ ___/
         / / /_/ / /_/ / /_/ /  __/ /    
        /_/\____/ .___/ .___/\___/_/     
               /_/   /_/                 
''')
print(f'{GREEN} [CHECK] {WHITE}Programa iniciado con exito')

if not os.path.exists(history):
	with open(history, 'w') as f:
		f.write('')
		f.close()

if not os.path.exists(email_found):
	with open(email_found, 'w') as f:
		f.write('')
		f.close()

def hisStart():
 with open(history, 'r') as f:
  show=f.readlines()
  for i in show:
   x=i.replace('\n', '')
   arr_history.append(x)
hisStart()

if prcs == '32bit':
 geck0 = 'geckodriver32bit.exe'
else:
 geck0 = 'geckodriver64bit.exe'

path_geck0=os.path.join('.', 'src', 'driver', geck0)
dirwordlist=os.path.join('.', 'src', 'wordlists')
showDirFile=os.listdir(dirwordlist)


def openFile(filename):
 with open(filename, 'r') as f:
  readline=f.readlines()
  for i in readline:
   line=i.replace('\n', '')
   users.append(line)

for filename in showDirFile:
 path_filename=os.path.join(dirwordlist, filename)
 openFile(path_filename)

def history_save(text, x):
 with open(x, 'a') as f:
  f.write(text + '\n')
  f.close()


def checkUsers():
 if users:
  return True
 else:
  return False


options = Options()
options.add_argument("--headless")
service = Service(executable_path=path_geck0)
driver = webdriver.Firefox(service=service, options=options)
driver.get(link)
print(f' {GREEN}[CHECK] {WHITE}Ahora estamos en [FACEBOOK]\n')
time.sleep(8)

print(f' {GREEN}[+] {WHITE}RESULTS FOUND \n')
if checkUsers() == True:
 yopAddress = [e + "@yopmail.com" for e in users]
 for yop in yopAddress:
  if yop not in arr_history:
  	time.sleep(2)
  	try:
  	 element = driver.find_element(By.ID, "identify_email")
  	 element.send_keys(yop)
  	 element.send_keys(Keys.RETURN)
  	 time.sleep(4)
  	 html_content = driver.page_source
  	 soup=b(html_content, 'html.parser')
  	 find1=soup.find_all('a', class_="_aklt")
  	 find2=soup.find_all('a', class_='_42ft _4jy0 _al4m _4jy6 _517h _51sy')
  	 if find1 or find2:
  	  print(f' {GREEN}[+] {WHITE}La cuenta existe => [{yop}]')
  	  driver.back()
  	  history_save(yop, history)
  	  history_save(yop, email_found)
  	 else:
  	  print(f'{RED} [x]{WHITE} No existe la cuenta => [{yop}]')
  	  history_save(yop, history)
  	except:
  	  print(f'{RED} [x]{WHITE} No existe la cuenta => [{yop}]')
  	  history_save(yop, history)
  	driver.back()


