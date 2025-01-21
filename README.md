# CrewAI Research Assistant

An automated research system leveraging the CrewAI framework for collaborative AI agents that perform topic research and generate comprehensive reports.

## About CrewAI Framework
CrewAI enables the creation of multiple AI agents that work together to accomplish complex tasks. In this project:
- Agents operate sequentially
- Each agent has specific roles and goals
- Information flows between agents
- Tasks are processed using GPT-3.5-turbo

## Project Architecture

### Agents
1. Research Agent
   - Primary role: Information gathering
   - Capabilities: Topic analysis, data collection
   - Output: Structured research findings

2. Reporting Analyst
   - Primary role: Report generation
   - Capabilities: Information synthesis, report writing
   - Output: Formatted comprehensive reports

### Workflow
1. Research agent gathers information
2. Findings passed to reporting analyst
3. Final report generated with analysis

## Technical Setup

### Prerequisites
- Python 3.9+
- OpenAI API key
- Git

### Installation
1. Clone repository:
git clone https://github.com/tobi-alja/crew-playground.git
cd crew-playground

2. Create virtual environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies:
pip install crewai langchain langchain-openai python-dotenv

### Configuration
1. Create `.env` file:
OPENAI_API_KEY=your-key-here

2. Customize research topic in `crew.py`:
topic = "Your research topic here"

## Project Structure
crew-playground/
├── agents/
│   ├── researcher.py      # Research agent implementation
│   └── reporting_analyst.py  # Report generation agent
├── crew.py               # Main orchestration script
├── .env                 # Configuration
└── README.md

## Usage

### Basic Execution
python crew.py

### Customization Options
1. Modify agent behaviors in respective files
2. Adjust LLM parameters in crew.py
3. Configure task descriptions
4. Change output formats

## Agent Configuration

### Research Agent
# agents/researcher.py
Agent(
    role='Researcher',
    goal='Conduct thorough research',
    backstory='Expert researcher with analytical skills'
)

### Reporting Agent
# agents/reporting_analyst.py
Agent(
    role='Reporting Analyst',
    goal='Create comprehensive reports',
    backstory='Skilled technical writer and analyst'
)

## CrewAI Task Flow
1. Task Assignment
   - Each agent receives specific tasks
   - Tasks include description and expected output

2. Execution Process
   - Sequential processing
   - Inter-agent communication
   - Result aggregation

3. Output Generation
   - Structured report format
   - Comprehensive analysis
   - Citation of sources

## Development

### Adding New Agents
1. Create agent file in `agents/`
2. Define agent class and behavior
3. Add to crew configuration

### Modifying Tasks
Update task descriptions in `crew.py`:
research_task = Task(
    description="Research topic",
    expected_output="Detailed findings"
)

## Security Considerations
- Store API keys in `.env`
- Never commit sensitive data
- Monitor API usage
- Set usage limits

## Troubleshooting
- Check API key configuration
- Verify agent task definitions
- Monitor token usage
- Review error messages

## License
MIT License
