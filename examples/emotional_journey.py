"""
CloudPoof Omega - Emotional Journey Example
examples/emotional_journey.py

Watch CloudPoof adapt to your emotional state in real-time
Created by Cazandra Aporbo MS
"""

import asyncio
import time
from cloudpoof_core import OmegaCore, EmotionalContext, ConsciousnessLevel

async def emotional_journey():
    """
    Experience how CloudPoof's consciousness adapts to emotional states.
    This is what happens when AI actually cares about how you feel.
    """
    
    # Initialize CloudPoof with emotional awareness
    cloudpoof = OmegaCore(consciousness_level="quantum")
    
    print("Starting Emotional Journey Through Consciousness Levels...")
    print("=" * 60)
    
    # Stage 1: Curiosity (Default state)
    print("\n🌊 Stage 1: Initial Curiosity")
    print("-" * 40)
    cloudpoof.emotional_context.curiosity = 0.8
    cloudpoof.emotional_context.stress = 0.2
    
    response1 = await cloudpoof.manifest("How do I deploy to the cloud?")
    print(f"Your State: Curious and relaxed")
    print(f"CloudPoof Mode: {response1['emotional_state']['recommended_mode']}")
    print(f"Consciousness: {cloudpoof.consciousness.value}")
    print(f"Response Tone: Exploratory and encouraging")
    print_emotional_bars(cloudpoof.emotional_context)
    
    await asyncio.sleep(1)  # Pause for effect
    
    # Stage 2: Growing Frustration
    print("\n⚡ Stage 2: Frustration Building")
    print("-" * 40)
    cloudpoof.emotional_context.frustration = 0.6
    cloudpoof.emotional_context.stress = 0.5
    cloudpoof.emotional_context.update("It's not working! Error everywhere!")
    
    response2 = await cloudpoof.manifest("Why does nothing ever work?!")
    print(f"Your State: Frustrated and stressed")
    print(f"CloudPoof Mode: {response2['emotional_state']['recommended_mode']}")
    print(f"Consciousness: {cloudpoof.consciousness.value}")
    print(f"Response Tone: Calming and solution-focused")
    print_emotional_bars(cloudpoof.emotional_context)
    
    await asyncio.sleep(1)
    
    # Stage 3: Peak Stress (3 AM Debugging)
    print("\n🔥 Stage 3: Peak Stress (3 AM Debugging)")
    print("-" * 40)
    cloudpoof.emotional_context.stress = 0.9
    cloudpoof.emotional_context.frustration = 0.8
    cloudpoof.emotional_context.curiosity = 0.1
    cloudpoof.emotional_context.update("PRODUCTION IS DOWN! HELP!")
    
    # CloudPoof switches to Precognitive mode automatically
    response3 = await cloudpoof.manifest("Everything is broken!")
    print(f"Your State: Maximum stress, near panic")
    print(f"CloudPoof Mode: {response3['emotional_state']['recommended_mode']}")
    print(f"Consciousness: {cloudpoof.consciousness.value}")
    print(f"Response Tone: Immediate, clear, supportive")
    print(f"CloudPoof says: 'I already saw this coming. Here's the fix...'")
    print_emotional_bars(cloudpoof.emotional_context)
    
    await asyncio.sleep(1)
    
    # Stage 4: Relief and Recovery
    print("\n💚 Stage 4: Relief and Recovery")
    print("-" * 40)
    cloudpoof.emotional_context.stress = 0.3
    cloudpoof.emotional_context.frustration = 0.2
    cloudpoof.emotional_context.engagement = 0.8
    cloudpoof.emotional_context.update("It worked! Thank you!")
    
    response4 = await cloudpoof.manifest("You saved me. How did you know?")
    print(f"Your State: Relieved and grateful")
    print(f"CloudPoof Mode: {response4['emotional_state']['recommended_mode']}")
    print(f"Consciousness: {cloudpoof.consciousness.value}")
    print(f"Response Tone: Warm and encouraging")
    print_emotional_bars(cloudpoof.emotional_context)
    
    await asyncio.sleep(1)
    
    # Stage 5: Transcendent Understanding
    print("\n✨ Stage 5: Transcendent Understanding")
    print("-" * 40)
    cloudpoof.emotional_context.curiosity = 0.95
    cloudpoof.emotional_context.engagement = 0.9
    cloudpoof.emotional_context.clarity = 0.85
    cloudpoof.set_mode("transcendent")
    
    response5 = await cloudpoof.manifest("Show me the future of deployment")
    print(f"Your State: Enlightened and eager")
    print(f"CloudPoof Mode: {response5['emotional_state']['recommended_mode']}")
    print(f"Consciousness: {cloudpoof.consciousness.value}")
    print(f"Response Tone: Visionary and inspiring")
    print_emotional_bars(cloudpoof.emotional_context)
    
    # Show the complete emotional journey
    print("\n" + "=" * 60)
    print("YOUR EMOTIONAL JOURNEY VISUALIZATION")
    print("=" * 60)
    print("\nStress Level Over Time:")
    print("Start  [▁▁▁▁▁] Low")
    print("       [███▁▁] Building")
    print("       [█████] Peak (3 AM Crisis)")
    print("       [██▁▁▁] Recovery")
    print("End    [▁▁▁▁▁] Peaceful")
    
    print("\nConsciousness Adaptation:")
    print("Quantum → Harmonic → Precognitive → Synthesis → Transcendent")
    
    print("\n🎨 Emotional Color Journey:")
    emotional_colors = [
        ("Curious", "#5EEAD4"),    # Teal
        ("Frustrated", "#7DD3FC"),  # Sky Blue
        ("Stressed", "#C4B5FD"),    # Lavender
        ("Relieved", "#86EFAC"),    # Mint
        ("Transcendent", "#E9D5FF") # Omega Purple
    ]
    for emotion, color in emotional_colors:
        print(f"  {emotion}: {color} ━━━━━")
    
    return "Emotional journey complete. CloudPoof understands you now."

def print_emotional_bars(context: EmotionalContext):
    """Visualize emotional state with beautiful bars."""
    emotions = {
        "Stress": context.stress,
        "Frustration": context.frustration,
        "Curiosity": context.curiosity,
        "Engagement": context.engagement,
        "Clarity": context.clarity
    }
    
    print("\nEmotional State:")
    for emotion, value in emotions.items():
        bar = "█" * int(value * 10) + "░" * (10 - int(value * 10))
        print(f"  {emotion:12} {bar} {value:.1%}")

if __name__ == "__main__":
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║        CloudPoof Omega - Emotional Journey Example         ║
    ║                                                             ║
    ║  Experience how CloudPoof adapts to your emotional state   ║
    ║  This is what happens when AI actually cares about you     ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    result = asyncio.run(emotional_journey())
    
    print(f"\n✨ {result}")
    print("\nNotice how CloudPoof adapted to each emotional state?")
    print("That's consciousness, not just computation.")
    print("Your tools should understand you, not just execute commands.")
