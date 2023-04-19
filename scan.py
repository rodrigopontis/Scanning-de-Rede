import threading
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# da uma limpada nos alertas de log verbose


conf.verb = 0
MAX_THREADS = 25
# faz o controle da qtd de threads que estao rodando
# quando chega no maximo ele pausa a execução enquanto as threads estao rodando
semaphore = threading.BoundedSemaphore(MAX_THREADS)
# o Lock() atua como objeto de esxclusao mutua, impede que duas threads tentarem consumir o mesmo pacote
# a threads estao usando o mesmo terminal para printar (recurso compartilhado)
# regiao critica = areas que o print é chamado
lock = threading.Lock()


def scan(ip):
    # pacote icmp
    icmpPacket = IP(dst=ip, ttl=20)/ICMP()  # faz um echo request
    # print(icmpPacket)
    responsePacket = sr1(icmpPacket, timeout=1)  # recebe o echo reply
    # print(responsePacket)
    # se reply == true print(hostvivo)
    if responsePacket:
        with lock:
            print(f"[+] Host{responsePacket[IP].src} is alive")
            teste = responsePacket[IP].src
            print(teste)
            # Verificar se a porta SSH 22 esta aberta ou nao
            # Verificar se é um switchCisco Servidor Linux ou Outro
            # Obter hostname ou MAC ou nada
            # conectar ao switch

    semaphore.release()


for i in range(256):
    semaphore.acquire()
    threading.Thread(target=scan, args=(f"192.168.15.{i}",)).start()
