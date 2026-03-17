# Servidor
import socket

HOST = "0.0.0.0"
PORT = 2018

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("[server] Aguardando jogador 1")
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[server] OK. Você é o jogador 1".encode())
    print("[server] Aguardando jogador 2")
    conn_2, addr_2 = s.accept()
    conn_2.sendall("[server] OK. Você é o jogador 2".encode())

    pontuacao_j1 = 0
    pontuacao_j2 = 0
    
    while pontuacao_j1 == 3 or pontuacao_j2 == 3:

        while True:
            conn_1.sendall("[server] Faça sua jogada: ".encode())
            print("[server] Aguardando jogador 1 jogar")
            jogada_j1 = conn_1.recv(1024).decode()
            print("Jogada do jogador 1: ", jogada_j1)

            conn_2.sendall("[server] Faça sua jogada: ".encode())
            print("[server] Aguardando jogador 2 jogar")
            jogada_j2 = conn_2.recv(1024).decode()
            print("Jogada do jogador 2: ", jogada_j2)

            if jogada_j1 == jogada_j2:
                vencedor = "empate"
            else:
                if jogada_j1 == "pedra":
                    if jogada_j2 == "tesoura":
                        vencedor = "Jogador 1 venceu"
                        if pontuacao_j2 > 0:
                            pontuacao_j1+=1
                            pontuacao_j2=0
                    else:
                        vencedor = "Jogador 2 venceu"
                        if pontuacao_j1 > 0:
                            pontuacao_j2+=1
                            pontuacao_j1=0



                if jogada_j1 == "tesoura":
                    if jogada_j2 == "papel":
                        vencedor = "Jogador 1 venceu"
                        if pontuacao_j2 > 0:
                            pontuacao_j1+=1
                            pontuacao_j2=0
                    else:
                        vencedor = "Jogador 2 venceu"
                        if pontuacao_j1 > 0:
                            pontuacao_j2+=1
                            pontuacao_j1=0
                    
                if jogada_j1 == "papel":
                    if jogada_j2 == "pedra":
                        vencedor = "Jogador 1 venceu"
                        if pontuacao_j2 > 0:
                            pontuacao_j1+=1
                            pontuacao_j2=0
                    else:
                        vencedor = "Jogador 2 venceu"
                        if pontuacao_j1 > 0:
                            pontuacao_j2+=1
                            pontuacao_j1=0

            conn_1.sendall(vencedor.encode())
            conn_2.sendall(vencedor.encode())

        
    