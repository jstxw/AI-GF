#!/usr/bin/env python3
"""
Test script to connect to LiveKit room and trigger the AI girlfriend agent
"""

import asyncio
import os
from dotenv import load_dotenv
from livekit import api, rtc

load_dotenv()

async def main():
    # Your LiveKit credentials from .env
    url = os.getenv("LIVEKIT_URL")  # wss://project1-67y5mslf.livekit.cloud
    api_key = os.getenv("LIVEKIT_API_KEY")  # APIKeaG8gG4xbLn
    api_secret = os.getenv("LIVEKIT_API_SECRET")  # AkguAchU2B8Lz5RGHPHVHB57E4n9LcZLXowj7f49o7S
    
    # Room and participant details
    room_name = "ai-girlfriend-room"
    participant_identity = "test-user"
    participant_name = "Test User"
    
    print(f"Connecting to LiveKit server: {url}")
    print(f"Room: {room_name}")
    print(f"Participant: {participant_identity}")
    
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
    
    print(f"Generated token: {token[:50]}...")
    
    # Connect to room
    room = rtc.Room()
    
    @room.on("participant_connected")
    def on_participant_connected(participant: rtc.RemoteParticipant):
        print(f"Participant connected: {participant.identity}")
    
    @room.on("participant_disconnected")
    def on_participant_disconnected(participant: rtc.RemoteParticipant):
        print(f"Participant disconnected: {participant.identity}")
    
    @room.on("track_published")
    def on_track_published(publication: rtc.RemoteTrackPublication, participant: rtc.RemoteParticipant):
        print(f"Track published: {publication.sid} by {participant.identity}")
    

    try:
        # Connect to the room
        await room.connect(url, token)
        print(f"✅ Connected to room: {room_name}")
        print(f"Local participant: {room.local_participant.identity}")
        
        # Keep the connection alive for a while to let the agent connect
        print("Waiting for AI girlfriend agent to connect...")
        print("The agent should say: 'hey cutie... <laugh> I was just thinking about you. what are you up to?'")
        
        # Wait for 30 seconds to see if agent connects
        await asyncio.sleep(30)
        
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
    finally:
        await room.disconnect()
        print("Disconnected from room")

if __name__ == "__main__":
    asyncio.run(main())
