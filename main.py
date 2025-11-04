def play(player, ai, score):
    if( 
    (player == 1 and ai == 3) or 
    (player == 3 and ai == 4) or
    (player == 4 and ai == 2) or
    (player == 2 and ai == 5) or
    (player == 5 and ai == 1) or
    (player == 1 and ai == 4) or
    (player == 4 and ai == 5) or
    (player == 5 and ai == 3) or
    (player == 3 and ai == 2) or
    (player == 2 and ai == 1)
    ):
        print("Voce \033[32mganhou!\033[0m\n")
        score[0] += 1
    elif player == ai:
        print("\033[1;0mDeu empate!\033[0m\n")
    else:
        print("Você \033[31mperdeu!\033[0m\n")
        score[1] += 1

import random
Start = True
score = [0, 0]
list_choice = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]

print("Bem vindo a Pedra, Papel, Tesoura, Lagarto e Spock!")
while(Start == True):
    print("\nDigite o numeral de sua escolha")
    print("1. Pedra\n2. Papel\n3. Tesoura\n4. Lagarto\n5. Spock\n")
    try:
        user_choice = int(input("Sua escolha: "))
    except ValueError:
        print("Digite um número inteiro!")
        user_choice = 0
    
    if (user_choice >= 1 and user_choice <= 5):
        user = list_choice[user_choice-1]
        print(f"\nVoce escolheu: {user}")
        
        game_choice = random.randint(1, 5)
        game = list_choice[game_choice-1]
        print(f"Contra: {game}\n")
        
        play(user_choice, game_choice, score)
        
        while True:
            resposta = input("Deseja jogar novamente? [S/N]: ").strip().upper()
            if resposta == 'S':
                Start = True
                break
            elif resposta == 'N':
                Start = False
                break
            else:
                print("\nOpção inválida! Digite apenas S ou N.")
    else:
        print("Opcao invalida!\n")

print("\nFim de jogo\n")
print(f"Pontuação\nPlayer: {score[0]}\nAI: {score[1]}")