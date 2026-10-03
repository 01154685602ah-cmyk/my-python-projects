import requests
from rich.console import Console
from rich.table import Table

console = Console()
city = console.input("[bold cyan]City (English): [/]")

try:
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url, timeout=10).json()
    now = data["current_condition"][0]

    table = Table(title=f"Weather in {city}", border_style="cyan")
    table.add_column("Item", style="yellow")
    table.add_column("Value", style="bold green")

    table.add_row("Temp", now["temp_C"] + " C")
    table.add_row("Feels like", now["FeelsLikeC"] + " C")
    table.add_row("Humidity", now["humidity"] + " %")
    table.add_row("Wind", now["windspeedKmph"] + " km/h")
    table.add_row("Status", now["weatherDesc"][0]["value"])

    console.print(table)
except Exception:
    console.print("[bold red]Could not get weather.[/]")
