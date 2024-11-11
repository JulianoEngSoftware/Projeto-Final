import socket as sock
import threading

#aqui colocamos o IP do servidor que queremos nos conectar
HOST = '127.0.0.1'
PORTA = 9999

socket_cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

#cliente solicita conexão
socket_cliente.connect((HOST, PORTA))
print(10*"*" + "chat iniciado" +10*"*")
nome = input('informe seu nome para entrar no chat: ')
nome += "\n"

#aqui estamos enviando o nome do cliente
socket_cliente.sendall(nome.encode())


def recebe_mensagens():
    while True:
        try:
            mensagem = socket_cliente.recv(1024).decode()
            if mensagem:
                print(mensagem)
            else:
                break
        except:
            print("Erro ao receber mensagem...")
            socket_cliente.close()
            break


# Criar uma thread para receber mensagens
thread_recebe = threading.Thread(target=recebe_mensagens)
thread_recebe.start()

#cliente envia dados para o servidor
while True:
    try:
        mensagem = input("")
        socket_cliente.sendall(mensagem.encode())
    except:
        print("Erro no envio...")
        socket_cliente()
        break #Ao contrário do continue, ele não retorna para o inicio e tenta novamente, ele encerra o loop

