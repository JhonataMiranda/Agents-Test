#!/usr/bin/env python
import sys
import os
import warnings
import datetime
from cd_agents_research.crew import CdAgentsResearch

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs_array = [{'topic': 'Common Cold'}, {'topic': 'Influenza (Flu)'}, {'topic': 'Lyme Disease'}, 
                    {'topic': 'Hay Fever (Allergic Rhinitis)'}, {'topic': 'Urinary Tract Infections (UTIs)'}]
    
    try:
        crew = CdAgentsResearch().crew()
        results = crew.kickoff_for_each(inputs=inputs_array)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        reports_dir = f"reports_{timestamp}"
        os.makedirs(reports_dir, exist_ok=True)

        for i, result in enumerate(results):
            disease_name = inputs_array[i]['topic'].replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
            file_name = f"report_{disease_name}.md"
            file_path = os.path.join(reports_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(result.raw)

            print(f"Report saved in: {file_path}")
            print(f"Content of {file_name}:\n{result.raw}")
            
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Common Cold"
    }
    try:
        CdAgentsResearch().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CdAgentsResearch().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Common Cold"
    }
    try:
        CdAgentsResearch().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
