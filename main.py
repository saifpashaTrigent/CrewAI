import os
import streamlit as st
from crewai import Task, Crew
from dotenv import load_dotenv

load_dotenv()
from functions.agents import (
    researcher,
    Blogwriter,
    FinancialAdvisor,
    RealEstateAnalyst,
    WellnessBlogger,
    HumanRightsResearcher,
    InvestigativeJournalist,
)

st.set_page_config("Crew Ai", "🧧", layout="wide")
# Here is the saif app

with st.sidebar:
    st.header("About Crew Ai")
    st.write("This is a sample demo built for demonstration purposes.")
    st.markdown(
        """
        1. Role-Based Agent Design: Customize agents with specific roles, goals, and tools.
        2. Autonomous Inter-Agent Delegation: Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
        3. Flexible Task Management: Define tasks with customizable tools and assign them to agents dynamically.
        4. Processes Driven: Currently only supports sequential task execution but more complex processes like consensual and hierarchical are being worked on.
    """
    )

st.header("Welcome to CrewAi 🧧")
st.markdown(
    """
1. Get the latest information of your Blog Title.
2. Select the appropriateAgent that matches your Title.
3. Look at the amazing blog written for the Title by the awesome Agent.
            """
)

inputAgent = st.selectbox(
    "Select an Agent",
    [
        "💲 Financial Advisor Agent",
        "✍🏻 Blog Writer Agent",
        "🏘️ Real Estate Analyst Agent",
        "💆🏻‍♀️ Wellness Blogger Agent",
        "🕵 Investigation Journalist Agent",
    ],
)


# Assigning the selected Agent
if inputAgent == "✍🏻 Blog Writer Agent":
    selectedAgent = Blogwriter
elif inputAgent == "🏘️ Real Estate Analyst Agent":
    selectedAgent = RealEstateAnalyst
elif inputAgent == "💆🏻‍♀️ Wellness Blogger Agent":
    selectedAgent = WellnessBlogger
elif inputAgent == "💲 Financial Advisor Agent":
    selectedAgent = FinancialAdvisor
elif inputAgent == "🕵 Investigation Journalist Agent":
    selectedAgent = InvestigativeJournalist
else:
    st.warning("Please select an agent")

task1 = Task(
    description=st.text_input(
        "What type of information would you like me to generate?",
        "should i invest in semi-conductor industry in 2024?",
    ),
    agent=researcher,
)

task2 = Task(
    description="""Using the insights provided, develop an engaging report.
    Your report should be informative yet accessible, catering to a savvy audience.
    Make it sound cool, avoid complex words so it doesn't sound like AI.
    Your final answer MUST be the full report with minimum 4 paragraphs with conclusion to
    the topic.
    Also include the sources of the generated Information.
    """,
    agent=selectedAgent,
)

crew = Crew(
    agents=[
        researcher,
        Blogwriter,
        FinancialAdvisor,
        RealEstateAnalyst,
        WellnessBlogger,
        InvestigativeJournalist,
    ],
    tasks=[task1, task2],
    verbose=2,
)

if st.button("Search"):
    with st.spinner("In progress..."):
        reearchReport = crew.kickoff()
        st.title("Research Report")
        st.write(reearchReport)

        st.download_button(
            label="Download",
            data=reearchReport.encode("utf-8"),
            file_name=f"{selectedAgent}.txt",
            mime="text/plain",
        )
