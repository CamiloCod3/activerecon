from rich.console import Console
from rich.table import Table

def generate_report(target, scan_results, output_file="report.md"):
    """
    Genererar en rapport baserat på rekognosering.
    """
    console = Console()
    table = Table(title=f"Scan Report for {target}")
    table.add_column("Service", style="cyan")
    table.add_column("Details", style="green")

    for result in scan_results:
        table.add_row(result.get("service", "Unknown"), result.get("details", "N/A"))

    console.print(table)

    with open(output_file, "w") as file:
        file.write(str(table))
