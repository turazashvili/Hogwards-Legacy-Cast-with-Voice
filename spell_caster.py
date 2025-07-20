import logging
from typing import Type, Set
from difflib import SequenceMatcher
import keyboard
import assemblyai as aai
import time
from assemblyai.streaming.v3 import (
    BeginEvent,
    StreamingClient,
    StreamingClientOptions,
    StreamingError,
    StreamingEvents,
    StreamingParameters,
    StreamingSessionParameters,
    TerminationEvent,
    TurnEvent,
)

from os import environ
api_key = environ.get("ASSEMBLYAI_API_KEY")

SPELLS = {
    "lumos": "f1+1",
    "levitate": "f1+2",
    "levi os o": "f1+2",
    "levioso": "f1+2",
    "wingardium leviosa": "f1+2",
    "incendio": "f1+3",
    "summon": "f1+4",
    "axio": "f1+4",
    "exhale": "f1+4",
    "protego": "q",
    "revelio": "r", 
    "repair": "f2+3",
    "reparo": "f2+3",


    "disarm": "f1+3",
    "stun": "f2+1",
    "stupefy": "f2+1",
    "ward": "f2+2",


    "bind": "f2+4",
    "petrificus": "f2+4",
    
    "ignite": "f3+1",
    "freeze": "f3+2",
    "glacius": "f3+2",
    "arrest": "f3+3",
    "momentum": "f3+3",
    "blast": "f3+4",
    "confringo": "f3+4",
    
    "banish": "f4+1",
    "depulso": "f4+1",
    "shatter": "f4+2",
    "reducto": "f4+2",

    "patronum": "f4+3",
    "mend": "f4+4",
}

# Pre-compute spell variations for faster matching
SPELL_VARIATIONS = {}
for spell in SPELLS.keys():
    SPELL_VARIATIONS[spell] = spell
    # Add common variations
    if spell.endswith('um'):
        SPELL_VARIATIONS[spell[:-2]] = spell
    if spell.endswith('us'):
        SPELL_VARIATIONS[spell[:-2]] = spell
    # Add partial matches for longer spells
    if len(spell) > 4:
        SPELL_VARIATIONS[spell[:4]] = spell
        SPELL_VARIATIONS[spell[:5]] = spell

# Track recently cast spells to prevent spam
recently_cast: Set[str] = set()
last_cast_time = {}

def optimized_fuzzy_match(text, spell_list, threshold=0.6):
    """Optimized fuzzy matching with early exits and caching"""
    text = text.lower().strip()
    
    # First, try exact matches in variations
    if text in SPELL_VARIATIONS:
        return SPELL_VARIATIONS[text]
    
    # Quick substring check for common patterns
    for spell in spell_list:
        if spell in text or text in spell:
            if len(text) >= len(spell) * 0.7:  # At least 70% of spell length
                return spell
    
    # Fallback to fuzzy matching with optimized threshold
    best_match = None
    best_score = 0
    
    for spell in spell_list:
        # Skip if spell was recently cast (within 1 second)
        current_time = time.time()
        if spell in last_cast_time and current_time - last_cast_time[spell] < 1.0:
            continue
            
        score = SequenceMatcher(None, text, spell).ratio()
        if score > best_score and score >= threshold:
            best_score = score
            best_match = spell
    
    return best_match

def cast_spell(spell_name):
    """Cast spell with spam prevention"""
    current_time = time.time()
    
    # Prevent spell spam (minimum 0.5 seconds between same spell)
    if spell_name in last_cast_time and current_time - last_cast_time[spell_name] < 0.5:
        return
    
    if spell_name in SPELLS:
        command = SPELLS[spell_name]
        print(f"⚡ Casting {spell_name} - {command}")
        last_cast_time[spell_name] = current_time
        
        try:
            if "+" in command:
                keys = command.split("+")
                keyboard.press_and_release("+".join(keys))
            else:
                keyboard.press_and_release(command)
        except Exception as e:
            print(f"Failed to cast {spell_name}: {e}")

def process_transcript(transcript: str, confidence_threshold=0.6, is_partial=False):
    """Process transcript and attempt spell casting"""
    transcript = transcript.lower().strip()
    
    if len(transcript) < 3:  # Too short to be a spell
        return False
    
    # For partial transcripts, use higher confidence threshold
    actual_threshold = confidence_threshold + 0.2 if is_partial else confidence_threshold
    
    # Try to find spell with optimized matching
    matched_spell = optimized_fuzzy_match(transcript, SPELLS.keys(), actual_threshold)
    if matched_spell:
        cast_spell(matched_spell)
        return True
    
    # Check if transcript contains multiple words and try last word
    words = transcript.split()
    if len(words) > 1:
        last_word = words[-1]
        if len(last_word) >= 3:
            matched_spell = optimized_fuzzy_match(last_word, SPELLS.keys(), actual_threshold)
            if matched_spell:
                cast_spell(matched_spell)
                return True
    
    return False

def on_begin(self: Type[StreamingClient], event: BeginEvent):
    print(f"🎭 Spell casting session started: {event.id}")

def on_turn(self: Type[StreamingClient], event: TurnEvent):
    transcript = event.transcript
    is_partial = not event.end_of_turn
    
    if is_partial:
        # Process partial transcript for immediate response (min 4 characters)
        if len(transcript) >= 4:
            print(f"👂 Partial: {transcript}")
            if process_transcript(transcript, confidence_threshold=0.8, is_partial=True):
                print("✨ Spell cast from partial transcript!")
    else:
        # Process complete transcript
        print(f"🗣️ Complete: {transcript}")
        if not process_transcript(transcript, confidence_threshold=0.6, is_partial=False):
            print("❌ No spell recognized")

def on_terminated(self: Type[StreamingClient], event: TerminationEvent):
    print(f"🏁 Spell casting session ended: {event.audio_duration_seconds:.2f} seconds")

def on_error(self: Type[StreamingClient], error: StreamingError):
    print(f"💥 Error occurred: {error}")

def main():
    print("🏰 Hogwarts Spell Caster - Optimized for Speed!")
    print("Available spells: " + ", ".join(sorted(set(SPELLS.keys()))))
    print("💡 Tip: Speak clearly and pause briefly after each spell")
    print("🚀 Processing partial transcripts for instant response!")
    client = StreamingClient(
        StreamingClientOptions(
            api_key=api_key,
            api_host="streaming.assemblyai.com",
        )
    )

    client.on(StreamingEvents.Begin, on_begin)
    client.on(StreamingEvents.Turn, on_turn)  # Handle both partial and complete transcripts
    client.on(StreamingEvents.Termination, on_terminated)
    client.on(StreamingEvents.Error, on_error)

    # Optimized streaming parameters for lower latency
    client.connect(
        StreamingParameters(
            sample_rate=16000,
            format_turns=True,
            # Aggressive turn detection for faster response
            end_of_turn_confidence_threshold=0.5,  # Lower threshold for faster detection
            min_end_of_turn_silence_when_confident=100,  # Reduced from 160ms
            max_turn_silence=1500,  # Reduced from 2400ms
        )
    )

    try:
        print("🎤 Listening for spells...")
        client.stream(aai.extras.MicrophoneStream(sample_rate=16000))
    except KeyboardInterrupt:
        print("\n🛑 Stopping spell caster...")
    finally:
        client.disconnect(terminate=True)

if __name__ == "__main__":
    main()