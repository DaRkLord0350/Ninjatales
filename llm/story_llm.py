from typing import Optional
from bytez import Bytez
import os
from dotenv import load_dotenv
from prompts.story_prompt import STORY_SYSTEM_PROMPT

class StoryLLM:
    """
    Singleton class to manage Bytez LLM instance
    """
    _instance: Optional['StoryLLM'] = None
    _sdk: Optional[Bytez] = None
    _model = None
    _system_message: Optional[str] = None
    
    def __init__(self):
        if StoryLLM._instance is not None:
            raise Exception("StoryLLM is a singleton! Use StoryLLM.get_instance()")
        
        # Load environment variables
        load_dotenv()
        
        # Initialize Bytez SDK
        api_key = os.getenv('BYTEZ_API_KEY')
        if not api_key:
            raise ValueError("BYTEZ_API_KEY not found in environment variables")
        
        self._sdk = Bytez(api_key)
        
        # Initialize Gemini 2.5 Flash model
        self._model = self._sdk.model("google/gemini-2.5-flash")
        
        # Set system message
        self._system_message = STORY_SYSTEM_PROMPT
    
    @classmethod
    def get_instance(cls) -> 'StoryLLM':
        """Get or create the singleton instance"""
        if cls._instance is None:
            cls._instance = StoryLLM()
        return cls._instance
    
    @property
    def model(self):
        """Get the model instance"""
        return self._model
    
    @property
    def system_message(self) -> str:
        """Get the system message"""
        return self._system_message