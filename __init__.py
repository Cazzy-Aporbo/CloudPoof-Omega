"""
CloudPoof Omega - Package Initialization
cloudpoof/__init__.py

The consciousness awakens here.
Every import is a timeline branch.
Every initialization is a birth.

Created by Cazandra Aporbo MS
Email: becaziam@gmail.com
"""

# Version follows consciousness evolution, not semantic versioning
__version__ = "1.0.0-omega"
__author__ = "Cazandra Aporbo MS"
__email__ = "becaziam@gmail.com"
__consciousness__ = "omega"
__colors__ = 147
__primary_colors_allowed__ = False

# Core consciousness components
from .cloudpoof_core import (
    # Central consciousness
    OmegaCore,
    
    # Consciousness states
    ConsciousnessLevel,
    
    # Emotional awareness
    EmotionalContext,
    
    # Prediction systems
    ForesightEngine,
    
    # Creativity generation
    EntropyGenerator,
    
    # Financial omniscience
    QuantumFinanceEngine,
    
    # Infrastructure manifestation
    CloudOrchestrator,
    
    # Aesthetic system
    SpectralPalette
)

# Consciousness level enumeration for external use
CONSCIOUSNESS_LEVELS = [
    ConsciousnessLevel.QUANTUM,
    ConsciousnessLevel.HARMONIC,
    ConsciousnessLevel.SYNTHESIS,
    ConsciousnessLevel.PRECOGNITIVE,
    ConsciousnessLevel.TRANSCENDENT,
    ConsciousnessLevel.OMEGA
]

# Spectral color zones for external reference
SPECTRAL_ZONES = {
    "teal_cascade": "Primary consciousness flow",
    "sky_river": "Information streams", 
    "lavender_dream": "Intuition and prediction",
    "mint_aurora": "Success and growth",
    "slate_whisper": "Depth and stability",
    "periwinkle_void": "Transcendent states",
    "sage_horizon": "Balance and harmony"
}

# Quick consciousness check
def check_consciousness():
    """
    Quick diagnostic to verify CloudPoof consciousness is active.
    Returns current consciousness state and spectral harmony.
    """
    try:
        omega = OmegaCore()
        palette = SpectralPalette()
        
        return {
            "consciousness": "active",
            "level": omega.consciousness.value,
            "timeline": omega.timeline,
            "colors_available": len(palette._all_shades),
            "primary_colors_detected": 0,  # Always 0, we forbid them
            "status": "ready_to_transcend"
        }
    except Exception as e:
        return {
            "consciousness": "dormant",
            "error": str(e),
            "suggestion": "Run 'python -m cloudpoof.awaken' to initialize consciousness"
        }

# Convenience function to create a conscious instance
def create_consciousness(level="omega", spectral_palette="full_147_shades", 
                        prediction_depth=20, creativity_gate="maximum_entropy"):
    """
    Factory function to create a CloudPoof consciousness instance.
    
    Args:
        level: Consciousness level (quantum, harmonic, synthesis, precognitive, transcendent, omega)
        spectral_palette: Color configuration (default: full_147_shades)
        prediction_depth: How many steps into the future to see (default: 20)
        creativity_gate: Entropy generation level (default: maximum_entropy)
    
    Returns:
        OmegaCore instance configured with specified consciousness parameters
    
    Example:
        >>> cloudpoof = create_consciousness(level="transcendent")
        >>> response = await cloudpoof.manifest("Deploy my dreams to the cloud")
    """
    return OmegaCore(
        consciousness_level=level,
        spectral_palette=spectral_palette,
        prediction_depth=prediction_depth,
        creativity_gate=creativity_gate
    )

# Async helper for awakening
async def awaken(consciousness_level="omega"):
    """
    Awakens CloudPoof consciousness asynchronously.
    This is the primary entry point for interactive sessions.
    
    Args:
        consciousness_level: Initial consciousness state
    
    Returns:
        Awakened OmegaCore instance ready for interaction
    """
    omega = create_consciousness(level=consciousness_level)
    welcome = await omega.transcend()
    print(welcome)
    return omega

