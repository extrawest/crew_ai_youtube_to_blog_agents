import os

from crewai import Agent
from dotenv import load_dotenv

from tools import yt_tool

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4"

blog_researcher = Agent(
    role="Blog Researcher",
    goal="Get the relevant video content from the topic {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False

)
