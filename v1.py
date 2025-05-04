import random
from os import system, name

palavras = ["python", "java", "sql", "springboot", "docker"]  

def limpar_tela():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def jogo(palavras):
    
    palavra = random.choice(palavras)
    chances = 6
        
    letras_certas = ['_' for letra in palavra]
    letras_erradas = []
    
    while chances > 0:
        tentativa = input(f"""
XXXXXXXXX Acerte a palavra XXXXXXXXX
                             
{"".join(letras_certas)}    
                                               
Letras erradas: {", ".join(letras_erradas)}

voçê tem: {chances} tentativas
""").lower()
        
        if tentativa in palavra and tentativa not in letras_certas:
            limpar_tela()
            for i, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_certas[i] = letra
        
        elif tentativa in letras_certas:
            limpar_tela()
            print('\nVoçê já digitou essa letra!')

        elif tentativa in letras_erradas:
            limpar_tela()
            print('\nVoçê já digitou essa letra!')
        
        else:
            limpar_tela()
            letras_erradas.append(tentativa)
            chances -= 1
        
        if "_" not in letras_certas:
            limpar_tela()
            print(f'\nVoçê venceu!, a palavra era {palavra}')
            break
    if chances == 0:
        print(f"voçê perdeu!, a palavra era: {palavra}")

def adicionar_palavra(palavras):
    while True:
        nova_palavra = input("""
========Adicionando========
*digite 'q' se quiser sair

Palavra: """)
        if nova_palavra.lower() == "q":
            limpar_tela()
            return palavras
        
        elif nova_palavra not in palavras and nova_palavra != "":
            palavras.append(nova_palavra)
            limpar_tela()
            print(f'{nova_palavra} adicionada!')
            
        
        elif nova_palavra == "":
            limpar_tela()
            print("Digite algo primeiro!")
        
def exibindo_palavras(palavras):
    opcao = input(f"""
========Palavras=========
{"\n".join(palavras)}
=========================
Digite 'q' se quiser sair 
""").lower()
    if opcao == "q":
        limpar_tela()
        print()
    else:
        limpar_tela()
        print("Opção Inválida!")       
  

while True:
    escolha = input("""
============Menu============
[a] Jogar
[s] Adicionar novas palavras
[d] Ver palavras existentes
============================
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
    
    else:
        print("Opção Inválida!")