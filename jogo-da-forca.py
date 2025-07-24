import random
from os import system, name

palavras = [{"palavra":"python", "dica" : "linguagem de programação da cobra"}] 

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def jogo(palavras):
    
    palavra = palavras[random.randrange(0,len(palavras))]
    chances = 6
    letras_certas = []  
    letras_erradas = []

    for letra in palavra["palavra"]:
        if letra == " ":
            letras_certas.append(letra)
        else:
            letras_certas.append("_")
    
    while chances > 0:
        img = display_hangman(chances)
        tentativa = input(f"""
XXXXXXXXX Acerte a palavra XXXXXXXXX
                          
Dica: {palavra["dica"]}                
        {img}
                          
{"".join(letras_certas)}    
                                               
Letras erradas: {", ".join(letras_erradas)}

você tem: {chances} tentativas
""").lower()
        
        if (tentativa in palavra["palavra"]) and (tentativa not in letras_certas) and (len(tentativa) == 1 and tentativa.isalpha()):
            limpar_tela()
            for i, letra in enumerate(palavra["palavra"]):
                if tentativa == letra:
                    letras_certas[i] = letra
        
        elif tentativa in letras_certas or tentativa in letras_erradas:
            limpar_tela()
            print('\nVocê já digitou essa letra!')

        elif len(tentativa) > 1 or not tentativa.isalpha():
            limpar_tela()
            print('\nVocê só pode digitar uma letra!')

        else:
            limpar_tela()
            letras_erradas.append(tentativa)
            chances -= 1
        
        if "_" not in letras_certas:
            limpar_tela()
            print(f'\nVocê venceu!, a palavra era {palavra["palavra"]}')
            break

    if chances == 0:
        print(f"você perdeu!, a palavra era: {palavra["palavra"]}")

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
        print("A palavra não pode conter números !")
        return False
    
    elif tem_caracteres == False:
        limpar_tela()
        print("A palavra não pode conter caracteres !")
    
    elif palavra_existe == True:
        limpar_tela()
        print(f"A palavra {palavra} já existe !")
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
        nova_palavra = input("""
======== Adicionando ========
[D] - Ver lista de palavras
[Q] - Voltar para o menu
=============================
Digite a palavra nova: """)
        
        if nova_palavra.lower() == "q":
            limpar_tela()
            return palavras
        
        elif nova_palavra.lower() == "d":
            limpar_tela()
            exibindo_palavras(palavras= palavras)

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
Digite 'Q' para voltar
""").lower()
    if opcao == "q":
        limpar_tela()
        print()
    else:
        limpar_tela()
        print("Opção Inválida!")       

while True:
    escolha = input("""
============ MENU ============
[A] - Jogar
[S] - Adicionar novas palavras
[D] - Ver palavras existentes
[Q] - Finalizar programa
==============================
Sua escolha: """)
    
    if escolha.lower() == "a":
        limpar_tela()
        print("jogo iniciado!")
        jogo(palavras= palavras)
    
    elif escolha.lower() == "s":
        limpar_tela()
        palavras = adicionar_palavra(palavras)
    
    elif escolha.lower() == "d":
        limpar_tela()
        exibindo_palavras(palavras)
    
    elif escolha.lower() == "q":
        limpar_tela()
        print("Programa finalizando...")
        break
    else:
        limpar_tela()
        print("Opção Inválida!")