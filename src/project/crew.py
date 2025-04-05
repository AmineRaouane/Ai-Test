from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.custom_tool import EmailClassifier

# Create an LLM with streaming enabled
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key="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"
)
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
from pydantic import BaseModel
from typing import Literal, Optional

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
            # tools=[EmailClassifier()],
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
