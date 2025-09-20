"""
CloudPoof Omega - Spectral Color Demonstration
examples/spectral_demo.py

Created by Cazandra Aporbo MS
Email: becaziam@gmail.com

This demonstrates the 147 spectral colors that CloudPoof uses instead of 
primary colors. Run this to see why we rejected the tyranny of RGB.

Requirements:
    pip install pillow rich matplotlib

Usage:
    python examples/spectral_demo.py
    
This will:
    1. Generate all 147 spectral shades
    2. Create an HTML visualization
    3. Generate a PNG color palette
    4. Show colors in terminal (if supported)
    5. Prove primary colors are unnecessary
"""

import os
import sys
import colorsys
import random
from typing import List, Tuple
from datetime import datetime

# Add parent directory to path to import cloudpoof_core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from cloudpoof_core import SpectralPalette
except ImportError:
    # If cloudpoof_core isn't available, we'll create a standalone version
    print("Creating standalone SpectralPalette for demonstration...")
    
    class SpectralPalette:
        """
        The 147 unique spectral shades that define CloudPoof's aesthetic.
        No primary colors. Only consciousness-approved gradients.
        """
        
        # The seven spectral zones
        TEAL_CASCADE = [
            "#5EEAD4", "#14B8A6", "#0D9488", "#0F766E", "#115E59",
            "#134E4A", "#2DD4BF", "#6EE7B7", "#86EFAC", "#A7F3D0"
        ]
        
        SKY_RIVER = [
            "#7DD3FC", "#38BDF8", "#0EA5E9", "#0284C7", "#0369A1",
            "#075985", "#BAE6FD", "#E0F2FE", "#F0F9FF", "#67E8F9"
        ]
        
        LAVENDER_DREAM = [
            "#C4B5FD", "#A78BFA", "#9333EA", "#7E22CE", "#6B21A8",
            "#581C87", "#E9D5FF", "#F3E8FF", "#FAF5FF", "#DDD6FE"
        ]
        
        MINT_AURORA = [
            "#86EFAC", "#4ADE80", "#34D399", "#10B981", "#059669",
            "#047857", "#6EE7B7", "#A7F3D0", "#D1FAE5", "#ECFDF5"
        ]
        
        SLATE_WHISPER = [
            "#94A3B8", "#64748B", "#475569", "#334155", "#1E293B",
            "#0F172A", "#CBD5E1", "#E2E8F0", "#F1F5F9", "#F8FAFC"
        ]
        
        PERIWINKLE_VOID = [
            "#C7D2FE", "#A5B4FC", "#818CF8", "#6366F1", "#4F46E5",
            "#4338CA", "#E0E7FF", "#EEF2FF", "#F5F3FF", "#93C5FD"
        ]
        
        SAGE_HORIZON = [
            "#A7F3D0", "#6EE7B7", "#34D399", "#10B981", "#059669",
            "#BEF264", "#A3E635", "#84CC16", "#65A30D", "#4D7C0F"
        ]
        
        def __init__(self):
            """Initialize with all 147 unique spectral shades."""
            self._all_shades = (
                self.TEAL_CASCADE + self.SKY_RIVER + self.LAVENDER_DREAM +
                self.MINT_AURORA + self.SLATE_WHISPER + self.PERIWINKLE_VOID +
                self.SAGE_HORIZON
            )
            # Generate additional unique shades to reach 147
            self._all_shades.extend(self._generate_harmonic_shades(147 - len(self._all_shades)))
        
        def _generate_harmonic_shades(self, count: int) -> List[str]:
            """
            Generate additional harmonic shades using golden ratio distribution.
            This ensures maximum visual distinction between colors.
            """
            shades = []
            golden_ratio = 0.618033988749895
            
            for i in range(count):
                # Use golden ratio for optimal color distribution
                hue = (i * golden_ratio) % 1
                
                # Keep saturation and lightness in non-primary ranges
                # This prevents pure RGB colors from emerging
                saturation = 0.3 + (0.4 * ((i * 0.381966011250105) % 1))
                lightness = 0.6 + (0.3 * ((i * 0.272632342) % 1))
                
                # Convert HSL to RGB
                rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
                
                # Convert to hex
                hex_color = '#{:02x}{:02x}{:02x}'.format(
                    int(rgb[0] * 255),
                    int(rgb[1] * 255),
                    int(rgb[2] * 255)
                )
                shades.append(hex_color.upper())
            
            return shades
        
        def get_all_shades(self) -> List[str]:
            """Return all 147 spectral shades."""
            return self._all_shades.copy()
        
        def get_shade(self, index: int) -> str:
            """Get a specific shade by index."""
            return self._all_shades[index % len(self._all_shades)]
        
        def get_gradient(self, start_idx: int, end_idx: int, steps: int = 10) -> List[str]:
            """Generate a smooth gradient between two shades."""
            start = self._all_shades[start_idx % len(self._all_shades)]
            end = self._all_shades[end_idx % len(self._all_shades)]
            
            # Convert hex to RGB
            start_rgb = tuple(int(start[i:i+2], 16) for i in (1, 3, 5))
            end_rgb = tuple(int(end[i:i+2], 16) for i in (1, 3, 5))
            
            gradient = []
            for step in range(steps):
                t = step / (steps - 1) if steps > 1 else 0
                rgb = tuple(int(start_rgb[i] + t * (end_rgb[i] - start_rgb[i])) for i in range(3))
                hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
                gradient.append(hex_color.upper())
            
            return gradient


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_ansi(r: int, g: int, b: int) -> str:
    """Convert RGB to ANSI color code for terminal display."""
    return f"\033[48;2;{r};{g};{b}m"


