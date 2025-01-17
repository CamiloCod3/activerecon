import requests

def analyze_http(target, ports):
    """
    Analyserar HTTP-tjänster och returnerar headers samt statuskoder.
    """
    http_ports = [p for p in ports if p.startswith("http")]
    results = []

    for port in http_ports:
        url = f"http://{target}:{port}"
        try:
            response = requests.get(url, timeout=5)
            results.append({"url": url, "status": response.status_code, "headers": dict(response.headers)})
        except Exception as e:
            results.append({"url": url, "error": str(e)})

    return results