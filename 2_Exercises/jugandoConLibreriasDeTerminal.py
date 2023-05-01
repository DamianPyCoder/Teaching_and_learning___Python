print()
# barra de tareas que se carga
from tqdm import tqdm
for i in tqdm(range(25600000)):
    pass



print()
# pip install tabulate
from tabulate import tabulate
data = [
    ["Barcelona", 66, "Europe"],
    ["Berlin", 32, "Europe"],
    ["Bangkok", 45, "Asia"]
]
print(tabulate(data, headers=["City", "Random number", "Continent"]))
print()





print()
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.progress import Progress
from rich.live import Live
from rich.bar import Bar

# Crear una consola
console = Console()


# Tabla con diferentes estilos
table = Table(title="Info", show_header=True, header_style="bold blue")
table.add_column("ID", style="dim", width=12)
table.add_column("Nombre")
table.add_column("Apellidos")
table.add_column("Edad", justify="right")
table.add_row("1", "Marc", "Lpez", "18")
table.add_row("2", "David", "Srez", "28")
table.add_row("3", "Maite", "Rguez", "41")
console.print(table)

# Panel con título y estilo
panel = Panel("Notas importantes que contiene el panel...", title="Título", style="bold green")
console.print(panel)
print()

# Barra de progreso
with Progress() as progress:
    task = progress.add_task("[green]Descargando archivo...", total=100)
    while not progress.finished:
        progress.advance(task)
console.print("[green]Descarga completada[/green]")


