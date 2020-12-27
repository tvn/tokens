from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import socket
import os
import random
from colorama import Fore, Back, init 
init(convert=True)

errors = 0
pending = 0
valid = 0




class DiscordBot:
  global errors
  global valid
  global pending
  def __init__(self):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    self.bot = webdriver.Firefox(options=fireFoxOptions)
  
  def createAccount(self):
    global errors
    global valid
    global pending
    bot = self.bot
    bot.get('https://discord.com')
    time.sleep(2)
    bot.find_element_by_class_name('openButton-McADyK').click()
    time.sleep(2)
    username = bot.find_element_by_class_name('username-27KRPU')
    time.sleep(2)
    username.clear()
    time.sleep(2)
    usernameslist = ['herpes_free_since_03','kiss-my-axe', 'king_0f_dairy_queen','Passive was here','dildo_swaggins', 'shaquille_oatmeal','skedaddle','donkey29','big_mamas_house', 'hanging_with_my_gnomies','tweezers','crapulence', 'fuck black people','Disc0rd admeen','dickdoodle','mc server owner','Deku Top Hero On The Set','crapulence','Lux','rape.works','fuck the ToS','emma2925','Freda1','RIP A','kthxbye','ggnoree','unstable is a skid','BackEnd','𝓴𝖊𝖓𝖘𝖊𝖎','ʙʟᴇᴀᴄʜ da skid','school shooter','now thats a lot of damage','fortnite is trash','ʙʟᴇᴀᴄʜ ␀#133 is a skid','print("goodbye world")','bitchlasagna', 'fuck black people','manhole','bitchlasagna', 'fuck black people','l33t 1337 haxor','bitchlasagna','pornhub','among us is fucking trash','XD OMegalul', 'ask_yo_girl_about_me', 'fuck black people','ares rat','join ares .gg/Mm2kcqq','I have to piss','axua.xyz','debt']
    wow = random.choice(usernameslist)
    username.send_keys(wow)
    time.sleep(2)
    username.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
      with open("porn.js", 'r') as file:
        bot.execute_script(file.read())
        valid += 1
        os.system('cls')
        print('--> Discord Account Generator <--\n')
        print(f'{Back.RESET}{Fore.RESET}| {Back.LIGHTYELLOW_EX}{Fore.LIGHTRED_EX}Pending{Back.RESET}{Fore.RESET} | {Back.LIGHTGREEN_EX}{Fore.BLACK}MADE{Fore.RESET}{Back.RESET} | {Back.LIGHTRED_EX}Error{Back.RESET} |')
        print(f'{Back.RESET}{Fore.RESET}| {pending}       | {valid}    | {errors}     |')
    except Exception as error:
      errors += 1
      print(error)
    time.sleep(3)
    bot.close()

def Bot():
  global errors
  global valid
  global pending
  pending += 1
  os.system('cls')
  print('--> Discord Account Generator <--\n')
  print(f'{Back.RESET}{Fore.RESET}| {Back.LIGHTYELLOW_EX}{Fore.LIGHTRED_EX}Pending{Back.RESET}{Fore.RESET} | {Back.LIGHTGREEN_EX}{Fore.BLACK}MADE{Fore.RESET}{Back.RESET} | {Back.LIGHTRED_EX}Error{Back.RESET} |')
  print(f'{Back.RESET}{Fore.RESET}| {pending}       | {valid}    | {errors}     |')
  lol = DiscordBot()
  lol.createAccount()


print('--> Discord Account Generator <--\n')
print(f'{Back.RESET}{Fore.RESET}| {Back.LIGHTYELLOW_EX}{Fore.LIGHTRED_EX}Pending{Back.RESET}{Fore.RESET} | {Back.LIGHTGREEN_EX}{Fore.BLACK}MADE{Fore.RESET}{Back.RESET} | {Back.LIGHTRED_EX}Error{Back.RESET} |')
print(f'{Back.RESET}{Fore.RESET}| {pending}       | {valid}    | {errors}     |')

while True:
  Bot()
  os.system('cls')
  print('--> Discord Account Generator <--\n')
  print(f'{Back.RESET}{Fore.RESET}| {Back.LIGHTYELLOW_EX}{Fore.LIGHTRED_EX}Pending{Back.RESET}{Fore.RESET} | {Back.LIGHTGREEN_EX}{Fore.BLACK}MADE{Fore.RESET}{Back.RESET} | {Back.LIGHTRED_EX}Error{Back.RESET} |')
  print(f'{Back.RESET}{Fore.RESET}| {pending}       | {valid}    | {errors}     |')
  time.sleep(120)
