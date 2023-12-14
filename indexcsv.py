# Gravando dados em um arquivo csv:
import csv

with open("planilha.csv","w", newline="") as obj:
     w = csv.writer(obj, delimiter=",")
     w.writerow(["Eduardo", "4899442618","VENDEDOR"])
     w.writerow(["Tomas", "4899442618","VENDEDOR"])


# Lendo dados de um arquivo csv:
with open("planilha.csv","r") as obj:
     i = csv.reader(obj, delimiter=",")
     for j in i:
          print(" ".join(j))