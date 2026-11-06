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

			# Repete a leitura ate receber uma posicao livre e valida.
			jogada_valida = 0
			while jogada_valida == 0:
				entrada_linha = input("Linha (1 a " + str(tamanho) + "): ")
				entrada_coluna = input("Coluna (1 a " + str(tamanho) + "): ")

				# Verifica os numeros sem usar metodos de texto.
				linha_valida = 0
				coluna_valida = 0

				if entrada_linha == "1" or entrada_linha == "2" or entrada_linha == "3":
					linha_valida = 1
				if tamanho == 5:
					if entrada_linha == "4" or entrada_linha == "5":
						linha_valida = 1

				if entrada_coluna == "1" or entrada_coluna == "2" or entrada_coluna == "3":
					coluna_valida = 1
				if tamanho == 5:
					if entrada_coluna == "4" or entrada_coluna == "5":
						coluna_valida = 1

				if linha_valida == 1 and coluna_valida == 1:
					linha = int(entrada_linha) - 1
					coluna = int(entrada_coluna) - 1
					if tabuleiro[linha][coluna] == " ":
						tabuleiro[linha][coluna] = jogador
						jogada_valida = 1
					else:
						print("Essa casa ja foi ocupada. Escolha outra.")
				else:
					print("Digite numeros validos entre 1 e " + str(tamanho) + ".")

			# Procura uma sequencia vencedora nas quatro direcoes.
			for linha in range(tamanho):
				for coluna in range(tamanho):
					if tabuleiro[linha][coluna] == jogador and vencedor == "":
						for direcao in range(1, 5):
							# Define a direcao horizontal, vertical ou diagonal.
							if direcao == 1:
								direcao_linha = 0
								direcao_coluna = 1
							elif direcao == 2:
								direcao_linha = 1
								direcao_coluna = 0
							elif direcao == 3:
								direcao_linha = 1
								direcao_coluna = 1
							else:
								direcao_linha = 1
								direcao_coluna = -1

							# Conta as pecas consecutivas nessa direcao.
							pecas_em_linha = 1
							passo = 1
							continuar_direcao = 1

							while passo < quantidade_vitoria and continuar_direcao == 1:
								proxima_linha = linha + direcao_linha * passo
								proxima_coluna = coluna + direcao_coluna * passo

								if proxima_linha >= 0 and proxima_linha < tamanho and proxima_coluna >= 0 and proxima_coluna < tamanho:
									if tabuleiro[proxima_linha][proxima_coluna] == jogador:
										pecas_em_linha += 1
									else:
										continuar_direcao = 0
								else:
									continuar_direcao = 0

								passo += 1

							if pecas_em_linha >= quantidade_vitoria:
								vencedor = jogador

			# Atualiza casas livres e alterna o jogador se nao houve vitoria.
			if vencedor == "":
				casas_vazias -= 1
				if casas_vazias > 0:
					if jogador == "X":
						jogador = "O"
					else:
						jogador = "X"

