from crewai import Agent

def create_researcher(llm):
    return Agent(
        role='Researcher',
        goal='Conduct thorough research and find accurate information',
        backstory="""You are an expert researcher with vast knowledge and 
        experience in finding and analyzing information.""",
        llm=llm
    )