"""Biblioteca que gera números aleatórios"""
import random

"""Função jogar jogo"""
def jogar_jogo():
    
    """gera um número aleatório e inicia as variáveis"""
    numero_secreto = random.randint(0,10)

    """Inicializa a pontuação máxima e mínima"""
    pontuacao_maxima = 100
    pontuacao_minima = 10

    """Inicializa a pontuação do jogador"""
    pontuacao_do_jogador = 0

    """Mensagem de boas vindas"""
    print("\nBem-vindo ao jogo do acerte o número")
    print("O computador escolheu um número entre 0 e 10.")


    """Loop para 5 tentativas"""
    for tentativa in range(1, 6):
        try:
            """captura de tentativa do usuário"""
            tentativa_usuario = int(input(f"\nTentativa {tentativa}:Digite sua suposição "))

            """Verificando se a suposição está dentro da faixa permitida"""
            if tentativa_usuario < 0 or tentativa_usuario > 10:
                print("Por Favor digite um número entre 0 e 10")
                continue
            
            """Verificação se a suposição  está correta"""
            if tentativa_usuario == numero_secreto:
                print(f"Parabéns você acertou o número {numero_secreto}.")
                pontuacao_do_jogador = pontuacao_maxima - (tentativa -1) * 10
                print(f"Sua pontuação : {pontuacao_do_jogador} pontos")
                break
            else:
                if tentativa < 5:
                    print("Tente novamente")          
        except ValueError:
            print("Por favor digite um número válido")   


        """Mensagem se o jogador não acertar após 5 tentativas"""

        if tentativa_usuario != numero_secreto:
            print(f"Você não acertou. O número correto era {numero_secreto} ")
            print("Sua pontuação: 0 pontos")

        return pontuacao_do_jogador

"""definição da função main e loop principal do jogo"""
def main(): 
    jogar_novamente = True

    while jogar_novamente:
         pontuação = jogar_jogo()

         opcao = input("Deseja jogar novamente? (S para sim, qualquer outra tecla para não):").upper()
         if opcao != 'S':
            jogar_novamente = False
            print("Obrigado por jogar! Sua pontuação final:", pontuação)

if __name__ == "__main__":
    main()
             

