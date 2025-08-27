# Rime LiveKit Agents – Technical Overview

## Project Summary

This project is a Python-based voice agent system built on top of LiveKit and Rime.ai. It enables hyper-realistic, character-driven conversational agents that can be deployed in real-time audio rooms using LiveKit's infrastructure. The system leverages advanced TTS (text-to-speech) models ("mistv2" and "arcana") and integrates with OpenAI for LLM (large language model) responses.

---

## Key Components

### 1. Agent Architecture

- **`rime_agent.py`**: Main entry point. Defines the agent logic, session management, and integration with LiveKit and Rime plugins.
- **`agent_configs.py`**: Contains voice/personality configurations and prompt engineering for different agent personas (e.g., "celeste").
- **`text_utils.py`**: Custom sentence tokenizer for the Arcana TTS model.

### 2. Core Technologies

- **LiveKit**: Real-time audio/video infrastructure. Used for room management, audio streaming, and agent orchestration.
- **Rime.ai**: Provides hyper-realistic TTS models ("mistv2", "arcana").
- **OpenAI**: Used for LLM-based conversational responses.
- **Python**: All orchestration and logic is written in Python 3.11+.

### 3. Plugins & Models

- **Noise Cancellation**: Uses `livekit-plugins-noise-cancellation` for improved audio quality.
- **Turn Detection**: Uses multilingual turn detection models for natural conversation flow.
- **Custom TTS**: Supports advanced TTS features and sentence tokenization for expressive speech.

---

## Setup & Configuration

### 1. Environment Variables (`.env`)

- `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`: LiveKit server connection.
- `OPENAI_API_KEY`: OpenAI API key for LLM responses.
- `RIME_API_KEY`: Rime.ai API key for TTS.

### 2. Installation

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
python rime_agent.py download-files  # Download model files
```

### 3. Running the Agent

- **Console mode (debugging):**
  ```bash
  python rime_agent.py console
  ```
- **LiveKit mode (production):**
  - Ensure all LiveKit env variables are set.
  - Run the agent to connect to a LiveKit room.
  ```bash
  python rime_agent.py dev
  ```

---

## Customization & Prompt Engineering

- Modify `agent_configs.py` to create new personalities, voices, and prompt styles.
- Each agent persona can have unique TTS settings, LLM prompts, and intro phrases.
- Example persona: "celeste" (clingy, playful, flirty university girlfriend).

---

## Technical Notes

- Uses a forked version of `livekit-plugins-rime` for improved arcana model support (see `requirements.txt`).
- All audio processing, TTS, and LLM calls are handled asynchronously for real-time performance.
- The agent is designed to be easily extended with new plugins, voices, or conversational logic.

---

## Demo/Deployment Tips

- For a demo, highlight:
  - Real-time, character-driven voice interaction.
  - Hyper-realistic TTS with expressive speech.
  - Easy persona customization via prompt engineering.
  - Integration with LiveKit for scalable, multi-user audio rooms.
- For production, consider deploying with Render or similar, and connecting a frontend via LiveKit's APIs.

---

## References

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/overview/)
- [Rime.ai](https://www.rime.ai/)
- [LiveKit Cloud](https://livekit.io/cloud)

---

_This document summarizes the technical architecture and setup for the Rime LiveKit Agents project. For more details, see the code._
