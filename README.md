# CdAgentsResearch Crew

Welcome to the CdAgentsResearch Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [crewAI](https://crewai.com).

First, if you haven't already, install crew ai:

```bash
pip install crewai crewai-tools
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY`, `SERPER_API_KEY` and `MODEL` settings into the `.env` file (create this file in the Agents-Test directory after clone this repository)**

## Running the Project

In the src/main.py file, define which themes will be generated in the inputs_array vector.

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the cd_agents_research Crew, assembling the agents and assigning them tasks as defined in your configuration.

You will be asked during execution whether you want to generate the report(s) synchronously or asynchronously.

The final reports will be created in a folder with a time stamp.

## Understanding Your Crew

The cd_agents_research Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Opening the MLFlow
To open the mlflow (`pip install mlflow`) of this project, make sure you are in the root folder of the project and type the following command:

```bash
$ mlflow server
```

Selecting the CrewAI tab in the left side, you can open the `Traces` of this project and view each run of this project.