# imports
import string
import secrets
import os

symbols = ".+-[]*~_@#:?"

#levels
def levelPass(string):
  if (string in ["M", "D"]):
    return True
  return False
  
def middlePassword(base):
  lista = string.digits + symbols
  password = base + ''.join(secrets.choice(lista) for i in range(8))
  return password

def hardPassword():  
  lista = string.ascii_letters + string.digits + symbols
  password = ''.join(secrets.choice(lista) for i in range(10))
  return password

#clear
def clear():
  if(os.name == "nt"):
    os.system("cls")
  else:
    os.system("clear")