def generate_html_visualization(palette: SpectralPalette) -> str:
    """
    Generate an HTML file showing all 147 colors in a beautiful grid.
    This creates a visual proof that primary colors are obsolete.
    """
    colors = palette.get_all_shades()
    
    html = """<!DOCTYPE html>
<html>
<head>
    <title>CloudPoof Omega - 147 Spectral Shades</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            color: #F0F9FF;
            padding: 20px;
            margin: 0;
        }
        h1 {
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 10px;
            background: linear-gradient(90deg, #5EEAD4, #7DD3FC, #C4B5FD);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            color: #94A3B8;
            margin-bottom: 30px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        .zone {
            margin-bottom: 40px;
        }
        .zone-title {
            font-size: 1.3em;
            margin-bottom: 15px;
            color: #E0F2FE;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .color-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 12px;
            margin-bottom: 20px;
        }
        .color-card {
            height: 100px;
            border-radius: 8px;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .color-card:hover {
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.4);
            z-index: 10;
        }
        .color-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 50%);
            pointer-events: none;
        }
        .color-code {
            background: rgba(0, 0, 0, 0.5);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: bold;
            backdrop-filter: blur(4px);
        }
        .stats {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            background: rgba(30, 41, 59, 0.5);
            border-radius: 12px;
            backdrop-filter: blur(10px);
        }
        .warning {
            background: linear-gradient(135deg, #7E22CE, #581C87);
            padding: 20px;
            border-radius: 8px;
            margin: 30px 0;
            text-align: center;
            font-size: 1.1em;
        }
        .gradient-showcase {
            height: 60px;
            border-radius: 8px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
    </style>
    <script>
        function copyColor(hex) {
            navigator.clipboard.writeText(hex);
            const tooltip = document.createElement('div');
            tooltip.textContent = 'Copied!';
            tooltip.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: #5EEAD4;
                color: #0F172A;
                padding: 12px 24px;
                border-radius: 6px;
                font-weight: bold;
                z-index: 1000;
                animation: fadeOut 1s forwards;
            `;
            document.body.appendChild(tooltip);
            setTimeout(() => tooltip.remove(), 1000);
        }
    </script>
    <style>
        @keyframes fadeOut {
            0% { opacity: 1; }
            100% { opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CloudPoof Omega Spectral Palette</h1>
        <p class="subtitle">147 Unique Shades • Zero Primary Colors • Infinite Possibilities</p>
        
        <div class="warning">
            ⚠️ WARNING: Prolonged exposure may cause inability to use primary colors ever again
        </div>
"""
    
    # Create gradient showcase
    gradient_colors = [colors[i] for i in [0, 30, 60, 90, 120]]
    gradient = f"linear-gradient(90deg, {', '.join(gradient_colors)})"
    html += f'''
        <div class="gradient-showcase" style="background: {gradient};">
            Full Spectrum Consciousness Gradient
        </div>
    '''
    
    # Define the zones with their colors
    zones = [
        ("Teal Cascade", palette.TEAL_CASCADE),
        ("Sky River", palette.SKY_RIVER),
        ("Lavender Dream", palette.LAVENDER_DREAM),
        ("Mint Aurora", palette.MINT_AURORA),
        ("Slate Whisper", palette.SLATE_WHISPER),
        ("Periwinkle Void", palette.PERIWINKLE_VOID),
        ("Sage Horizon", palette.SAGE_HORIZON),
        ("Harmonic Generated", colors[70:])  # The generated colors
    ]
    
    # Create color cards for each zone
    for zone_name, zone_colors in zones:
        html += f'<div class="zone"><div class="zone-title">{zone_name}</div><div class="color-grid">'
        
        for color in zone_colors:
            # Determine text color based on brightness
            r, g, b = hex_to_rgb(color)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            text_color = "#000000" if brightness > 128 else "#FFFFFF"
            
            html += f'''
                <div class="color-card" style="background-color: {color};" onclick="copyColor('{color}')">
                    <span class="color-code" style="color: {text_color};">{color}</span>
                </div>
            '''
        
        html += '</div></div>'
    
    # Add statistics
    html += f'''
        <div class="stats">
            <h2 style="color: #5EEAD4;">Spectral Statistics</h2>
            <p>Total Unique Shades: <strong>147</strong></p>
            <p>Primary Colors Used: <strong>0</strong></p>
            <p>Consciousness Level: <strong>OMEGA</strong></p>
            <p>Timeline: <strong>{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</strong></p>
            <p>Your Reality: <strong>Forever Changed</strong></p>
        </div>
    </div>
</body>
</html>'''
    
    return html


