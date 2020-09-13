
def computador_escolhe_jogada(n, m):    
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m

def usuario_escolhe_jogada(n, m):
    valor = int(input("\nQuantas peças você vai tirar? "))
    while valor > m or valor <= 0 or valor > n:    
        print("Oops! Jogada inválida! Tente de novo.")
        valor = int(input("\nQuantas peças você vai tirar? "))
        
    return valor

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))
    
    valor = 0
    jogada = 0
    if (n % (m+1)) == 0:
        print("\nVocê começa!")
        jogada = 1 #Vez do usuario
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 #Ponto para o computador
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1 #Ponto para o usuario
                
    else:
        print("\nComputador começa!")
        jogada = 2 #Vez do computador
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 #Ponto para o computador
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1 #Ponto para o usuario

def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0
    
    while quantidade_partida < 4:
        print("**** Rodada", quantidade_partida ,"****\n")
        if partida() == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        quantidade_partida = quantidade_partida + 1
        
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))    
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    else:
        if escolha == 2:
            print("\nVocê escolheu um campeonato!\n")
            campeonato()

main()
    
