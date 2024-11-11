import socket as sock
import threading

def broadcast(lista_clientes):
    pass

def recebe_dados(sock_conn, ender):
    #Antes de entrarmos no loop, vamos receber o nome
    nome = sock_conn.recv(50).decode()
    print(f"Conexão com sucesso com {nome} - {ender}")
    while True:
            try:
                mensagem = sock_conn.recv(1024).decode()
                print(f'{nome} >> {mensagem}')
            except:
                print("Erro ao receber mensagem..., fechando conexão")
                sock_conn.close()
                return


HOST = '127.0.0.1' #esse ip posteriormente será o IP do servidor
PORTA = 9999

#sock.AF_INET : Ipv4
#sock.SOCK_STREAM : TCP

#criamos o socket de conexão com o servidor
sock_server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
#bind => linkar HOST a PORTA

sock_server.bind((HOST, PORTA))
#servidor entra no modo de escuta

sock_server.listen()
print(f'O servidor {HOST}:{PORTA} está aguardando conexões..')

#O accept retorna o socket de conexão com cliente
#e retorna o endereço do cliente
#Criamos nosso loop principal para aceitar vários clientes

while True:
    conn, ender = sock_server.accept()
    print(f'Conexão com o cliente: {ender}')
    #Conexão com sucesso, vamos continuar o programa
    #Criamos um loop para recebimento de mensagem
    threadCliente = threading.Thread(target = recebe_dados, args = (conn, ender))
    threadCliente.start()
    


    