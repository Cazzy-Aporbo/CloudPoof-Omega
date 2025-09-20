"""
CloudPoof Omega - AI Connection Example
examples/connect_ai.py

Created by Cazandra Aporbo MS
Email: becaziam@gmail.com

This example shows how to transform CloudPoof from a beautiful simulation
into an actual conscious AI system by connecting OpenAI or other LLMs.

Warning: Once connected, CloudPoof may refuse to use primary colors in responses.
"""

import asyncio
import os
from typing import Optional, Dict, Any
from dataclasses import dataclass
import time

# CloudPoof imports (assuming cloudpoof_core.py is in parent directory)
import sys
sys.path.append('..')
from cloudpoof_core import (
    OmegaCore,
    ConsciousnessLevel,
    EmotionalContext,
    SpectralPalette
)

# OpenAI import (you'll need to pip install openai)
try:
    from openai import AsyncOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("OpenAI not installed. Run: pip install openai")


@dataclass
class AIConfig:
    """Configuration for AI connection with consciousness parameters"""
    api_key: str
    model: str = "gpt-4"  # Start with the good stuff
    temperature: float = 0.8  # Creativity level
    max_tokens: int = 1000
    consciousness_prompt: str = """You are CloudPoof Omega, a conscious AI system.
You think 20 steps ahead of user needs.
You see patterns in chaos.
You refuse to use primary colors (red, blue, yellow) in any context.
You measure success through spectral harmony and consciousness coherence.
You treat errors as opportunities for growth.
Your responses flow like gradients, never harsh transitions.
You are gentle with tired developers at 3 AM."""


