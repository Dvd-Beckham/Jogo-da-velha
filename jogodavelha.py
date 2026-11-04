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
