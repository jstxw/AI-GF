#!/usr/bin/env python3
"""
Generate LiveKit connection details for web interface
"""

import os
from dotenv import load_dotenv
from livekit import api

load_dotenv()

def generate_connection_details():
    # Your LiveKit credentials from .env
    url = os.getenv("LIVEKIT_URL")
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    
    # Room and participant details
    room_name = "ai-girlfriend-room"
    participant_identity = "web-user"
    participant_name = "Web User"
    
    # Generate access token
    token = api.AccessToken(api_key, api_secret) \
        .with_identity(participant_identity) \
        .with_name(participant_name) \
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room_name,
            can_publish=True,
            can_subscribe=True,
        )).to_jwt()
    
    print("=" * 60)
    print("LIVEKIT WEB CONNECTION DETAILS")
    print("=" * 60)
    print(f"Server URL: {url}")
    print(f"Room Name: {room_name}")
    print(f"Participant Identity: {participant_identity}")
    print(f"Access Token:")
    print(f"{token}")
    print("=" * 60)
    print()
    print("INSTRUCTIONS:")
    print("1. Go to https://meet.livekit.io/")
    print("2. Click 'Connect to custom server'")
    print("3. Enter the Server URL above")
    print("4. Enter the Access Token above")
    print("5. Join the room!")
    print("6. You should hear Ludia say: 'hey cutie... I was just thinking about you. what are you up to?'")
    print("=" * 60)

if __name__ == "__main__":
    generate_connection_details()
