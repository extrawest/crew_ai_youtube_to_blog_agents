from crewai import Task

from agents import blog_researcher, blog_writer
from tools import yt_tool

research_task = Task(
    name="Research",
    description=(
        "Identify the video {topic}."
        "Get detailed info about the video from YT channel"
    ),
    tools=[yt_tool],
    expected_output="A comprehensive 3 paragraphs ling report based on the {topic} of video",
    agent=blog_researcher,
)

write_task = Task(
    description=(
        "Get the info from the YT channel on the topic {topic}."
    ),
    tools=[yt_tool],
    expected_output="Summarize the info from the YT channel on the {topic} and create content for the blog",
    agent=blog_writer,
    async_execution=False,
    output_file='new_blog_post.md'
)
