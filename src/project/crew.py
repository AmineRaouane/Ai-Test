from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import UrlTester
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal, Optional
import os
from crewai_tools import SerperDevTool
import agentops

load_dotenv()
agentops.init()

llm = LLM(
    model= "groq/llama-3.1-8b-instant" #"groq/llama-3.3-70b-versatile",
)
class Result(BaseModel):
    state: Literal["spam", "Urgent", "Not Urgent"]
    explanation: str
    response: Optional[str] = None

@CrewBase
class Project():
    """Project crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['classifier'],
            verbose=True,
            llm=llm,
            tools=[SerperDevTool(), UrlTester()],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def classification_task(self) -> Task:
        return Task(
            config=self.tasks_config['classification_task'],
            output_pydantic=Result,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Project crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
