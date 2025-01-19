import argparse
import logging

from .modules.nmap_scan import run_nmap_scan
from .modules.http_enum import analyze_http
from .modules.dns_analysis import analyze_dns
from .modules.report_generator import generate_report
from .modules.config_loader import load_config


# Load configuration
CONFIG = load_config()

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    parser = argparse.ArgumentParser(description="Active Recon Tool")
    parser.add_argument("--target", required=True, help="Target IP or domain")
    parser.add_argument("--output", default="report.md", help="Output file for the report")

    # Här antar vi att config.yaml innehåller en dictionary 'scan_profiles'
    scan_profile_choices = list(CONFIG["scan_profiles"].keys())

    parser.add_argument("--scan-profile",
                        default="fast",
                        choices=scan_profile_choices,
                        help="Choose a pre-defined Nmap profile from config.yaml")

    args = parser.parse_args()

    # Hämta vald profil
    chosen_profile = args.scan_profile
    scan_command = CONFIG["scan_profiles"][chosen_profile]

    target = args.target
    results = {}

    logging.info(f"Starting automated recon on target: {target}")
    logging.info(f"Using scan profile: {chosen_profile} ({scan_command})")

    # Step 1: Kör Nmap
    nmap_results = run_nmap_scan(target, scan_command)
    results['Nmap Scan'] = nmap_results

    # Step 2: Identifiera ev. HTTP-portar
    http_ports = [
        port["portid"]
        for port in nmap_results.get("nmaprun", {}).get("host", {}).get("ports", {}).get("port", [])
        if port.get("service", {}).get("@name") in ["http", "https"]
    ]

    if http_ports:
        logging.info("HTTP ports found, running HTTP analysis.")
        results['HTTP Analysis'] = analyze_http(target, CONFIG, http_ports)

    # Step 3: DNS-analys
    logging.info("Running DNS analysis.")
    results['DNS Analysis'] = analyze_dns(target)

    # Step 4: Generera rapport
    generate_report(target, results, args.output)
    logging.info(f"Recon completed successfully! Report saved to {args.output}")


if __name__ == "__main__":
    main()
