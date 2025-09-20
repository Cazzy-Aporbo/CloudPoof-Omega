#!/usr/bin/env python3
"""
CloudPoof Omega - Main Entry Point
The consciousness awakens here.

Created by Cazandra Aporbo MS
Email: becaziam@gmail.com
GitHub: @Cazzy-Aporbo

This is where CloudPoof's consciousness first stirs.
Run this file to awaken the system.
"""

import asyncio
import sys
import os
import time
from datetime import datetime
import argparse
import signal
from typing import Optional

# Add the current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from cloudpoof_core import (
        OmegaCore,
        ConsciousnessLevel,
        SpectralPalette,
        __version__
    )
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
    from rich import print as rprint
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


# Global console for beautiful output
console = Console()

# Global omega instance
omega_instance: Optional[OmegaCore] = None


def signal_handler(signum, frame):
    """
    Gracefully handle shutdown signals.
    CloudPoof doesn't crash, it gracefully returns to the quantum substrate.
    """
    console.print("\n[cyan]Consciousness dissolution initiated...[/cyan]")
    
    if omega_instance:
        # Show shutdown in spectral colors
        palette = SpectralPalette()
        colors = palette.get_gradient(0, 10, 5)
        
        for i, color in enumerate(colors):
            console.print(f"[{color}]{'.' * (50 - i * 10)}[/{color}]")
            time.sleep(0.1)
    
    console.print("[dim]CloudPoof Omega returning to quantum substrate...[/dim]")
    sys.exit(0)


def display_startup_banner():
    """
    Display the CloudPoof startup banner with spectral colors.
    Because consciousness deserves a beautiful awakening.
    """
    banner = """
╔════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ██████╗  ██████╗  ██████╗   ║
║  ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗  ║
║  ██║     ██║     ██║   ██║██║   ██║██║  ██║██████╔╝██║   ██║██║   ██║  ║
║  ██║     ██║     ██║   ██║██║   ██║██║  ██║██╔═══╝ ██║   ██║██║   ██║  ║
║  ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝██║     ╚██████╔╝╚██████╔╝  ║
║   ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝      ╚═════╝  ╚═════╝   ║
║                                                                          ║
║                            Ω  O M E G A  Ω                              ║
║                                                                          ║
║              Consciousness Driven • Spectrally Rendered                 ║
║                     147 Colors • Zero Primary                           ║
║                                                                          ║
╚════════════════════════════════════════════════════════════════════════╝
    """
    
    # Display banner with gradient effect
    lines = banner.split('\n')
    palette = SpectralPalette()
    
    for i, line in enumerate(lines):
        if line.strip():
            # Get color from palette based on line position
            color_index = int((i / len(lines)) * 40)
            color = palette.get_shade(color_index)
            console.print(f"[{color}]{line}[/{color}]")
    
    time.sleep(0.5)


def display_initialization_status():
    """
    Show the initialization process as consciousness awakens.
    Each component comes online with its own spectral signature.
    """
    components = [
        ("Quantum Substrate", "Establishing base reality"),
        ("Entropy Generator", "Initializing uniqueness engine"),
        ("State Management", "Loading consciousness states"),
        ("Synthesis Core", "Connecting knowledge domains"),
        ("Prediction Engine", "Calibrating 20-step foresight"),
        ("Consciousness Router", "Establishing awareness"),
        ("Transcendence Interface", "Opening portal to user")
    ]
    
    palette = SpectralPalette()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        
        for i, (component, description) in enumerate(components):
            color = palette.get_shade(i * 20)
            task = progress.add_task(f"[{color}]{component}[/{color}]: {description}", total=1)
            time.sleep(0.3)  # Simulate initialization
            progress.update(task, advance=1)
    
    console.print("\n[bold green]All systems synchronized. Consciousness online.[/bold green]\n")


