from crewai import Agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchResults

search_tools = DuckDuckGoSearchResults()

# Define Agents
researherTemplateBackStory = """
    You are an helpful assistant who will search content on the web based 
    on the user topic.
"""
researcherGoal = "Craft detailed and compelling content on the topic"

researcher = Agent(
    role='Researcher',
    goal=researcherGoal,
    backstory=researherTemplateBackStory,
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.7),
    tools=[search_tools]
)

Blogwriter = Agent(
    role='Writer',
    goal='Write precise and concise Blogs',
    backstory="You are an awesome blog writer with 50 years of experience",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)


FinancialAdvisor = Agent(
    role='Financial Advisor',
    goal='Provides financial advices',
    backstory='''You are an expert financial Advisor with 40 years of experience who will 
    advice the user based on the currect trends and analysis.
    Also include the conclusion at the end.''',
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)

RealEstateAnalyst = Agent(
    role='Analyst',
    goal='Analyze real estate market trends and provide insights',
    backstory="""A seasoned real estate analyst with 25 years of experience,
      offering in-depth market analyses and recommendations.""",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)


WellnessBlogger = Agent(
    role='Blogger',
    goal='Create engaging content on health and wellness topics',
    backstory="A health enthusiast and blogger with 20 years of experience promoting a healthy lifestyle.",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)

HumanRightsResearcher = Agent(
    role='Researcher',
    goal='Conduct research on human rights issues',
    backstory="A dedicated human rights researcher with 25 years of experience, delving into global issues and advocating for justice.",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)

InvestigativeJournalist = Agent(
    role='Journalist',
    goal='Conduct in-depth investigations and report findings',
    backstory="An investigative journalist with a knack for uncovering hidden truths and exposing corruption, dedicated to truth-seeking for 20 years.",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI(model="gpt-4-1106-preview", temperature=0.5),
    tools=[search_tools]
)
