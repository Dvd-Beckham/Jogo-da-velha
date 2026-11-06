# Jogo da Velha em Python (3x3 e 5x5)

Jogo da velha para dois jogadores no terminal, com dois tamanhos de tabuleiro (3x3 e 5x5) e placar separado para cada um. O programa foi feito apenas com variáveis, condicionais, laços e listas (matrizes), sem funções.

## Integrantes

Neto - 01852930
Letícia - 01893799
Beckham - 01938803

## Como executar

1. Instale o Python 3 (https://www.python.org/downloads/).
2. Clone o repositório e entre na pasta do projeto.
3. Execute no terminal:

```
python jogodavelha.py
```

Em alguns sistemas o comando é `python3 jogodavelha.py`.

## Menu

```
=== JOGO DA VELHA ===
1 - Jogar em 3x3
2 - Jogar em 5x5
3 - Ver placar
4 - Sair
```

Ao terminar uma partida, o programa volta ao menu, e o placar continua acumulando enquanto o programa estiver aberto.

## Regras do jogo

- Dois jogadores, X e O, jogam alternadamente. O jogador X sempre começa.
- Em cada jogada, o jogador informa a linha e a coluna (de 1 até o tamanho do tabuleiro) da casa desejada.
- Não é possível jogar em uma casa já ocupada nem digitar uma posição fora do tabuleiro. Nesses casos, o jogo avisa e pede a jogada novamente.
- Tabuleiro 3x3: vence quem formar 3 peças seguidas na horizontal, na vertical ou na diagonal.
- Tabuleiro 5x5: vence quem formar 4 peças seguidas na horizontal, na vertical ou na diagonal.
- Se todas as casas forem preenchidas sem vencedor, a partida termina em empate.
- O placar guarda vitórias de X, vitórias de O e empates, separadamente para 3x3 e 5x5.

## Desafios escolhidos

- **Tabuleiro 5x5 com vitória por 4 peças em sequência:** a verificação de vitória usa laços que percorrem o tabuleiro e contam peças consecutivas nas quatro direções (horizontal, vertical e as duas diagonais), servindo para qualquer tamanho.
- **Placar separado por tamanho de tabuleiro:** o programa mantém contadores independentes de vitórias e empates para o 3x3 e para o 5x5, consultados pela opção 3 do menu.

## Divisão de tarefas

| Integrante | O que fez |
|---|---|
| **Neto** | Menu principal e escolha do tamanho, criação das matrizes 3x3 e 5x5, laço da partida, exibição do tabuleiro (durante e ao final da partida) |
| **Letícia** | Opção de sair e tratamento de opção inválida, leitura e validação de linha e coluna, verificação de vitória por laços nas quatro direções, contagem de peças consecutivas, alternância de jogadores |
| **Beckham** | Variáveis do placar, exibição do placar no menu, registro da jogada e bloqueio de casa ocupada, detecção de empate, exibição do resultado e atualização do placar |
