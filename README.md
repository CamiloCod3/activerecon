# ActiveRecon

ActiveRecon is an automated reconnaissance tool that combines Nmap scanning, DNS analysis, and HTTP analysis.

## Features

- **Nmap Scanning**: Execute various predefined profiles for fast and comprehensive port scanning.
- **DNS Analysis**: Query A, MX, and TXT records for a target.
- **HTTP Analysis**: Identify HTTP services and fetch basic details.

## Installation

### Prerequisites

- **Python 3.6 or later**
- **Nmap**: Install Nmap using the following command:

    ```bash
    sudo apt-get install nmap
    ```

### Install from GitHub

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/activerecon.git
    cd activerecon
    ```

2. Install the package with pip:

    ```bash
    pip install .
    ```

## Usage

Once installed, you can run the tool as a command-line utility:

```bash
activerecon --target <IP_OR_DOMAIN> --scan-profile <PROFILE> --output <OUTPUT_FILE>
