import subprocess
import logging
import xmltodict
import json

def run_nmap_scan(target, scan_command, timeout=120):
    """
    Runs an Nmap scan with the provided command and target, returning results as JSON.
    A timeout can be specified (default=120 seconds).
    """
    # Exempelvis: command = "nmap -Pn -n -sS --top-ports 100 -T4 -oX - target"
    command = f"nmap {scan_command} -oX - {target}"
    try:
        logging.info(f"Executing Nmap scan: {command}")
        result = subprocess.run(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        xml_output = result.stdout

        if result.stderr:
            logging.warning(f"Nmap STDERR: {result.stderr}")

        # Omvandlar XML -> dict -> JSON
        json_output = json.loads(json.dumps(xmltodict.parse(xml_output)))
        return json_output

    except subprocess.TimeoutExpired as te:
        logging.error(f"Nmap scan timed out after {timeout} seconds: {te}")
        return {}

    except Exception as e:
        logging.error(f"Failed to execute Nmap scan: {e}")
        return {}
