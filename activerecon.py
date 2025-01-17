from modules.port_scan import run_port_scan
from modules.http_enum import analyze_http
from modules.report_generator import generate_report

def main():
    target = input("Enter target (IP/Domain): ")
    print("[*] Running port scan...")
    ports = run_port_scan(target)

    print("[*] Analyzing HTTP services...")
    http_results = analyze_http(target, ports)

    print("[*] Generating report...")
    generate_report(target, http_results)
    print("[+] Recon completed successfully!")

if __name__ == "__main__":
    main()
