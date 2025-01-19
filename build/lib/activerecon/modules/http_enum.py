import requests
import logging

def analyze_http(target, config):
    """
    Analyzes HTTP services and returns headers and status codes.
    """
    logging.info("Starting HTTP analysis")
    results = []
    http_ports = [80, 443]  # Add more ports if needed

    for port in http_ports:
        url = f"http://{target}:{port}" if port == 80 else f"https://{target}:{port}"
        try:
            response = requests.get(url, timeout=config['http_timeout'])
            results.append({"url": url, "status": response.status_code, "headers": dict(response.headers)})
        except requests.RequestException as e:
            results.append({"url": url, "error": str(e)})

    logging.info("HTTP analysis completed.")
    return results