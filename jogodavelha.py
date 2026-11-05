# Inicializa o placar separado para cada tamanho de tabuleiro.
vitorias_x_3 = 0
vitorias_o_3 = 0
empates_3 = 0  

vitorias_x_5 = 0
vitorias_o_5 = 0
empates_5 = 0

# Controla a repeticao do menu ate a opcao de sair.
opcao_menu = 0

# Exibe o menu e recebe a opcao do usuario.
while opcao_menu != 4:
	print("\n=== JOGO DA VELHA ===")
	print("1 - Jogar em 3x3")
	print("2 - Jogar em 5x5")
	print("3 - Ver placar")
	print("4 - Sair")

	entrada_menu = input("Escolha uma opcao: ")
	iniciar_partida = 0

	# Define o tamanho da partida ou executa uma opcao do menu.
	if entrada_menu == "1":
		tamanho = 3
		iniciar_partida = 1
	elif entrada_menu == "2":
		tamanho = 5
		iniciar_partida = 1
	elif entrada_menu == "3":
		# Mostra as vitorias e os empates acumulados.
		print("\n=== PLACAR ===")
		print("Tabuleiro 3x3:")
		print("Vitorias de X: " + str(vitorias_x_3))
		print("Vitorias de O: " + str(vitorias_o_3))
		print("Empates: " + str(empates_3))
		print("\nTabuleiro 5x5:")
		print("Vitorias de X: " + str(vitorias_x_5))
		print("Vitorias de O: " + str(vitorias_o_5))
		print("Empates: " + str(empates_5))
	elif entrada_menu == "4":
		opcao_menu = 4
	else:
		print("Opcao invalida. Digite 1, 2, 3 ou 4.")
		
# Cria o tabuleiro escolhido e define quantas pecas vencem.
	if iniciar_partida == 1:
		if tamanho == 3:
			tabuleiro = [
				[" ", " ", " "],
				[" ", " ", " "],
				[" ", " ", " "]
			]
			quantidade_vitoria = 3
			
else:
			tabuleiro = [
				[" ", " ", " ", " ", " "],
				[" ", " ", " ", " ", " "],
				[" ", " ", " ", " ", " "],
				[" ", " ", " ", " ", " "],
				[" ", " ", " ", " ", " "]
			]
			quantidade_vitoria = 4

		# Prepara o estado inicial da partida.
		vencedor = ""
		jogador = "X"
		casas_vazias = tamanho * tamanho

# Mantem a partida ativa enquanto houver jogadas e ninguem vencer.
		while vencedor == "" and casas_vazias > 0:
			# Desenha o tabuleiro e identifica o jogador da vez.
			print("\n   ", end="")
			for coluna in range(tamanho):
				print(str(coluna + 1) + "   ", end="")
			print()

			for linha in range(tamanho):
				print(str(linha + 1) + " ", end="")
				for coluna in range(tamanho):
					print("| " + tabuleiro[linha][coluna] + " ", end="")
				print("|")
				print("  ", end="")
				for coluna in range(tamanho):
					print("----", end="")
				print("-")

			print("Vez do jogador " + jogador)