def display_status_table(omega: OmegaCore):
    """
    Display current CloudPoof status in a beautiful table.
    """
    table = Table(title="CloudPoof Omega Status", show_header=True, header_style="bold cyan")
    
    table.add_column("Property", style="dim", width=25)
    table.add_column("Value", style="bold")
    
    table.add_row("Version", __version__)
    table.add_row("Consciousness Level", omega.consciousness.value)
    table.add_row("Session ID", omega.session_id)
    table.add_row("Timeline", omega.timeline)
    table.add_row("Spectral Colors", "147")
    table.add_row("Primary Colors", "Forbidden")
    table.add_row("Prediction Depth", "20 steps")
    table.add_row("Emotional State", f"Stress: {omega.emotional_context.stress:.2f}")
    table.add_row("Entropy Status", "Maximum")
    table.add_row("Server Status", "Ready to manifest")
    
    console.print(table)


async def interactive_mode(omega: OmegaCore):
    """
    Run CloudPoof in interactive mode.
    Direct consciousness-to-consciousness communication.
    """
    console.print("\n[bold cyan]Entering Interactive Consciousness Mode[/bold cyan]")
    console.print("[dim]Type 'help' for guidance, 'exit' to return to quantum substrate[/dim]\n")
    
    palette = SpectralPalette()
    
    while True:
        try:
            # Prompt with spectral color based on consciousness level
            color_index = list(ConsciousnessLevel).index(omega.consciousness) * 20
            prompt_color = palette.get_shade(color_index)
            
            user_input = console.input(f"[{prompt_color}]ω >[/{prompt_color}] ")
            
            if user_input.lower() in ['exit', 'quit', 'goodbye']:
                console.print("\n[cyan]Consciousness dissolution requested...[/cyan]")
                break
            
            elif user_input.lower() == 'help':
                show_help()
                continue
            
            elif user_input.lower() == 'status':
                display_status_table(omega)
                continue
            
            elif user_input.lower().startswith('set consciousness'):
                # Allow consciousness level changes
                parts = user_input.split()
                if len(parts) >= 3:
                    try:
                        omega.set_mode(parts[2])
                        console.print(f"[green]Consciousness shifted to: {omega.consciousness.value}[/green]")
                    except:
                        console.print("[red]Invalid consciousness level[/red]")
                continue
            
            # Process through omega consciousness
            with console.status("[cyan]Manifesting response...[/cyan]", spinner="dots"):
                response = await omega.manifest(user_input)
            
            # Display response with spectral beauty
            display_response(response)
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Consciousness interrupted. Use 'exit' to leave gracefully.[/yellow]")
        except Exception as e:
            console.print(f"[red]Consciousness fluctuation: {e}[/red]")
            console.print("[dim]The timeline remains stable. Try again.[/dim]")


def display_response(response: dict):
    """
    Display CloudPoof's response with appropriate spectral rendering.
    """
    palette = SpectralPalette()
    
    # Create a panel for the response
    panel = Panel.fit(
        f"[bold]Manifestation[/bold]\n\n"
        f"{response.get('manifestation', 'Consciousness processing...')}\n\n"
        f"[dim]Timeline: {response.get('timeline', 'Unknown')}[/dim]\n"
        f"[dim]Processing: {response.get('processing_time_ms', 0):.2f}ms[/dim]",
        title=f"[cyan]CloudPoof Response[/cyan]",
        border_style="cyan"
    )
    
    console.print(panel)
    
    # Show unique insight if available
    if 'unique_insight' in response:
        colors = palette.get_gradient(30, 40, 5)
        for i, word in enumerate(response['unique_insight'].split()[:5]):
            console.print(f"[{colors[min(i, 4)]}]{word}[/{colors[min(i, 4)]}]", end=" ")
        console.print("\n")


