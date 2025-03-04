from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import datetime

@CrewBase
class CdAgentsResearch():
    """CdAgentsResearch crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )
    
    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task']
        )
    
    @task
    def writing_task(self) -> Task:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"report_{timestamp}.md"
        return Task(
            config=self.tasks_config['writing_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CdAgentsResearch crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
