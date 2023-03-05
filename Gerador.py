#obtendo dados da lista de  produto

from datetime import date
from csv import reader
import csv

class Produtos:

    def __init__(self, nome_produto, preco_produto, peso):
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.peso = peso

    def custo_por_grama(self):
        """Gera o valor do custo de cada grama do produto"""
        self.custo_grama = self.preco_produto/self.peso
        return self.custo_grama


class Ingredientes():
    def __init__(self, qtd_usada, custograma):
        self.qtd_usada = qtd_usada
        self.custograma = custograma
    def custo_sabor(self):
        self.custo_sabor = self.qtd_usada * self.custograma





#Dicionarios,lista e variavies

tupla_produtos = ("Mussarela", "Bacon", "Frango") # Gera uma lista padrao
tupla_sabores = ("Mussarela", "Frango 1", "Calabresa")


#Funcoes do programa
def parametros_produtos(nome, preco, peso):

    return nome, preco, peso


def parametros_sabores(nome_sabor, qtd_usada, ingredientente):
    return nome_sabor, qtd_usada, ingredientente







def add_ingredientes( nome, ingrediente_custo):
    qtd_usada = int(input(f"Quantas gramas de {nome} e usado no sabor ? :"))
    soma_custo = (qtd_usada * ingrediente_custo)
    return soma_custo



def menu_opcoes_principal():
    print(25*"=", "Calculadora de Custo ", 25*"=")
    print(
        '''
        --------------------------------------
        |**************** MENU ***************|
        --------------------------------------
            [1] -> Lista de Produtos
            [2] -> Sabores de pizzas 
            [3] -> Gerar custo  
        '''
    )
    while True:
        escolher = int(input("Escolha o numero das opcoes acima =>:"))
        if escolher > 3 or escolher <= -1:
            print("Numeros de opcoes invalidade ")
            continue
        else:
            break
        return escolher


def armazenamento ():

    nome, preco, peso = parametros_produtos(f"Mussarela {print(tupla_produtos[0])}",
                                            preco=float(input("Valor pago:")),peso=float(
                                                input(
                                                    "Peso contendo na embalagem * Usar a unidade de gramas :")))

    Mussarela = Produtos(nome, preco, peso)


# -----------------------------------------------------------------------------------------------------------------------
    nome, preco, peso = parametros_produtos(f"Bacon {print(tupla_produtos[1])}",
                                            preco=float(input("Valor pago:")),
                                            peso=float(
                                                input(
                                                    "Peso contendo na embalagem * Usar a unidade de gramas :")))

    Bacon = Produtos(nome, preco, peso)


# ----------------------------------------------------------------------------------------------------------------------
    nome, preco, peso = parametros_produtos(f"Frango {print(tupla_produtos[2])}",
                                            preco=float(input("Valor pago:")),
                                            peso=float(
                                                input(
                                                    "Peso contendo na embalagem * Usar a unidade de gramas :")))

    Frango = Produtos(nome, preco, peso)


# -----------------------------------------------------------------------------------------------------------------------
    # Amarzenamento de dados

    with open("Dictc_custos_ingredientes.csv", "w", newline="", encoding='utf-8') as custo_ingredientes:
        titulo = ["Id", "Nome Produto", "Custo Grama"]
        writer = csv.DictWriter(custo_ingredientes, titulo)
        writer.writeheader()



        # Mussarela
        writer.writerow({"Id": 1, "Nome Produto": str(Mussarela.nome_produto).replace("Mussarela None", "Mussarela"),
                         "Custo Grama": Mussarela.custo_por_grama().__round__(2)})

        # Bacon
        writer.writerow({"Id": 2, "Nome Produto": str(Bacon.nome_produto).replace("Bacon None", "Bacon"),
                         "Custo Grama": Bacon.custo_por_grama().__round__(2)})

        # Frango
        writer.writerow({"Id": 3, "Nome Produto":  str(Frango.nome_produto).replace("Frango None", "Frango"),
                         "Custo Grama": Frango.custo_por_grama().__round__(2)})
        custo_ingredientes.close()





    with open("produtos.csv", "w", newline="") as produtos:
        cabecalho = ["Nome Produto", "Preco", "Kg"]
        writer = csv.DictWriter(produtos, cabecalho)
        writer.writeheader()

        # Mussarela
        writer.writerow({"Nome Produto": str(Mussarela.nome_produto).replace("Mussarela None", "Mussarela"),
                         "Preco": Mussarela.preco_produto, "Kg": Mussarela.peso})

        # Bacon
        writer.writerow({"Nome Produto": str(Bacon.nome_produto).replace("Bacon None", "Bacon"),
                         "Preco": Bacon.preco_produto, "Kg": Bacon.peso})

        # Frango
        writer.writerow({"Nome Produto": str(Frango.nome_produto).replace("Frango None", "Frango"),
                         "Preco": Frango.preco_produto, "Kg": Frango.peso})



