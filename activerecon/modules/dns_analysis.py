import dns.resolver
import logging

def analyze_dns(target):
    """
    Analyzes DNS records for the target.
    """
    logging.info("Starting DNS analysis")
    dns_records = {}
    try:
        dns_records['A'] = [answer.address for answer in dns.resolver.resolve(target, "A")]
        dns_records['MX'] = [answer.exchange.to_text() for answer in dns.resolver.resolve(target, "MX")]
        dns_records['TXT'] = [answer.to_text() for answer in dns.resolver.resolve(target, "TXT")]
    except Exception as e:
        logging.error(f"DNS analysis failed: {e}")
    return dns_records

