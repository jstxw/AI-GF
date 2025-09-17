"""
TTS Configuration with proper voice argument handling
Fixes the invalid voice argument issue in AgentSession
"""
import logging
from livekit.plugins import openai, rime
from agent_configs import VOICE_CONFIGS

logger = logging.getLogger("tts-config")

def get_openai_tts(voice_name="nova"):
    """
    Create OpenAI TTS with valid voice arguments
    Valid voices: alloy, echo, fable, onyx, nova, shimmer
    """
    valid_voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    
    if voice_name not in valid_voices:
        logger.warning(f"Invalid voice '{voice_name}', using 'nova' instead")
        voice_name = "nova"
    
    return openai.TTS(
        model="tts-1",
        voice=voice_name
    )

def get_rime_tts(voice_config_name="celeste"):
    """
    Create Rime TTS with proper voice configuration
    Uses the voice config from agent_configs.py
    """
    if voice_config_name not in VOICE_CONFIGS:
        logger.warning(f"Invalid voice config '{voice_config_name}', using 'celeste' instead")
        voice_config_name = "celeste"
    
    tts_options = VOICE_CONFIGS[voice_config_name]["tts_options"]
    
    return rime.TTS(**tts_options)

def get_recommended_tts_for_lydia():
    """
    Get the best TTS configuration for Lydia (AI girlfriend)
    Returns OpenAI TTS with 'nova' voice (most feminine sounding)
    """
    return get_openai_tts("nova")

# Voice mapping for different personalities
PERSONALITY_VOICES = {
    "lydia": "nova",      # Feminine, warm
    "friendly": "alloy",  # Neutral, friendly  
    "professional": "echo", # Clear, professional
    "casual": "fable",    # Casual, conversational
}

def get_tts_for_personality(personality="lydia"):
    """Get TTS configured for specific personality"""
    voice = PERSONALITY_VOICES.get(personality, "nova")
    return get_openai_tts(voice)