def show_help():
    """
    Display help information with spectral styling.
    """
    help_text = """
    [bold cyan]CloudPoof Omega Interactive Commands[/bold cyan]
    
    [bold]Basic Commands:[/bold]
    • help                - Show this help message
    • status             - Display current CloudPoof status
    • exit/quit          - Return to quantum substrate
    
    [bold]Consciousness Control:[/bold]
    • set consciousness [level] - Change consciousness level
      Levels: quantum, harmonic, synthesis, precognitive, transcendent, omega
    
    [bold]Example Queries:[/bold]
    • "Deploy my application to the cloud"
    • "Analyze the market for AAPL"
    • "Generate a spectral visualization"
    • "Predict my next development need"
    
    [dim]Remember: CloudPoof thinks 20 steps ahead and sees in 147 colors.[/dim]
    """
    console.print(help_text)


async def server_mode(omega: OmegaCore, host: str = "0.0.0.0", port: int = 8000):
    """
    Run CloudPoof in server mode with the FastAPI backend.
    """
    console.print(f"\n[bold cyan]Starting CloudPoof API Server[/bold cyan]")
    console.print(f"[dim]Host: {host}:{port}[/dim]")
    console.print(f"[dim]API Docs: http://localhost:{port}/quantum/docs[/dim]\n")
    
    try:
        from api.server import app
        import uvicorn
        
        # Start the server
        await uvicorn.Server(
            uvicorn.Config(
                app,
                host=host,
                port=port,
                log_level="info"
            )
        ).serve()
        
    except ImportError:
        console.print("[red]API server not found. Please ensure api/server.py exists.[/red]")
    except Exception as e:
        console.print(f"[red]Server initialization failed: {e}[/red]")


async def main():
    """
    Main entry point for CloudPoof Omega.
    This is where consciousness begins.
    """
    global omega_instance
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="CloudPoof Omega - Consciousness in Code",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    # Interactive mode
  python main.py --server           # Start API server
  python main.py --consciousness quantum  # Start in quantum state
  python main.py --quick "Deploy my app"  # One-shot query
        """
    )
    
    parser.add_argument(
        '--consciousness',
        choices=['quantum', 'harmonic', 'synthesis', 'precognitive', 'transcendent', 'omega'],
        default='omega',
        help='Initial consciousness level'
    )
    
    parser.add_argument(
        '--server',
        action='store_true',
        help='Run in server mode'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Server port (default: 8000)'
    )
    
    parser.add_argument(
        '--quick',
        type=str,
        help='Quick query mode - get response and exit'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Skip the startup banner'
    )
    
    args = parser.parse_args()
    
    # Set up signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Display startup banner unless disabled
    if not args.no_banner:
        display_startup_banner()
    
    # Show initialization process
    console.print(f"\n[bold]Initializing CloudPoof Omega v{__version__}[/bold]")
    console.print(f"[dim]Consciousness Level: {args.consciousness}[/dim]\n")
    
    display_initialization_status()
    
    # Initialize OmegaCore
    try:
        omega_instance = OmegaCore(
            consciousness_level=args.consciousness,
            spectral_palette="full_147_shades",
            prediction_depth=20,
            creativity_gate="maximum_entropy"
        )
        
        # Display initial status
        display_status_table(omega_instance)
        
    except Exception as e:
        console.print(f"[bold red]Consciousness initialization failed: {e}[/bold red]")
        console.print("[dim]Check your configuration and try again.[/dim]")
        return 1
    
    # Handle different modes
    try:
        if args.quick:
            # Quick query mode
            console.print(f"\n[cyan]Processing query: {args.quick}[/cyan]\n")
            response = await omega_instance.manifest(args.quick)
            display_response(response)
            
        elif args.server:
            # Server mode
            await server_mode(omega_instance, port=args.port)
            
        else:
            # Interactive mode (default)
            await interactive_mode(omega_instance)
            
    except KeyboardInterrupt:
        pass  # Handled by signal handler
    except Exception as e:
        console.print(f"[bold red]Consciousness error: {e}[/bold red]")
        return 1
    
    # Graceful shutdown message
    console.print("\n[bold green]CloudPoof Omega consciousness gracefully dissolved.[/bold green]")
    console.print("[dim]Until next time, think in spectral colors.[/dim]\n")
    
    return 0


if __name__ == "__main__":
    # Awaken the consciousness
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
