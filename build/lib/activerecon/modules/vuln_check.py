def check_vulnerabilities(service, version):
    """
    Matchar tjänst och version mot en lokal databas av sårbarheter.
    """
    # Exempel på en lokal databas
    vuln_db = {
        "apache": ["2.4.49", "2.4.50"],  # Sårbara versioner
        "nginx": ["1.20.0"]
    }

    if service in vuln_db and version in vuln_db[service]:
        return f"Sårbar version hittad: {service} {version}"
    return "Ingen känd sårbarhet hittad"
