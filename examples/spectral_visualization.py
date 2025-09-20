"""
CloudPoof Omega - Spectral Visualization Example
examples/spectral_visualization.py

This demonstrates the 147 spectral colors that CloudPoof uses instead of 
primary colors. Run this to see why we refuse to use red, green, and blue.

Created by Cazandra Aporbo MS
"""

import colorsys
import random
from typing import List, Tuple
import json

class SpectralVisualizer:
    """
    Generates and visualizes the 147 spectral colors of CloudPoof.
    No primary colors were harmed in the making of this palette.
    """
    
    def __init__(self):
        """Initialize the spectral consciousness."""
        # The seven spectral zones that define CloudPoof's aesthetic
        self.zones = {
            "TEAL_CASCADE": {
                "base": "#5EEAD4",
                "description": "For clarity and flow states",
                "colors": [
                    "#5EEAD4", "#4DD4C0", "#3CBFAC", "#2BAA98", "#1A9584",
                    "#14B8A6", "#0D9488", "#0F766E", "#115E59", "#134E4A",
                    "#2DD4BF", "#6EE7B7", "#86EFAC", "#A7F3D0"
                ]
            },
            "SKY_RIVER": {
                "base": "#7DD3FC",
                "description": "For infinite possibilities",
                "colors": [
                    "#7DD3FC", "#67E8F9", "#38BDF8", "#22D3EE", "#0EA5E9",
                    "#0284C7", "#0369A1", "#075985", "#0C4A6E", "#BAE6FD",
                    "#E0F2FE", "#F0F9FF", "#DBEAFE", "#93C5FD"
                ]
            },
            "LAVENDER_DREAM": {
                "base": "#C4B5FD",
                "description": "For intuition and precognition",
                "colors": [
                    "#C4B5FD", "#C7D2FE", "#A78BFA", "#A5B4FC", "#9333EA",
                    "#818CF8", "#7E22CE", "#6366F1", "#6B21A8", "#4F46E5",
                    "#581C87", "#4338CA", "#E9D5FF", "#F3E8FF", "#FAF5FF",
                    "#DDD6FE", "#E0E7FF", "#EEF2FF"
                ]
            },
            "MINT_AURORA": {
                "base": "#86EFAC",
                "description": "For growth and success states",
                "colors": [
                    "#86EFAC", "#6EE7B7", "#4ADE80", "#34D399", "#10B981",
                    "#059669", "#047857", "#065F46", "#064E3B", "#A7F3D0",
                    "#D1FAE5", "#ECFDF5", "#DCFCE7", "#BBF7D0"
                ]
            },
            "SLATE_WHISPER": {
                "base": "#94A3B8",
                "description": "For depth and stability",
                "colors": [
                    "#94A3B8", "#8B9AAF", "#64748B", "#556379", "#475569",
                    "#3E4C59", "#334155", "#2B3544", "#1E293B", "#0F172A",
                    "#CBD5E1", "#E2E8F0", "#F1F5F9", "#F8FAFC"
                ]
            },
            "PERIWINKLE_VOID": {
                "base": "#C7D2FE",
                "description": "For transcendent states",
                "colors": [
                    "#C7D2FE", "#E0E7FF", "#A5B4FC", "#C4B5FD", "#818CF8",
                    "#A78BFA", "#6366F1", "#6D28D9", "#4F46E5", "#5B21B6",
                    "#4338CA", "#4C1D95", "#EEF2FF", "#F5F3FF"
                ]
            },
            "SAGE_HORIZON": {
                "base": "#A7F3D0",
                "description": "For balance and harmony",
                "colors": [
                    "#A7F3D0", "#D1FAE5", "#6EE7B7", "#86EFAC", "#34D399",
                    "#4ADE80", "#10B981", "#059669", "#BEF264", "#D9F99D",
                    "#A3E635", "#84CC16", "#65A30D", "#4D7C0F", "#3F6212",
                    "#365314", "#ECFCCB", "#F7FEE7"
                ]
            }
        }
        
        # Generate additional harmonic colors to reach 147
        self.harmonic_colors = self._generate_harmonic_colors()
        
        # Compile all colors
        self.all_colors = self._compile_all_colors()
    
    def _generate_harmonic_colors(self) -> List[str]:
        """
        Generate additional harmonic colors using golden ratio distribution.
        These fill the gaps between our main spectral zones.
        """
        harmonic = []
        golden_ratio = 0.618033988749895
        
        # We need additional colors to reach 147
        current_count = sum(len(zone["colors"]) for zone in self.zones.values())
        needed = 147 - current_count
        
        for i in range(needed):
            # Use golden ratio for optimal distribution
            hue = (i * golden_ratio) % 1
            
            # Keep saturation and lightness in non-primary ranges
            # This ensures we never generate pure RGB
            saturation = 0.3 + (0.5 * ((i * 0.381966011250105) % 1))
            lightness = 0.55 + (0.35 * ((i * 0.272632342) % 1))
            
            # Convert to RGB then to hex
            rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(rgb[0] * 255),
                int(rgb[1] * 255),
                int(rgb[2] * 255)
            ).upper()
            
            harmonic.append(hex_color)
        
        return harmonic
    
    def _compile_all_colors(self) -> List[str]:
        """Compile all 147 unique spectral colors."""
        all_colors = []
        
        # Add all zone colors
        for zone in self.zones.values():
            all_colors.extend(zone["colors"])
        
        # Add harmonic colors
        all_colors.extend(self.harmonic_colors)
        
        # Ensure uniqueness
        all_colors = list(set(all_colors))
        
        # If we somehow have duplicates, generate more
        while len(all_colors) < 147:
            new_color = self._generate_unique_color(all_colors)
            all_colors.append(new_color)
        
        return all_colors[:147]  # Ensure exactly 147
    
    def _generate_unique_color(self, existing: List[str]) -> str:
        """Generate a unique color that doesn't exist in the list."""
        while True:
            h = random.random()
            s = 0.3 + random.random() * 0.5
            l = 0.5 + random.random() * 0.4
            rgb = colorsys.hls_to_rgb(h, l, s)
            hex_color = '#{:02x}{:02x}{:02x}'.format(
                int(rgb[0] * 255),
                int(rgb[1] * 255),
                int(rgb[2] * 255)
            ).upper()
            
            if hex_color not in existing:
                return hex_color
    
    def verify_no_primary_colors(self) -> bool:
        """
        Verify that none of our colors are primary colors.
        Returns True if we're primary-free, False if contamination detected.
        """
        # The forbidden colors
        primary_colors = [
            "#FF0000",  # Pure red
            "#00FF00",  # Pure green
            "#0000FF",  # Pure blue
            "#FFFF00",  # Pure yellow
            "#FF00FF",  # Pure magenta
            "#00FFFF",  # Pure cyan
            "#FFFFFF",  # Pure white (technically all primaries)
            "#000000",  # Pure black (absence of all)
        ]
        
        for color in self.all_colors:
            if color in primary_colors:
                print(f"WARNING: Primary color contamination detected: {color}")
                return False
            
            # Also check for near-primary colors (within threshold)
            rgb = self.hex_to_rgb(color)
            if self._is_nearly_primary(rgb):
                print(f"WARNING: Near-primary color detected: {color}")
                return False
        
        return True
    
    def _is_nearly_primary(self, rgb: Tuple[int, int, int], threshold: int = 20) -> bool:
        """Check if a color is nearly a primary color."""
        r, g, b = rgb
        
        # Check for nearly pure red
        if r > 235 and g < threshold and b < threshold:
            return True
        # Check for nearly pure green
        if g > 235 and r < threshold and b < threshold:
            return True
        # Check for nearly pure blue
        if b > 235 and r < threshold and g < threshold:
            return True
        
        return False
    
    def hex_to_rgb(self, hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    def create_gradient(self, start_idx: int, end_idx: int, steps: int = 10) -> List[str]:
        """Create a smooth gradient between two colors from our palette."""
        start_color = self.all_colors[start_idx % 147]
        end_color = self.all_colors[end_idx % 147]
        
        start_rgb = self.hex_to_rgb(start_color)
        end_rgb = self.hex_to_rgb(end_color)
        
        gradient = []
        for step in range(steps):
            t = step / (steps - 1) if steps > 1 else 0
            rgb = tuple(
                int(start_rgb[i] + t * (end_rgb[i] - start_rgb[i]))
                for i in range(3)
            )
            hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb).upper()
            gradient.append(hex_color)
        
        return gradient
    
    def visualize_console(self):
        """Display the colors in console with descriptions."""
        print("\n" + "="*80)
        print("CLOUDPOOF OMEGA - THE 147 SPECTRAL COLORS")
        print("="*80)
        print(f"\nTotal Colors: {len(self.all_colors)}")
        print(f"Primary Colors: {'NONE (as it should be)' if self.verify_no_primary_colors() else 'CONTAMINATION DETECTED!'}")
        print("\n" + "-"*80)
        
        # Display each zone
        for zone_name, zone_data in self.zones.items():
            print(f"\n{zone_name}")
            print(f"Purpose: {zone_data['description']}")
            print(f"Base Color: {zone_data['base']}")
            print(f"Colors in zone: {len(zone_data['colors'])}")
            
            # Show first 5 colors as sample
            for color in zone_data['colors'][:5]:
                rgb = self.hex_to_rgb(color)
                print(f"  {color} | RGB({rgb[0]:3}, {rgb[1]:3}, {rgb[2]:3})")
        
        print("\n" + "-"*80)
        print(f"Harmonic Colors Generated: {len(self.harmonic_colors)}")
        print("Sample harmonic colors:")
        for color in self.harmonic_colors[:5]:
            rgb = self.hex_to_rgb(color)
            print(f"  {color} | RGB({rgb[0]:3}, {rgb[1]:3}, {rgb[2]:3})")
    
    def generate_html_visualization(self, filename="spectral_colors.html"):
        """Generate an HTML file to visualize all 147 colors."""
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CloudPoof Omega - 147 Spectral Colors</title>
    <style>
        body {
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            color: #F0F9FF;
            font-family: 'Courier New', monospace;
            padding: 20px;
            margin: 0;
        }
        h1 {
            text-align: center;
            background: linear-gradient(90deg, #5EEAD4, #7DD3FC, #C4B5FD);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3em;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #94A3B8;
            margin-bottom: 40px;
        }
        .zone {
            margin-bottom: 40px;
            padding: 20px;
            background: rgba(30, 41, 59, 0.5);
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        .zone-title {
            font-size: 1.5em;
            margin-bottom: 10px;
            color: #86EFAC;
        }
        .zone-desc {
            color: #CBD5E1;
            margin-bottom: 15px;
        }
        .color-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }
        .color-box {
            height: 80px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8em;
            color: #000;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .color-box:hover {
            transform: scale(1.1);
        }
        .gradient-display {
            height: 40px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .stats {
            background: rgba(94, 234, 212, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 30px 0;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #64748B;
        }
    </style>
</head>
<body>
    <h1>CloudPoof Omega</h1>
    <p class="subtitle">The 147 Spectral Colors That Refuse Primary Contamination</p>
    
    <div class="stats">
        <h2>Spectral Statistics</h2>
        <p>Total Colors: <strong>147</strong></p>
        <p>Primary Colors Used: <strong>0</strong> (and proud of it)</p>
        <p>Spectral Zones: <strong>7</strong></p>
        <p>Consciousness Level: <strong>OMEGA</strong></p>
    </div>
"""
        
        # Add each zone
        for zone_name, zone_data in self.zones.items():
            zone_title = zone_name.replace('_', ' ').title()
            html += f"""
    <div class="zone">
        <div class="zone-title">{zone_title}</div>
        <div class="zone-desc">{zone_data['description']}</div>
        <div class="color-grid">
"""
            for color in zone_data['colors']:
                # Calculate text color based on background
                rgb = self.hex_to_rgb(color)
                brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
                text_color = '#000' if brightness > 128 else '#FFF'
                html += f"""            <div class="color-box" style="background: {color}; color: {text_color};" 
                 onclick="navigator.clipboard.writeText('{color}')" title="Click to copy">
                {color}
            </div>
"""
            html += """        </div>
    </div>
"""
        
        # Add harmonic colors section
        html += """
    <div class="zone">
        <div class="zone-title">Harmonic Generation</div>
        <div class="zone-desc">Additional colors generated through golden ratio distribution</div>
        <div class="color-grid">
"""
        for color in self.harmonic_colors[:20]:  # Show first 20
            rgb = self.hex_to_rgb(color)
            brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
            text_color = '#000' if brightness > 128 else '#FFF'
            html += f"""            <div class="color-box" style="background: {color}; color: {text_color};"
                 onclick="navigator.clipboard.writeText('{color}')" title="Click to copy">
                {color}
            </div>
"""
        html += """        </div>
    </div>
    
    <div class="zone">
        <div class="zone-title">Sample Gradients</div>
        <div class="zone-desc">Smooth transitions between spectral zones</div>
"""
        
        # Create some sample gradients
        gradients = [
            self.create_gradient(0, 50, 10),
            self.create_gradient(50, 100, 10),
            self.create_gradient(100, 146, 10)
        ]
        
        for i, gradient in enumerate(gradients):
            gradient_css = ', '.join(gradient)
            html += f"""        <div class="gradient-display" style="background: linear-gradient(90deg, {gradient_css});"></div>
"""
        
        html += """    </div>
    
    <div class="footer">
        <p>Created with consciousness by Cazandra Aporbo MS</p>
        <p>CloudPoof Omega - Where primary colors go to be rejected</p>
    </div>
    
    <script>
        // Add click feedback
        document.querySelectorAll('.color-box').forEach(box => {
            box.addEventListener('click', function() {
                const original = this.textContent;
                this.textContent = 'Copied!';
                setTimeout(() => {
                    this.textContent = original;
                }, 1000);
            });
        });
    </script>
</body>
</html>"""
        
        with open(filename, 'w') as f:
            f.write(html)
        
        print(f"\nHTML visualization saved to {filename}")
    
    def export_json(self, filename="spectral_colors.json"):
        """Export all colors as JSON for use in other applications."""
        data = {
            "metadata": {
                "total_colors": len(self.all_colors),
                "primary_colors_used": 0,
                "created_by": "Cazandra Aporbo MS",
                "philosophy": "Primary colors are for people who've given up"
            },
            "zones": {},
            "all_colors": self.all_colors,
            "harmonic_colors": self.harmonic_colors
        }
        
        # Add zone information
        for zone_name, zone_data in self.zones.items():
            data["zones"][zone_name] = {
                "base": zone_data["base"],
                "description": zone_data["description"],
                "colors": zone_data["colors"]
            }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Colors exported to {filename}")
    
    def demonstrate_no_primary_contamination(self):
        """Prove that we use zero primary colors."""
        print("\n" + "="*80)
        print("PRIMARY COLOR CONTAMINATION TEST")
        print("="*80)
        
        forbidden = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF"]
        
        print("\nScanning all 147 colors for primary contamination...")
        print("-"*80)
        
        contamination_found = False
        for i, color in enumerate(self.all_colors):
            if color in forbidden:
                print(f"ALERT: Primary color found at index {i}: {color}")
                contamination_found = True
            
            # Check for near-primary
            rgb = self.hex_to_rgb(color)
            if self._is_nearly_primary(rgb):
                print(f"WARNING: Near-primary at index {i}: {color}")
        
        if not contamination_found:
            print("✓ No primary colors detected")
            print("✓ All 147 colors are spectral")
            print("✓ CloudPoof remains pure")
        
        print("\n" + "="*80)
        print("CONTAMINATION TEST COMPLETE")
        print("="*80)


def main():
    """Run the spectral visualization demonstration."""
    print("""
╔════════════════════════════════════════════════════════════╗
║          CloudPoof Omega - Spectral Visualization          ║
║                                                            ║
║     Generating 147 colors that refuse to be primary       ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Create the visualizer
    visualizer = SpectralVisualizer()
    
    # Display in console
    visualizer.visualize_console()
    
    # Test for primary contamination
    visualizer.demonstrate_no_primary_contamination()
    
    # Generate HTML visualization
    visualizer.generate_html_visualization()
    
    # Export as JSON
    visualizer.export_json()
    
    # Demonstrate gradients
    print("\n" + "="*80)
    print("GRADIENT DEMONSTRATION")
    print("="*80)
    print("\nCreating smooth transitions between spectral zones...")
    
    gradient = visualizer.create_gradient(0, 50, 10)
    print(f"Gradient from {visualizer.all_colors[0]} to {visualizer.all_colors[50]}:")
    for i, color in enumerate(gradient):
        print(f"  Step {i+1}: {color}")
    
    print("\n" + "="*80)
    print("VISUALIZATION COMPLETE")
    print("="*80)
    print("\nFiles generated:")
    print("  - spectral_colors.html (open in browser to see all colors)")
    print("  - spectral_colors.json (for programmatic use)")
    print("\nRemember: In a world of primary colors, be the spectral gradient.")


if __name__ == "__main__":
    main()
