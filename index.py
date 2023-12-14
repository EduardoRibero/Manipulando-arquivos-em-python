# A função Path consegue criar um caminho para o seu arquivo apenas com os nomes das pastas que compoem esse caminho:
import os
caminho = os.path.join("caminho","de","teste")
print(caminho)


# A função open realiza a abertura dos arquivos, o primeiro parametro seria o caminho do arquivo 
# O segundo parametro seria o modo como vamos abrir o arquivo 
# ("W" para gravação), ("r" para leitura), e ("w+" para leitura e gravação).
arquivo = open("arquivo.txt", "w") 
for i in range(10):
    arquivo.write("Olá Mundo!\n") 
    #sempre fechar o arquivo
    arquivo.close 


# Para não correr o risco de esquecer de fechar o arquivo ("with"):
with open("arquivo02.txt","w") as arquivo:
    for i in range(10):
        arquivo.write("Ola mundo!\n")


# Leitura do arquivo, você pode salvar os dados do arquivo tanto em um interavel quanto em uma variavel:
lista = list()
with open("arquivo.txt","r") as arquivo:
   lista.append(arquivo.read())

print(lista)

with open("arquivo02.txt","r") as arquivo:
    variavel = arquivo.read()

print(variavel)


