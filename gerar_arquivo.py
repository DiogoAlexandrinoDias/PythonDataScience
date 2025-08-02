
# csv - comma separted values
# arquivo separado por ;

import csv

# os - operational system
#  criar arquivos, gerenciar pastas
import os

# Biblioteca de graficos
import matplotlib.pyplot as plt

# nome do arquivo
ARQUIVO_CSV = "dados_senai.csv"

# verificar se o arquivo existe
arquivo_existe = os.path.exists(ARQUIVO_CSV)
# arquivo -> true || false

# salvar arquivo 
def salvar_em_csv (nome, idade, email):
    # a = acrescimo
    # newLine -> evitar linhas brancas
    with open (ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        if  not arquivo_existe:
            # cria uma nova linha
            escritor.writerow(['nome', 'idade', 'email'])
        escritor.writerow([nome, idade, email])

def mostrar_grafico():
    faixas = {
        '0-17': 0,
        '18-30': 0,
        '31-45': 0,
        '46-60': 0,
        '60+':0
    }

    with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                idade = int(linha['idade'])
                if idade <= 17:
                    faixas['0-17'] +=1
                elif idade <= 30:
                    faixas['18-30'] += 1
                elif idade <=45:
                    faixas['31-45'] += 1
                elif idade <= 60:
                    faixas['46-60'] += 1
                else:
                    faixas['60+'] += 1
            
            except ValueError:
                continue              
        plt.bar(faixas.keys(), faixas.values(), color='skyblue')
        plt.title("Distribuilção por Faixa Etaria")
        plt.xlabel("Faixa Etaria")
        plt.ylabel("Quantidade de Pessoas")      
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()                                                         

def main():

    while True:
        print("\nDigite os daods de usuario")
        nome = input("Nome :")
        idade = input("Idade :")
        email = input("Email :")

        salvar_em_csv(nome, idade, email)
        print("Dados salvos co sucesso")

        continuar = input("Deseja adicionar outro? s/n ")
        if continuar != 's':
            break

    mostrar_grafico()
           
if __name__ == '__main__':
    main()
