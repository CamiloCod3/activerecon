import logging

def generate_report(target, results, output_file):
    """
    Generates a well-formatted Markdown report from the scan results.
    """
    logging.info(f"Generating report to: {output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        # Header
        f.write(f"# Active Recon Report\n\n")
        f.write(f"**Target:** {target}\n")
        f.write(f"**Host Status:** {results.get('status', {}).get('state', 'Unknown')}\n")
        f.write("---\n\n")

        # Scan Info Section
        f.write("## Scan Information\n\n")
        scan_info = results.get("scan_info", {})
        f.write(f"- **Protocol:** {scan_info.get('protocol', 'N/A')}\n")
        f.write(f"- **Ports Scanned:** {scan_info.get('numservices', 'N/A')}\n")
        f.write("---\n\n")

        # Ports Section
        f.write("## Open Ports\n\n")
        ports = results.get("ports", [])
        if ports:
            for port in ports:
                f.write(f"- **Port:** {port['portid']}/{port['protocol']} - **State:** {port['state']} - **Service:** {port['service']}\n")
        else:
            f.write("No open ports found.\n")
        f.write("---\n\n")
