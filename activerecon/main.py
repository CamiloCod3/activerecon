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

    # Load scan profiles from config.yaml
    scan_profile_choices = list(CONFIG["scan_profiles"].keys())
    parser.add_argument("--scan-profile",
                        default="fast",
                        choices=scan_profile_choices,
                        help="Choose a pre-defined Nmap profile from config.yaml")

    args = parser.parse_args()

    # Fetch chosen profile
    chosen_profile = args.scan_profile
    scan_command = CONFIG["scan_profiles"][chosen_profile]

    target = args.target
    results = {}

    logging.info(f"Starting automated recon on target: {target}")
    logging.info(f"Using scan profile: {chosen_profile} ({scan_command})")

    # Step 1: Run Nmap Scan
    try:
        nmap_results = run_nmap_scan(target, scan_command)
        results['Nmap Scan'] = nmap_results
        logging.info(f"Nmap scan completed successfully. Found {len(nmap_results.get('ports', []))} ports.")
    except Exception as e:
        logging.error(f"Error during Nmap scan: {e}")
        results['Nmap Scan'] = {"error": "Nmap scan failed"}

    # Step 2: HTTP Enumeration
    http_ports = [
        port['portid'] for port in nmap_results.get('ports', [])
        if port['service'] == 'http' or port['service'] == 'https'
    ]
    if http_ports:
        try:
            logging.info(f"HTTP ports found: {http_ports}. Running HTTP analysis.")
            results['HTTP Analysis'] = analyze_http(target, CONFIG, http_ports)
        except Exception as e:
            logging.error(f"Error during HTTP analysis: {e}")
            results['HTTP Analysis'] = {"error": "HTTP analysis failed"}
    else:
        logging.info("No HTTP ports found. Skipping HTTP analysis.")

    # Step 3: DNS Analysis
    try:
        logging.info("Running DNS analysis.")
        results['DNS Analysis'] = analyze_dns(target)
    except Exception as e:
        logging.error(f"Error during DNS analysis: {e}")
        results['DNS Analysis'] = {"error": "DNS analysis failed"}

    # Step 4: Generate the Report
    try:
        generate_report(target, results, args.output)
        logging.info(f"Recon completed successfully! Report saved to {args.output}")
    except Exception as e:
        logging.error(f"Error during report generation: {e}")


if __name__ == "__main__":
    main()

