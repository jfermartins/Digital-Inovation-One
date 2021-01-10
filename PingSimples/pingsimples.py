import os ##importa o módulo ou biblioteca OS (integra os programas
#recursos do Sistema Operacional

print("*" * 60) ##imprimindo o * 60 vezes

ip_ou_host = input("Digite o ip ou  host a ser verificado: ")
#Criamos um pacote que vai receber do usuário im IP

print("-" * 60) ##Imprimindo o - 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##Chamando System da biblioteca OS - comando ping
# - n - num de pacotes que serão 6

print("-" * 60) ##Imprimindo o - 60 vezes