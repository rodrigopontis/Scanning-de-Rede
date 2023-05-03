#Necessario instalar
#sudo pip3 install python3-nmap
#sudo dnf install python3-nmap
#sudo python3 -m pip install --upgrade pip

from socket import *
from socket import gethostbyname
import nmap3
import argparse


def scan(ipAlvo, portas):
    #Comando nmap 
    nmapScan = nmap3.NmapScanTechniques()
    resultado = nmapScan.nmap_tcp_scan(ipAlvo, f'-p {portas}')
    #para cada porta do resultado do scan
    for porta in resultado[ipAlvo]['ports']:
        print(f"[*] {ipAlvo} {porta['portid']:>5}/tcp :: {porta['state'].upper()}")
    
def main():
    #Container de especificacao de argumentos ex: -H, -p
    parser = argparse.ArgumentParser()
    parser.add_argument('-H',
        help="Especifique o host do alvo",
        dest='alvo',
        required=True
    )
    parser.add_argument('-p',
        help="Especifique a(s) portas(s) (separadas por virgula)",
        dest='portas',
        required=True #argmento obrigatorio
    )
    #Retorna os valores adicionados nas variaveis
    args = parser.parse_args()
    hostAlvo = args.alvo
    portas = args.portas
    # print(hostAlvo)
    # print(portas)
    #teste = ""

    with socket(AF_INET,SOCK_STREAM) as connSkt:
        try:
            connSkt.connect((hostAlvo, int(portas)))
            ipAlvo = gethostbyname(hostAlvo)
            hostName = gethostname()


        except:
            exit(f"Nao foi possivel resolver o hostname {hostAlvo}")
        else:
            try:
                teste = f"\n Banner: {connSkt.recv(1024).decode()}"
                print(teste)
            except:
                pass

    print(f"Alvo: {hostName} | IP: {ipAlvo}")
    print("Portas :")
    scan(ipAlvo, portas)

if __name__ == "__main__":
    main()
