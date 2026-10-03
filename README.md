# Pedra, Papel, Tesoura, Lagarto e Spock

Jogo de terminal em Python: você contra o computador na versão estendida de Pedra, Papel e Tesoura.

## O que faz

- Menu numerado com 5 opções: `1` Pedra, `2` Papel, `3` Tesoura, `4` Lagarto, `5` Spock.
- O computador escolhe uma opção aleatória (`random.randint`).
- Mostra o resultado colorido no terminal (vitória em verde, derrota em vermelho, empate).
- Ao fim de cada rodada pergunta `Deseja jogar novamente? [S/N]`.
- Ao sair, exibe o placar final (Player x AI).
- Entradas inválidas (texto ou número fora de 1–5) são tratadas e o jogo pede de novo.

### Regras

| Opção | Vence de |
|---|---|
| Pedra | Tesoura, Lagarto |
| Papel | Pedra, Spock |
| Tesoura | Papel, Lagarto |
| Lagarto | Papel, Spock |
| Spock | Pedra, Tesoura |

## Como rodar

```bash
python main.py
```

## Requisitos

- Python 3.6 ou superior
- Terminal com suporte a cores ANSI (Windows Terminal, terminais Linux/macOS)
- Sem dependências externas

## Estrutura

```
main.py   # jogo completo
```
