import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)






@CrewBase
class StudyBuddyTopicBreakdownAndQuizAssistantCrew:
    """StudyBuddyTopicBreakdownAndQuizAssistant crew"""

    
    @agent
    def topic_breakdown_specialist(self) -> Agent:

        
        return Agent(
            config=self.agents_config["topic_breakdown_specialist"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def quiz_creator(self) -> Agent:

        
        return Agent(
            config=self.agents_config["quiz_creator"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def study_guide_compiler(self) -> Agent:

        
        return Agent(
            config=self.agents_config["study_guide_compiler"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def break_down_study_topic(self) -> Task:
        return Task(
            config=self.tasks_config["break_down_study_topic"],
            markdown=False,
            
            
        )
    
    @task
    def generate_quiz_questions(self) -> Task:
        return Task(
            config=self.tasks_config["generate_quiz_questions"],
            markdown=False,
            
            
        )
    
    @task
    def compile_complete_study_guide(self) -> Task:
        return Task(
            config=self.tasks_config["compile_complete_study_guide"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the StudyBuddyTopicBreakdownAndQuizAssistant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