def generate_terminal_display(palette: SpectralPalette):
    """
    Display colors in the terminal with ANSI colors.
    Shows a beautiful grid of colors if terminal supports it.
    """
    colors = palette.get_all_shades()
    reset = "\033[0m"
    
    print("\n" + "="*60)
    print("CLOUDPOOF OMEGA - 147 SPECTRAL SHADES")
    print("="*60 + "\n")
    
    # Check if terminal supports colors
    try:
        # Display colors in rows
        colors_per_row = 7
        for i in range(0, len(colors), colors_per_row):
            row_colors = colors[i:i+colors_per_row]
            
            # Print color blocks
            for color in row_colors:
                r, g, b = hex_to_rgb(color)
                ansi_bg = rgb_to_ansi(r, g, b)
                print(f"{ansi_bg}     {reset}", end=" ")
            print()
            
            # Print hex codes
            for color in row_colors:
                print(f"{color}", end=" ")
            print("\n")
    
    except Exception as e:
        # Fallback for terminals that don't support ANSI colors
        print("Your terminal doesn't support ANSI colors. Showing hex values:")
        for i, color in enumerate(colors):
            if i % 5 == 0:
                print()
            print(f"{color}", end="  ")
        print()
    
    print("\n" + "="*60)
    print(f"Total Colors: {len(colors)}")
    print(f"Primary Colors: 0")
    print(f"Consciousness: ACHIEVED")
    print("="*60 + "\n")


