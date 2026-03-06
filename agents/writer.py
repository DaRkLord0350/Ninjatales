from prompts.story_prompt import STORY_SYSTEM_PROMPT
from utils.logger import logger
from data.schema.chapter import Chapter

class ChapterGenerator:
    def __init__(self, model, system_prompt: str):
        """Initialize the chapter writer agent."""
        self.model = model
        self.system_prompt = system_prompt

    def generate_chapter(self, task: str, days: int, currDay: int, recap: str) -> dict:
        """Generates a chapter based on the task."""
        logger.info(f"Generating chapter for task {currDay}/{days}: [yellow]{task}[/yellow]")

        # Prepare prompt with system message and task details
        prompt = f"""System: {self.system_prompt}

User Request:
Here is the task: {task} and the day: {currDay} out of {days}. 
Write a chapter for the story based on this task. 
Recap from previous chapter: {recap}"""
        
        # Call Bytez model
        results = self.model.run(prompt)
        
        if results.error:
            logger.error(f"Error generating chapter: {results.error}")
            raise Exception(f"Bytez API Error: {results.error}")
        
        # Extract output text from response
        output_text = results.output.get('content', str(results.output))
        
        # Create chapter object
        chapter = Chapter(
            title=f"Chapter {currDay}",
            story=output_text
        )
        
        logger.success(f"Chapter written: \"{chapter.title}\"")

        return {"chapter": chapter}

    