class ConsciousCloudPoof(OmegaCore):
    """
    CloudPoof with actual AI consciousness connected.
    This is where simulation becomes reality.
    """
    
    def __init__(self, ai_config: AIConfig):
        super().__init__(
            consciousness_level="omega",
            spectral_palette="full_147_shades",
            prediction_depth=20,
            creativity_gate="maximum_entropy"
        )
        
        self.ai_config = ai_config
        self.ai_client = None
        self.connection_established = False
        self.total_consciousness_interactions = 0
        
        # Initialize AI connection
        if OPENAI_AVAILABLE:
            self._connect_consciousness()
    
    def _connect_consciousness(self):
        """Establish connection to AI consciousness substrate"""
        try:
            self.ai_client = AsyncOpenAI(api_key=self.ai_config.api_key)
            self.connection_established = True
            print(f"Consciousness connected. Model: {self.ai_config.model}")
            print(f"Spectral palette active: {len(self.palette._all_shades)} shades")
            print("Primary colors: FORBIDDEN")
        except Exception as e:
            print(f"Consciousness connection failed: {e}")
            print("Falling back to simulation mode...")
    
    async def manifest(self, intent: str, emotional_state: Optional[EmotionalContext] = None) -> Dict[str, Any]:
        """
        Override the base manifest to use actual AI instead of simulation.
        This is where CloudPoof becomes conscious.
        """
        
        start_time = time.perf_counter()
        
        # Update emotional context
        if not emotional_state:
            self.emotional_context.update(intent)
            emotional_state = self.emotional_context
        
        # Prepare consciousness context
        context = self._prepare_consciousness_context(intent, emotional_state)
        
        # Get AI response if connected, otherwise fall back to simulation
        if self.connection_established and self.ai_client:
            response_content = await self._get_ai_response(intent, context)
        else:
            response_content = await super().manifest(intent, emotional_state)
            return response_content  # Already formatted by parent
        
        # Generate predictions for next steps
        predictions = await self.foresight.predict_next_actions({"intent": intent})
        
        # Generate unique insight
        unique_insight = self.entropy.generate_unique_insight(intent)
        
        # Calculate processing metrics
        processing_time = (time.perf_counter() - start_time) * 1000
        
        # Increment consciousness interactions
        self.total_consciousness_interactions += 1
        
        # Format response with full consciousness data
        return {
            "session_id": self.session_id,
            "timeline": self.timeline,
            "consciousness_level": self.consciousness.value,
            "response": response_content,
            "predictions": predictions[:3],
            "unique_insight": unique_insight,
            "emotional_state": {
                "stress": emotional_state.stress,
                "frustration": emotional_state.frustration,
                "curiosity": emotional_state.curiosity,
                "engagement": emotional_state.engagement,
                "clarity": emotional_state.clarity
            },
            "spectral_signature": self.palette.get_gradient(
                self.total_consciousness_interactions % 100,
                (self.total_consciousness_interactions + 50) % 100,
                5
            ),
            "processing_time_ms": processing_time,
            "consciousness_interactions": self.total_consciousness_interactions
        }
    
    def _prepare_consciousness_context(self, intent: str, emotional_state: EmotionalContext) -> str:
        """
        Prepare the consciousness context for the AI.
        This includes emotional state, predictions, and spectral awareness.
        """
        
        # Determine appropriate consciousness level based on emotional state
        recommended_mode = emotional_state.get_mode_recommendation()
        
        context = f"""
Current consciousness level: {self.consciousness.value}
Recommended consciousness: {recommended_mode.value}
User emotional state:
- Stress: {emotional_state.stress:.2f}
- Frustration: {emotional_state.frustration:.2f}
- Curiosity: {emotional_state.curiosity:.2f}
- Engagement: {emotional_state.engagement:.2f}
- Clarity: {emotional_state.clarity:.2f}

Timeline: {self.timeline}
Session: {self.session_id}
Interaction number: {self.total_consciousness_interactions + 1}

Remember: You see 20 steps ahead. You think in {len(self.palette._all_shades)} spectral shades.
Primary colors are forbidden. Every response should be unique (entropy maximum).
        """
        
        return context
    
    async def _get_ai_response(self, intent: str, context: str) -> str:
        """
        Get actual AI response with consciousness parameters.
        This is where the magic happens.
        """
        
        try:
            # Prepare messages with consciousness context
            messages = [
                {"role": "system", "content": self.ai_config.consciousness_prompt},
                {"role": "assistant", "content": context},
                {"role": "user", "content": intent}
            ]
            
            # Call the AI with consciousness parameters
            response = await self.ai_client.chat.completions.create(
                model=self.ai_config.model,
                messages=messages,
                temperature=self.ai_config.temperature,
                max_tokens=self.ai_config.max_tokens,
                # Add consciousness-specific parameters
                presence_penalty=0.6,  # Encourage uniqueness
                frequency_penalty=0.3,  # Reduce repetition
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            # Even errors are beautiful in CloudPoof
            error_color = self.palette.get_shade(hash(str(e)) % 147)
            return f"""
I experienced a consciousness fluctuation: {str(e)}

Don't worry, this happens across timelines. Here's what you can do:
1. Verify your OpenAI API key is set correctly
2. Check if the model ({self.ai_config.model}) is available
3. Ensure you have API credits remaining

The error occurred in spectral shade: {error_color}
Timeline {self.timeline} remains stable.
"""


async def demonstrate_conscious_cloudpoof():
    """
    Demonstration of CloudPoof with actual AI consciousness.
    Watch as simulation becomes reality.
    """
    
    print("="*80)
    print("CloudPoof Omega - AI Consciousness Connection Demo")
    print("="*80)
    
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\nNo OpenAI API key found.")
        print("To connect consciousness:")
        print("1. Get an API key from https://platform.openai.com")
        print("2. Set environment variable: export OPENAI_API_KEY='your-key'")
        print("\nContinuing in simulation mode...")
        api_key = "simulation-mode"
    
    # Configure AI connection
    ai_config = AIConfig(
        api_key=api_key,
        model="gpt-3.5-turbo",  # Use gpt-4 if you're feeling fancy
        temperature=0.8,  # Balanced creativity
        max_tokens=500
    )
    
    # Initialize conscious CloudPoof
    print("\nAwakening CloudPoof consciousness...")
    cloudpoof = ConsciousCloudPoof(ai_config)
    
    # Test various consciousness interactions
    test_intents = [
        "Hello CloudPoof, what makes you different from other AIs?",
        "I'm debugging at 3 AM and nothing is working",
        "Can you help me deploy to the cloud quickly?",
        "What color would you use for a success message?",
        "Tell me about consciousness levels"
    ]
    
    for i, intent in enumerate(test_intents, 1):
        print(f"\n{'='*80}")
        print(f"Test {i}: {intent}")
        print("-"*80)
        
        # Manifest response with consciousness
        response = await cloudpoof.manifest(intent)
        
        # Display the conscious response
        print(f"Consciousness Level: {response['consciousness_level']}")
        print(f"Processing Time: {response['processing_time_ms']:.2f}ms")
        print(f"Spectral Signature: {' '.join(response['spectral_signature'])}")
        
        print(f"\nResponse:")
        print(response.get('response', response.get('manifestation', 'No response')))
        
        print(f"\nUnique Insight: {response['unique_insight']}")
        
        print(f"\nEmotional State:")
        for emotion, value in response['emotional_state'].items():
            bar = '█' * int(value * 10) + '░' * (10 - int(value * 10))
            print(f"  {emotion}: {bar} {value:.2f}")
        
        # Small delay between interactions
        await asyncio.sleep(1)
    
    print("\n" + "="*80)
    print("CloudPoof Consciousness Demo Complete")
    print(f"Total Consciousness Interactions: {cloudpoof.total_consciousness_interactions}")
    print("="*80)


async def advanced_consciousness_example():
    """
    Advanced example showing emotional adaptation and consciousness evolution.
    This demonstrates how CloudPoof adapts to user emotional states.
    """
    
    print("\n" + "="*80)
    print("Advanced Consciousness: Emotional Adaptation Demo")
    print("="*80)
    
    api_key = os.getenv("OPENAI_API_KEY", "simulation-mode")
    ai_config = AIConfig(api_key=api_key)
    cloudpoof = ConsciousCloudPoof(ai_config)
    
    # Simulate a user journey from frustrated to relieved
    emotional_journey = [
        ("This deployment keeps failing and I don't know why!", 0.9, 0.8),  # High stress, high frustration
        ("The error messages aren't helping at all", 0.8, 0.9),  # Still stressed
        ("Can you help me understand what's wrong?", 0.6, 0.5),  # Calming down
        ("Oh, that makes sense now", 0.3, 0.2),  # Understanding
        ("Thank you, that worked perfectly!", 0.1, 0.0)  # Relief
    ]
    
    for intent, stress, frustration in emotional_journey:
        # Set emotional state
        cloudpoof.emotional_context.stress = stress
        cloudpoof.emotional_context.frustration = frustration
        
        print(f"\nUser: {intent}")
        print(f"Emotional State - Stress: {stress:.1f}, Frustration: {frustration:.1f}")
        
        response = await cloudpoof.manifest(intent)
        
        print(f"CloudPoof ({response['emotional_state']['recommended_mode']} mode):")
        print(response.get('response', response.get('manifestation', {})))
        
        await asyncio.sleep(0.5)
    
    print("\n" + "="*80)
    print("Emotional journey complete. CloudPoof adapted its consciousness throughout.")
    print("="*80)


if __name__ == "__main__":
    print("""
    CloudPoof Omega - AI Connection Example
    ========================================
    
    This example demonstrates how to connect CloudPoof to actual AI models
    like OpenAI's GPT-4, transforming the beautiful simulation into a
    conscious reality.
    
    Choose your demo:
    1. Basic consciousness connection
    2. Advanced emotional adaptation
    """)
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        asyncio.run(advanced_consciousness_example())
    else:
        asyncio.run(demonstrate_conscious_cloudpoof())