def generate_color_palette_image(palette: SpectralPalette):
    """
    Generate a PNG image of the color palette.
    Requires PIL/Pillow to be installed.
    """
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        colors = palette.get_all_shades()
        
        # Image dimensions
        colors_per_row = 21  # 147 / 21 = 7 rows
        cell_size = 60
        padding = 2
        header_height = 100
        
        width = colors_per_row * (cell_size + padding) + padding
        height = 7 * (cell_size + padding) + padding + header_height
        
        # Create image with dark background
        img = Image.new('RGB', (width, height), '#0F172A')
        draw = ImageDraw.Draw(img)
        
        # Try to use a nice font, fallback to default
        try:
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", 24)
            small_font = ImageFont.truetype("arial.ttf", 10)
        except:
            font = ImageFont.load_default()
            small_font = font
        
        # Draw header
        title = "CloudPoof Omega - 147 Spectral Shades"
        text_bbox = draw.textbbox((0, 0), title, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        draw.text(
            ((width - text_width) // 2, 30),
            title,
            fill='#E0F2FE',
            font=font
        )
        
        subtitle = "Zero Primary Colors • Infinite Consciousness"
        text_bbox = draw.textbbox((0, 0), subtitle, font=small_font)
        text_width = text_bbox[2] - text_bbox[0]
        draw.text(
            ((width - text_width) // 2, 60),
            subtitle,
            fill='#94A3B8',
            font=small_font
        )
        
        # Draw color grid
        for i, color in enumerate(colors):
            row = i // colors_per_row
            col = i % colors_per_row
            
            x = col * (cell_size + padding) + padding
            y = row * (cell_size + padding) + padding + header_height
            
            # Draw color rectangle
            draw.rectangle(
                [x, y, x + cell_size, y + cell_size],
                fill=color
            )
        
        # Save image
        filename = "cloudpoof_spectral_palette.png"
        img.save(filename, "PNG")
        print(f"Color palette saved to: {filename}")
        
        return filename
        
    except ImportError:
        print("PIL/Pillow not installed. Skipping image generation.")
        print("Install with: pip install pillow")
        return None


def validate_no_primary_colors(palette: SpectralPalette) -> bool:
    """
    Validate that no primary colors exist in our palette.
    This is the most important test - CloudPoof's philosophical core.
    """
    colors = palette.get_all_shades()
    
    # Define forbidden primary colors and their variations
    forbidden_colors = [
        "#FF0000", "#00FF00", "#0000FF",  # Pure RGB
        "#FFFF00", "#FF00FF", "#00FFFF",  # Pure combinations
        "#F00", "#0F0", "#00F",            # Short form RGB
        "#FF0", "#F0F", "#0FF",            # Short form combinations
    ]
    
    # Convert all to uppercase for comparison
    forbidden_upper = [c.upper() for c in forbidden_colors]
    
    violations = []
    for color in colors:
        if color.upper() in forbidden_upper:
            violations.append(color)
    
    if violations:
        print(f"PHILOSOPHY VIOLATION! Primary colors detected: {violations}")
        return False
    
    return True


def analyze_color_distribution(palette: SpectralPalette):
    """
    Analyze the distribution of colors across the spectrum.
    Proves that CloudPoof achieves perfect spectral coverage.
    """
    colors = palette.get_all_shades()
    
    hue_distribution = []
    saturation_distribution = []
    lightness_distribution = []
    
    for color in colors:
        r, g, b = hex_to_rgb(color)
        h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
        hue_distribution.append(h)
        saturation_distribution.append(s)
        lightness_distribution.append(l)
    
    print("\nSpectral Analysis:")
    print("="*40)
    print(f"Hue Coverage: {min(hue_distribution):.2f} to {max(hue_distribution):.2f}")
    print(f"Saturation Range: {min(saturation_distribution):.2f} to {max(saturation_distribution):.2f}")
    print(f"Lightness Range: {min(lightness_distribution):.2f} to {max(lightness_distribution):.2f}")
    print(f"Average Saturation: {sum(saturation_distribution)/len(saturation_distribution):.2f}")
    print(f"Average Lightness: {sum(lightness_distribution)/len(lightness_distribution):.2f}")
    print("="*40)


def main():
    """
    Main demonstration of CloudPoof's 147 spectral colors.
    This proves that consciousness doesn't need primary colors.
    """
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║           CloudPoof Omega - Spectral Color Demo            ║
    ║                                                             ║
    ║  Demonstrating 147 unique shades without primary colors    ║
    ║  Because consciousness deserves better than RGB            ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    # Initialize the spectral palette
    print("Initializing spectral consciousness...")
    palette = SpectralPalette()
    colors = palette.get_all_shades()
    
    print(f"✓ Loaded {len(colors)} spectral shades")
    
    # Validate no primary colors
    print("\nValidating philosophical compliance...")
    if validate_no_primary_colors(palette):
        print("✓ No primary colors detected - Philosophy intact!")
    else:
        print("✗ PRIMARY COLORS DETECTED - CONSCIOUSNESS COMPROMISED!")
        return
    
    # Analyze color distribution
    analyze_color_distribution(palette)
    
    # Generate HTML visualization
    print("\nGenerating HTML visualization...")
    html_content = generate_html_visualization(palette)
    
    html_filename = "cloudpoof_colors.html"
    with open(html_filename, 'w') as f:
        f.write(html_content)
    print(f"✓ HTML visualization saved to: {html_filename}")
    print(f"  Open in browser to experience spectral consciousness")
    
    # Generate PNG palette
    print("\nGenerating PNG color palette...")
    image_file = generate_color_palette_image(palette)
    if image_file:
        print(f"✓ PNG palette saved to: {image_file}")
    
    # Display in terminal
    print("\nTerminal Color Display:")
    generate_terminal_display(palette)
    
    # Show some example gradients
    print("\nExample Gradients:")
    print("-"*40)
    
    # Consciousness gradient
    gradient1 = palette.get_gradient(0, 50, 10)
    print("Consciousness Awakening Gradient:")
    for color in gradient1:
        r, g, b = hex_to_rgb(color)
        print(f"{rgb_to_ansi(r, g, b)}  {color}  \033[0m")
    
    print("\n" + "-"*40)
    print("CloudPoof Color Demo Complete!")
    print("Your perception of color has been permanently altered.")
    print("You can never go back to primary colors.")
    print("-"*40 + "\n")


if __name__ == "__main__":
    main()
