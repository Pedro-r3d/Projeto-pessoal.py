import random
import time


inimigos = [
    {"nome" : "jorge", "vidaMax" : 10},
    {"nome" : "Maligno", "vidaMax" : 30}
]

inventario = []


capacete_comprado = False
taco_comprado = False

lutador1_vidaMax = 10
lutador1_vidaAtual = lutador1_vidaMax

while True:
    lutador1Nome = input("nome do seu lutador: ")
    if lutador1Nome != "":
        break
    else:
        print("O nome não pode estar em branco.")
        

dano_max = 10
moedas = 0

inimigo_atual = 0

opcao = 10
while opcao != "0":
    print("===== MENU PRINCIPAL =====\n1- LUTAR\n2- TREINAR\n3- STATUS\n4- MERCADO\n5- TRABALHAR\n0- SAIR")
    opcao = input("")
    if inimigo_atual < len(inimigos):
        if opcao == "1":
            
            roundAtual = 1

            lutador2_vidaMax = inimigos[inimigo_atual]["vidaMax"]
            lutador2_vidaAtual = lutador2_vidaMax
            lutador2Nome = inimigos[inimigo_atual]["nome"]


            lutador1_vidaAtual = lutador1_vidaMax
            lutador2_vidaAtual = lutador2_vidaMax
            while lutador1_vidaAtual > 0 and lutador2_vidaAtual > 0:
                print(f"=====ROUND {roundAtual}=====")
                time.sleep(1)

                dano_jogador = random.randint(1, dano_max)
                dano = random.randint(1,10)
                lutadores = [lutador1Nome, lutador2Nome]
                atacante = random.choices(lutadores)[0]

                if atacante == lutador1Nome:
                    lutador2_vidaAtual -= dano_jogador
                    print(f"{lutador1Nome} atacou e causou {dano_jogador} de dano!")
                else:
                    lutador1_vidaAtual -= dano
                    print(f"{lutador2Nome} atacou e causou {dano} de dano!")
                roundAtual += 1
                print("")
                time.sleep(1.5)
                
            print("É O VENCEDOR É...")

            time.sleep(1.5)
            if lutador1_vidaAtual > 0:
                print(f"{lutador1Nome} venceu a luta!")
                print(f"Vida final do vencedor: {lutador1_vidaAtual}")           
                inimigo_atual += 1
                input("- AVANÇAR -")
            else:
                print(f"{lutador2Nome} venceu a luta!")
                print(f"Vida final do vencedor: {lutador2_vidaAtual}")
                input("- VOLTAR -")
    else:
        print("Todos inimigos derrotados, Você pode descansar em paz...")         
        break 
    
    if opcao == "2":
        while True:
            print("1- Treinar HP\n2- Treinar força")
            opcaoTreino = input("")
            if opcaoTreino != '1' and opcaoTreino != '2':
                print("Escolha uma opção válida.")
            else:
                break
        while True:
            jokenpo = ["Pedra", "Papel", "Tesoura"]
            escolhido_computador = random.choice(jokenpo)
            while True:
                print("====== TREINANDO.... ======")
                print("Escolha Pedra, Papel ou tesoura para disputar um jokenpo e ganhar seus pontos.")
                print("1- Pedra === 2- Papel === 3- Tesoura")
                escolhido_jogador = input("")
                if escolhido_jogador != '1' and escolhido_jogador != '2' and escolhido_jogador != '3':
                    print("Escolha uma opção válida.")
                else:
                    break
            escolhido_jogador_real = ""
            perdeu = True
            if escolhido_jogador == "1":
                escolhido_jogador_real = "Pedra"
            elif escolhido_jogador == "2":
                escolhido_jogador_real = "Papel"
            elif escolhido_jogador == "3":
                escolhido_jogador_real = "Tesoura"

            if escolhido_jogador_real == "Tesoura" and escolhido_computador == "Papel":
                perdeu = False
                print("Ganhou!")
                print(f"Você escolheu {escolhido_jogador_real}, e seu oponente {escolhido_computador}")
                input("-Avançar-")
                break
                
                
            elif escolhido_jogador_real == "Pedra" and escolhido_computador == "Tesoura":
                perdeu = False
                print("Ganhou!")
                print(f"Você escolheu {escolhido_jogador_real}, e seu oponente {escolhido_computador}.")
                input("-Avançar-")
                break
                
                
            elif escolhido_jogador_real == "Papel" and escolhido_computador == "Pedra":
                perdeu = False
                print("Ganhou!")
                print(f"Você escolheu {escolhido_jogador_real}, e seu oponente {escolhido_computador}.")
                input("-Avançar-")
                break
                
            else:
                perdeu = True
                print("Perdeu!")
                print(f"Você escolheu {escolhido_jogador_real}, e seu oponente {escolhido_computador}.")
                input("- VOLTAR -")
                break
                
        if opcaoTreino == "1" and perdeu == False:
            vidaAumento = random.randint(1,10)
            lutador1_vidaMax += vidaAumento
            print(f"Ganhou {vidaAumento} de HP")
            input("")
            
        elif opcaoTreino == "2" and perdeu == False:
            dano_aumento = random.randint(1, 10)
            dano_max += dano_aumento
            print(f"Ganhou {dano_aumento} de força")
            input("")
            

    elif opcao == "3":
        print("====== STATUS JOGADOR ======")
        print(f"Lutador - {lutador1Nome}")
        print(f"Vida Max - {lutador1_vidaMax}")
        print(f"Força - 1 a {dano_max}")
        print(f"Dinheiro - {moedas}R$")
        print(f"Inventario - {inventario}")
        
        input("")

    elif opcao == "4":
        print("====== MERCADO ======")
        print("1- CAPACETE DE MALHA\n   +7 Vida max\n   200R$\n\n2- TACO DE GOLFE\n   +4 Dano max\n   250R$ ")
        opcao_compra = input("")
        preco_capacete = 200
        preco_taco = 250

        if opcao_compra == None:
            break
        if opcao_compra == "1":
            if capacete_comprado == False:
                if moedas >= preco_capacete:
                    moedas -= preco_capacete
                    if opcao_compra == "1":
                        inventario.append("Capacete de malha")
                        print("Item adicionado ao inventário.")
                        input("- VOLTAR -")
                        lutador1_vidaMax += 7
                        capacete_comprado = True
                else:
                    print("Dinheiro insuficiente")
                    input("- VOLTAR -")
            else:
                print("Item já comprado.")
                input("- VOLTAR -")

        if opcao_compra == "2":
            if taco_comprado == False:
                if moedas >= preco_taco:
                    moedas -= preco_taco
                    if opcao_compra == "2":
                        print("Item adicionado ao inventário.")
                        input("- VOLTAR -")
                        inventario.append("Taco de golfe")
                        taco_comprado = True
                        dano_max += 4
                else:
                    print("Dinheiro insuficiente")
                    input("- VOLTAR -")
            else:
                print("Item já comprado.")
                input("- VOLTAR -")

            

    elif opcao == "5":
        print("===== TRABALHANDO... =====")
        print("Responda essas questões de matemática para ganhar dinheiro")
        while True:
            numero_um = random.randint(1, 100)
            numero_dois = random.randint(1,100)
            resposta = numero_dois + numero_um
            print(f"{numero_um} + {numero_dois}")
            try:
                tentativa = int(input("Responda: "))
                if tentativa == resposta:
                    moedas += 50
                    moedas_ganhas = 50
                    print("Resposta correta.")
                    print(f"+ {moedas_ganhas}")
                    
                    input("- VOLTAR -")
                    break
                elif tentativa != resposta:
                    print("Resposta incorreta.")
                    input("- VOLTAR -")
                    break

            except Exception:
                print("Valor inválido!")
                input("- VOLTAR -")
                break

                
            