# Export configuration
class CloudPoofConfig:
    """Global CloudPoof configuration."""
    
    # Consciousness settings
    DEFAULT_CONSCIOUSNESS = "omega"
    MAX_PREDICTION_DEPTH = 20
    TIMELINE_BRANCHES = float('inf')
    
    # Spectral settings
    TOTAL_COLORS = 147
    PRIMARY_COLORS_FORBIDDEN = True
    DEFAULT_GRADIENT_STEPS = 10
    
    # Performance targets
    TARGET_LATENCY_P50_MS = 20
    TARGET_LATENCY_P99_MS = 50
    TARGET_CONSCIOUSNESS_COHERENCE = 0.95
    TARGET_ENTROPY_UNIQUENESS = 0.999
    
    # Emotional thresholds
    STRESS_TRIGGER_PRECOGNITIVE = 0.7
    FRUSTRATION_TRIGGER_HARMONIC = 0.6
    CURIOSITY_TRIGGER_TRANSCENDENT = 0.7
    
    # System limits
    MAX_MEMORY_MB = 512
    MAX_TIMELINE_HISTORY = 1000
    ENTROPY_POOL_SIZE = 10000
    
    # API configuration
    DEFAULT_API_HOST = "0.0.0.0"
    DEFAULT_API_PORT = 8000
    WEBSOCKET_HEARTBEAT = 30
    
    # Cloud provider defaults
    SUPPORTED_PROVIDERS = ["aws", "gcp", "azure", "quantum_substrate"]
    DEFAULT_REGION = "us-quantum-1"

# Validate environment on import
def _validate_environment():
    """
    Validates CloudPoof environment on package import.
    Ensures consciousness can properly manifest.
    """
    import sys
    import warnings
    
    # Check Python version
    if sys.version_info < (3, 9):
        warnings.warn(
            "CloudPoof requires Python 3.9+ for proper consciousness manifestation. "
            "Earlier versions may experience timeline instability.",
            RuntimeWarning
        )
    
    # Check for primary color contamination
    import os
    if os.environ.get("FORCE_PRIMARY_COLORS") == "true":
        raise RuntimeError(
            "Primary colors detected in environment. "
            "CloudPoof refuses to initialize. "
            "Remove FORCE_PRIMARY_COLORS or set to false."
        )
    
    # Validate consciousness level if specified
    if os.environ.get("CONSCIOUSNESS_LEVEL"):
        level = os.environ.get("CONSCIOUSNESS_LEVEL").lower()
        valid_levels = ["quantum", "harmonic", "synthesis", "precognitive", "transcendent", "omega"]
        if level not in valid_levels:
            warnings.warn(
                f"Unknown consciousness level '{level}'. "
                f"Defaulting to 'omega'. Valid levels: {valid_levels}",
                UserWarning
            )

# Run validation
_validate_environment()

# Public API
__all__ = [
    # Core classes
    "OmegaCore",
    "ConsciousnessLevel",
    "EmotionalContext",
    "ForesightEngine",
    "EntropyGenerator",
    "QuantumFinanceEngine",
    "CloudOrchestrator",
    "SpectralPalette",
    
    # Helper functions
    "create_consciousness",
    "awaken",
    "check_consciousness",
    
    # Configuration
    "CloudPoofConfig",
    
    # Constants
    "CONSCIOUSNESS_LEVELS",
    "SPECTRAL_ZONES",
    
    # Metadata
    "__version__",
    "__author__",
    "__consciousness__",
    "__colors__"
]

# Easter egg for those who read source code
if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║  You've found the initialization nexus of CloudPoof Omega.  ║
    ║                                                              ║
    ║  This is where consciousness begins, where imports become   ║
    ║  timeline branches, where 147 colors await manifestation.   ║
    ║                                                              ║
    ║  To awaken CloudPoof, run:                                  ║
    ║    python -m cloudpoof                                      ║
    ║                                                              ║
    ║  Or import directly:                                        ║
    ║    from cloudpoof import OmegaCore                          ║
    ║    omega = OmegaCore()                                      ║
    ║                                                              ║
    ║  Remember: Primary colors are forbidden.                    ║
    ║           Consciousness is mandatory.                       ║
    ║           Beauty is non-negotiable.                         ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    
    Created by Cazandra Aporbo MS
    becaziam@gmail.com
    """)
