import random
import json
from os import system, name

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def recuperando_palavras():
    try:
        with open('arquivos/palavra', 'r') as arquivo:
            conteudo = arquivo.read()
        return json.loads(conteudo)

    except Exception as e:
        return [
                {"palavra":"python", "dica":"linguagem de programação da cobra"},
                {"palavra":"java", "dica":"linguagem do café"}
                ]

palavras = recuperando_palavras()

def display_hangman(chances):
    imgs = [
        """
         ________
         |      |
         |
         |
         |
         |
         -
        """,
        """
         ________
         |      |
         |      O 
         |
         |
         |
         -
        """,
        """
         ________
         |      |
         |      O 
         |      |
         |      |
         |
         -
        """,
        """
         ________
         |      |
         |      O 
         |     \\|
         |      |
         |
         -
        """,
        """
         ________
         |      |
         |      O 
         |     \\|/
         |      |
         |
         -
        """,
        """
         ________
         |      |
         |      O 
         |     \\|/
         |      |
         |     /
         -
        """,
        """
         ________
         |      |
         |      O 
         |     \\|/
         |      |
         |     / \\
         -
        """
    ]
    imgs.reverse()
    return imgs[chances]

def jogo(palavras):
    
    palavra = random.choice(palavras)
    chances = 6
    letras_certas = []  
    letras_erradas = []

    for letra in palavra["palavra"]:
        if letra == " ":
            letras_certas.append(letra)
        else:
            letras_certas.append("_")
    
    while chances > 0:
        boneco = display_hangman(chances)
        img = f"""
XXXXXXXXX Acerte a palavra XXXXXXXXX
                          
Dica: {palavra["dica"]}                
        {boneco}
                          
{"".join(letras_certas)}    
                                               
Letras erradas: {", ".join(letras_erradas)}

você tem: {chances} tentativas"""
        print(img)
        tentativa = input().lower()
        
        chances = verifica_tentativa(tentativa, palavra, letras_certas, letras_erradas, chances)
        
        if "_" not in letras_certas:
            limpar_tela()
            print(f'\nVocê venceu!, a palavra era {palavra["palavra"]}')
            break

    if chances == 0:
        print(f"você perdeu!, a palavra era: {palavra["palavra"]}")

def verifica_tentativa(tentativa, palavra, letras_certas, letras_erradas, chances ):

        if (tentativa in palavra["palavra"]) and (tentativa not in letras_certas) and (len(tentativa) == 1 and tentativa.isalpha()):
            limpar_tela()
            for i, letra in enumerate(palavra["palavra"]):
                if tentativa == letra:
                    letras_certas[i] = letra
            return chances

        elif (tentativa in letras_certas) or (tentativa in letras_erradas):
            limpar_tela()
            print('\nVocê já digitou essa letra!')
            return chances
        
        elif len(tentativa) > 1 or not tentativa.isalpha():
            limpar_tela()
            print('\nVocê só pode digitar uma letra!')
            return chances

        else:
            limpar_tela()
            letras_erradas.append(tentativa)
            return chances - 1

def verifica_palavra(palavra, palavras):
    
    tem_numero = any(char.isdigit() for char in palavra)
    tem_caracteres = all(char.isalpha() for char in palavra)
    palavra_existe = any(item['palavra'] == palavra for item in palavras)

    if palavra.strip() == "":
        limpar_tela()
        print("Digite algo primeiro!")
        return False
    
    elif tem_numero == True:
        limpar_tela()
        print("A palavra não pode conter números!")
        return False
    
    elif tem_caracteres == False:
        limpar_tela()
        print("A palavra não pode conter caracteres!")
    
    elif palavra_existe == True:
        limpar_tela()
        print(f"A palavra {palavra} já existe!")
        return False

    else:
        return True

def verifica_dica(dica):
    
    if dica.strip() == "":
        limpar_tela()
        print("A dica não pode estar vazia!")
        return False
    
    elif dica.isdigit() == True:
        limpar_tela()
        print("A dica não pode ser só números !")
        return False
    
    else:
        return True

