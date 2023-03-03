import funcoes
import string
import time

#entrada
levelStr = str.upper(input("Nível da senha:\n------------\n[D] Difícil \n[M] Médio \n------------\n"))
while(levelStr not in ["M", "D"]):
  funcoes.clear()
  print("Por favor, insira apenas os valores possíveis.")
  time.sleep(2)
  levelStr = str.upper(input("\nNível da senha:\n------------\n[D] Difícil \n[M]Médio \n------------\n"))

#senhas
password = ""
if (levelStr == "M"):
  password = funcoes.hardPassword()
elif(levelStr == "D"):
  base = input("Um nome: ")
  password = funcoes.middlePassword(base)

#saída
print("Sua senha:", password)
