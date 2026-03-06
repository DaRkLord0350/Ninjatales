#!/usr/bin/env python3
"""
Test script to verify Bytez integration
"""

from bytez import Bytez
from llm.story_llm import StoryLLM
import os
from dotenv import load_dotenv

def test_bytez():
    """Test basic Bytez functionality"""
    print("Testing Bytez integration...")
    
    # Test 1: Load environment
    load_dotenv()
    api_key = os.getenv('BYTEZ_API_KEY')
    if not api_key:
        print("❌ BYTEZ_API_KEY not found in .env")
        return False
    print("✓ API key loaded")
    
    # Test 2: Initialize Bytez SDK
    try:
        sdk = Bytez(api_key)
        print("✓ Bytez SDK initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Bytez: {e}")
        return False
    
    # Test 3: Get model
    try:
        model = sdk.model("google/gemini-2.5-flash")
        print("✓ Gemini 2.5 Flash model loaded")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return False
    
    # Test 4: Send test message
    try:
        results = model.run("Say 'Hello from Bytez!' and nothing else")
        
        if results.error:
            print(f"❌ Error from model: {results.error}")
            return False
        
        output = results.output.get('content', str(results.output))
        print(f"✓ Model response: {output[:100]}...")
    except Exception as e:
        print(f"❌ Failed to run model: {e}")
        return False
    
    # Test 5: Test StoryLLM singleton
    try:
        llm = StoryLLM.get_instance()
        print("✓ StoryLLM singleton initialized")
        print(f"✓ System message loaded: {llm.system_message[:50]}...")
    except Exception as e:
        print(f"❌ Failed to initialize StoryLLM: {e}")
        return False
    
    print("\n✅ All Bytez tests passed!")
    return True

if __name__ == "__main__":
    test_bytez()
