from crewai import Agent

def create_reporting_analyst(llm):
    return Agent(
        role='Reporting Analyst',
        goal='Create comprehensive and well-structured reports',
        backstory="""You are an experienced analyst skilled at creating detailed 
        reports and presenting information clearly and effectively.""",
        llm=llm
    )