#Inicio do programa
#Gambiara
escolhido = 0


while escolhido == 0:
    escolhido = menu_opcoes_principal()

# Botao 3  ------------------------------------------------------------------------------------------------------------
    while escolhido == 3:
        print(25 * "=", "Gerar Custo")
        print('''
            [1] Ver Custo 
            [2] Refazer pesagem  dos sabores
            [0] voltar
                  ''')
        clikc = int(input("=>:"))
        if clikc == 0:
            escolhido = 0

# Botao 2  ------------------------------------------------------------------------------------------------------------

    add = ""
    count_s = 0
    while escolhido == 2:
        print(25 * "=", "Sabores Pizzas")
        print('''
        
        [1] Ver pesagem de  todos os sabores 
        [2] Refazer pesagem
        [0] voltar 
              ''')
        clikc = int(input("=>:"))
        if clikc == 0:
            escolhido = 0
        if clikc == 2:
            print(25*"=", "Refazer pesagem")
            while True:
                d_id = {}
                with open("Sabores peso.txt","w") as Sabores:
                    Sabores.write("Nome sabor:")
                    Sabores.write(" ")
                    Sabores.write(str(input("Nome sabor:")))
                    Sabores.write("\n")
                    Sabores.write("*Ingrediente:")
                    Sabores.write(" ")
                    print("="*25, "INGREDIENTES")
                r = 0
                while r == 0:
                    with open("Dictc_custos_ingredientes.csv", "r") as custo_ingredientes:
                        leitura = csv.reader(custo_ingredientes)
                        for x in leitura:
                            print(f"{x[0]}:{x[1]}")
                            d_id.update({f'{x[0]}': [x[1], x[2]]})
                        escolha_i = int(input("Escolha o numero do ingredientes que deseja adicionar:"))
                        validador = d_id.get(f"{escolha_i}")
                    with open("Sabores peso.txt", "w") as Sabores:
                        Sabores.write(validador[0])
                        Sabores.write("\n")
                        Sabores.write("Peso:")
                        Sabores.write(' ')
                        qtd_usada = float(input("Quantidade usada em Gramas:"))
                        Sabores.write(" ")
                        Sabores.write(str(qtd_usada))
                        Sabores.write("\n")
                        Sabores.write("Custo Ingrediente:")
                        Sabores.write(" ")
                        custo_grama = validador[1]
                        custo_ing_sabor = (float(custo_grama) * int(qtd_usada))
                        Sabores.write("R$ ")
                        Sabores.write(str(custo_ing_sabor))
                        Sabores.write("\n")
                        add_mais = str(input("Adicionar mais ingredientes [S/N]").strip().upper())
                        if add_mais == "N":
                            print("=>  Funcao adicionar ingrediente desligada")
                            add_s = str(input("Adicionar mais sabor [S/N]").strip().upper())
                            if add_s == "N":
                                Sabores.seek(0)
                                break
                            else:
                                cunt_s = count_s + 1
                                print(f"{count_s} Sabores Adicionados")
                        else:
                            Sabores.write("*Ingredientes:")
                            Sabores.write(" ")
                            r = 1


























    # Botao 1  ------------------------------------------------------------------------------------------------------------

    while escolhido == 1:
        print(25*"=", "Lista de Produtos")
        print('''
    [1] Ver lista de produtos com o valor atual 
    [2] Recalibrar precos de produtos
    [0] voltar 
          ''')
        clikc = int(input("=>:"))
        if clikc == 1:
            print("="*20, "Lista de produtos", "="*20)
            with open("produtos.csv", "r") as produtos:
                ler = csv.reader(produtos)
                a = [x for x in ler]
                for b, c, d in a:
                    print(f"{b} : R$ {c} : {d}g")

            while True:
                print(f">" * 25, "Lista de produtos")
                print("[0] Voltar")
                voltar = int(input("=> :"))
                if voltar > 0 or voltar <= -1:
                    print("Numero digitado ivalido")
                else:
                    break
        if clikc == 2:
                print("="*20, "Recalibrar", "="*20)
                armazenamento()
                while True:
                    print(">"*25, "Lista atualizada")
                    print("[0] Voltar  [1] Ver custo por grama")
                    voltar = int(input("=> :"))
                    if voltar == 0:
                        break
                    if voltar == 1:
                        print("="*25,"Lista Custo por Grama")
                        with open("Dictc_custos_ingredientes.csv", "r") as custo_ingredientes:
                            ler1 = csv.reader(custo_ingredientes)
                            a1 = [x for x in ler1]
                            for b1, c2, d3 in a1:
                                print(f"{b1} : {c2} : {d3}g")

        if clikc == 0:
            escolhido = 0









#Entrada com os valores do produtos

#Ingredientes




