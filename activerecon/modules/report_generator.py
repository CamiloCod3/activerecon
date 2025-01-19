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
        f.write(f"**Date:** {results.get('date', 'N/A')}\n")
        f.write(f"**Scan Duration:** {results.get('duration', 'N/A')} seconds\n\n")
        f.write("---\n\n")

        # Summary Section
        f.write("## **Summary**\n\n")
        f.write(f"- **Open Ports:** {results.get('open_ports', 0)}\n")
        f.write(f"- **Vulnerabilities Found:** {results.get('vulnerabilities', 0)}\n")
        f.write(f"- **Host Status:** {results.get('status', 'Unknown')}\n\n")
        f.write("---\n\n")

        # Nmap Scan Section
        f.write("## **Nmap Scan**\n\n")
        f.write("### Command Executed:\n")
        f.write("```bash\n")
        f.write(f"{results.get('nmap_command', 'N/A')}\n")
        f.write("```\n\n")

        f.write("### Ports Scanned:\n")
        f.write(f"- **Protocol:** {results.get('protocol', 'N/A')}\n")
        f.write(f"- **Number of Services Scanned:** {results.get('num_services', 'N/A')}\n")
        f.write(f"- **Ports:** {results.get('ports', 'N/A')}\n\n")

        f.write("### Results:\n")
        f.write(f"- **Status:** {results.get('port_status', 'N/A')} (Reason: {results.get('port_reason', 'N/A')})\n")
        f.write(f"- **Total Open Ports:** {results.get('open_ports', 0)}\n")
        f.write(f"- **Filtered Ports Count:** {results.get('filtered_ports', 'N/A')}\n\n")
        f.write("---\n\n")

        # DNS Analysis Section
        f.write("## **DNS Analysis**\n\n")
        dns_analysis = results.get('dns_analysis', {})
        if dns_analysis:
            for record_type, records in dns_analysis.items():
                f.write(f"- **{record_type} Records:** {records}\n")
        else:
            f.write("No DNS records found for the target.\n")
        f.write("\n---\n\n")

        # Run Statistics Section
        f.write("## **Run Statistics**\n\n")
        f.write(f"- **Hosts Scanned:** {results.get('hosts_scanned', 'N/A')}\n")
        f.write(f"- **Nmap Exit Status:** {results.get('exit_status', 'N/A')}\n")
        f.write(f"- **Scan Completed At:** {results.get('scan_end_time', 'N/A')}\n")
