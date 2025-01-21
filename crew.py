from crewai import LLM, Task, Crew
from config_loader import get_agent_config, get_task_config
from agents import create_researcher, create_reporting_analyst
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

def create_crew(topic):
    # Configure LLM
    openai_llm = LLM(
        model="gpt-3.5-turbo",
        api_key=os.getenv('OPENAI_API_KEY'),
        base_url="https://api.openai.com/v1"
    )

    # Create agents
    researcher = create_researcher(openai_llm)
    reporting_analyst = create_reporting_analyst(openai_llm)

    # Load configurations
    task_config = get_task_config()

    # Create tasks
    research_task = Task(
        description=f"Research about {topic}",
        expected_output="A detailed research report about the topic with key findings and insights",  # Added this line
        agent=researcher
    )

    reporting_task = Task(
        description="Create a comprehensive report",
        expected_output="A well-structured report with analysis and recommendations",  # Added this line
        agent=reporting_analyst
    )

    # Create and return crew
    return Crew(
        agents=[researcher, reporting_analyst],
        tasks=[research_task, reporting_task]
    )

def main():
    topic = "The evolution of AI agents and autonomous systems in 2025, focusing on multi-agent collaboration, emergent behaviors, and real-world applications in business and research"
    crew = create_crew(topic)
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()