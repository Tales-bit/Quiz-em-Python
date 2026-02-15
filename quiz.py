pontos = []
for i in range (0, 1):
    print("====================================")
    print("    Quiz de Matematica em Python")
    print("====================================\n")
    print("Para comecarmos, digite a quantidade de jogadores:", end=" ")
    nj = int(input())
    for i in range(nj):
        pontos.append(0)
    print("\n")

    with open("perguntas.txt", "r") as arq1, open("gabarito.txt", "r") as arq2:
        # O "3" é o total de questões 
        for _ in range(3):
            respostas = []
            for _ in range(8):
                linha = arq1.readline().rstrip()
                print(linha)
            for _ in range(nj):
                n = input()
                respostas.append(n)

            # lê só a resposta da questão atual
            arq2.readline() # ignora "Questao X"
            linha = arq2.readline().strip().upper()
            for i in range(nj):
                if respostas[i].upper() == linha:
                    print("jogador {} acertou!".format(i+1))
                    pontos[i] = pontos[i]+1