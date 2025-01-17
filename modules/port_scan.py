import subprocess

def run_port_scan(target):
    """
    Kör en portskanning med nmap och returnerar resultaten som en lista.
    """
    try:
        result = subprocess.run(
            ["nmap", "-sV", "-T4", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except Exception as e:
        print(f"[!] Error running port scan: {e}")
        return None