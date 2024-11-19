import socket as sock
import threading


#Lista de clientes Conectados e seus nomes
clientes = {}
enderecos = {}


def broadcast(mensagem, cliente_atual):
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                remove_cliente(cliente)
                   
def remove_cliente(cliente):
    if cliente in clientes:
        del enderecos[clientes[cliente]]
        del clientes[cliente]
        



def recebe_dados(sock_conn, ender):
    #Antes de entrarmos no loop, vamos receber o nome
    nome = sock_conn.recv(50).decode().strip()
    clientes[sock_conn] = nome
    enderecos[nome] = sock_conn
    print(f"Conexão com sucesso com {nome} - {ender}")
    broadcast(f' {nome} --Acabou de se conectar ao Chat--'.encode(), sock_conn)
    while True:
            try:
                mensagem = sock_conn.recv(1024).decode()
                if mensagem == "exit":
                    print(f'{nome} saiu do chat')
                    broadcast(f'{nome} saiu do chat.'.encode(), sock_conn)
                    sock_conn.close()
                    remove_cliente(sock_conn)
                    break
                if mensagem.startswith("/msg "):
                    _, destinatario, mensagem_privada = mensagem.split(" ", 2)
                    if destinatario in enderecos:
                        enderecos[destinatario].send(f"[Privado de {nome}]: {mensagem_privada}".encode())
                    else:
                        sock_conn.send("Usuário não encontrado.\n".encode())        
                else:
                    print(f'{nome} >> {mensagem}')
                    broadcast(f'{nome} >> {mensagem}'.encode(), sock_conn)
                    
            except:
                print("Erro ao receber mensagem..., fechando conexão")
                sock_conn.close()
                remove_cliente(sock_conn)
                break


HOST = '127.0.0.1' #esse ip posteriormente será o IP do servidor
PORTA = 9999

#sock.AF_INET : Ipv4
#sock.SOCK_STREAM : TCP

#criamos o socket de conexão com o servidor
sock_server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
#AF_INT Significa que é protocolo ipv4 (usado para endereços de ip como 192.168.1.1 e número de porta como 80). 
#SOCK_STREAM Significa que é um socket do tipo TCP, onde garante que o dados são entregues na ordem correta e sem duplicar.

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
    