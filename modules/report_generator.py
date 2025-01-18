import logging

def generate_report(target, results, output_file="report.md"):
    """
    Generates a report based on reconnaissance results.
    """
    logging.info("Generating report")
    with open(output_file, "w") as file:
        file.write(f"# Scan Report for {target}\n\n")
        file.write(f"## Summary\n\n")
        file.write(f"- Open Ports: {len(results.get('Port Scan', []))}\n")
        file.write(f"- Vulnerabilities Found: {len(results.get('Vulnerabilities', []))}\n\n")
        for module, data in results.items():
            file.write(f"## {module}\n\n{data}\n\n")
    logging.info(f"Report saved to {output_file}")
