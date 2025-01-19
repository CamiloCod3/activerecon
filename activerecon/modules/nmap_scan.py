import subprocess
import logging
import xml.etree.ElementTree as ET

def run_nmap_scan(target, scan_command):
    """
    Runs an Nmap scan with XML output and parses the results.
    """
    command = f"nmap {scan_command} -oX - {target}"
    try:
        logging.info(f"Executing Nmap scan: {command}")
        result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Parse the XML output
        xml_output = result.stdout
        root = ET.fromstring(xml_output)

        # Extract useful data
        scan_results = {
            "target": target,
            "ports": [],
            "status": root.find(".//status").attrib,
            "scan_info": root.find("scaninfo").attrib,
            "host": root.find("host/address").attrib.get("addr", "Unknown"),
        }

        # Collect port information
        for port in root.findall(".//port"):
            port_data = {
                "portid": port.attrib.get("portid"),
                "protocol": port.attrib.get("protocol"),
                "state": port.find("state").attrib.get("state"),
                "service": port.find("service").attrib.get("name", "Unknown"),
            }
            scan_results["ports"].append(port_data)

        return scan_results
    except Exception as e:
        logging.error(f"Failed to execute Nmap scan: {e}")
        return {}