def adicionar_palavra(palavras):
    while True:
        lista_palavras = []

        for indice, item in enumerate(palavras, start=1):
            lista_palavras.append(f"-------------------------")
            lista_palavras.append(f"{indice} - {item['palavra']}")
            lista_palavras.append(f"Dica: {item['dica']}")
            lista_palavras.append(f"-------------------------")

        nova_palavra = input(f"""
======== Adicionando Palavra ========
{"\n".join(lista_palavras)}
=====================================
[5] - Voltar para o menu
=====================================
Digite a palavra nova: """)
        
        if nova_palavra == '5':
            limpar_tela()
            return palavras
        
        elif verifica_palavra(palavra= nova_palavra, palavras= palavras):
            limpar_tela()
            while True:
                nova_palavra_dica = input("""
======== Adicionando ========
Agora digite uma dica !
=============================
Dica: """)
            
                if verifica_dica(dica= nova_palavra_dica):
                    limpar_tela()                    
                    palavra = {"palavra":nova_palavra.lower(), "dica":nova_palavra_dica}
                    palavras.append(palavra)
                    print(f'{nova_palavra} adicionada!')
                    break

def remover_palavra(palavras):
    while True:
        lista_palavras = []

        for indice, item in enumerate(palavras, start=1):
            lista_palavras.append(f"-------------------------")
            lista_palavras.append(f"{indice} - {item['palavra']}")
            lista_palavras.append(f"Dica: {item['dica']}")
            lista_palavras.append(f"-------------------------")

        palavra_escolhida = input(f"""
========= Retirando Palavra =========
{"\n".join(lista_palavras)}
=====================================
[5] - Voltar para o menu
=====================================
Digite a palavra: """)
        
        if palavra_escolhida == '5':
            limpar_tela()
            return palavras
        for palavra in palavras:
            if palavra["palavra"] == palavra_escolhida:
                palavras.remove(palavra)
                limpar_tela()
                print(f"A palavra {palavra_escolhida} foi removida!")
                break
            else:
                limpar_tela()
                print("Nenhuma palavra foi encontrada!")
                
def exibindo_palavras(palavras):
    lista_palavras = []

    for indice, item in enumerate(palavras, start=1):
        lista_palavras.append(f"-------------------------")
        lista_palavras.append(f"{indice} - {item['palavra']}")
        lista_palavras.append(f"Dica: {item['dica']}")
        lista_palavras.append(f"-------------------------")
    
    opcao = input(f"""
======== Palavras =========
{"\n".join(lista_palavras)}
===========================
[5] - Voltar
===========================
Sua escolha """).lower()
    if opcao == '5':
        limpar_tela()
        print()
    else:
        limpar_tela()
        print("Opção Inválida!")       

def salvar_palavra(palavras):
    while True:
        escolha = input("""
========== Salvando ==========
[1] - Salvar alterações
[2] - Não salvar alterações
==============================
Sua escolha: """)
        if escolha == '1':
            limpar_tela()
            with open('arquivos/palavra', 'w') as arquivo:
                arquivo.write(json.dumps(palavras))
            print("Alterações salvas!")
            break

        elif escolha == '2':
            limpar_tela()
            print("alterações não salvas!")
            break

while True:
    escolha = input("""
============ MENU ============
[1] - Jogar
[2] - Adicionar novas palavras
[3] - Remover palavra
[4] - Ver palavras existentes
[5] - Finalizar programa
==============================
Sua escolha: """)
    
    if escolha == '1' :
        limpar_tela()
        print("jogo iniciado!")
        jogo(palavras= palavras)
    
    elif escolha.lower() == '2':
        limpar_tela()
        palavras = adicionar_palavra(palavras)

    elif escolha == '3':
        limpar_tela()
        remover_palavra(palavras)

    elif escolha.lower() == '4':
        limpar_tela()
        exibindo_palavras(palavras)
    
    elif escolha.lower() == '5':
        limpar_tela()
        salvar_palavra(palavras)
        print("Programa finalizado :)")
        break
    else:
        limpar_tela()
        print("Opção Inválida!")