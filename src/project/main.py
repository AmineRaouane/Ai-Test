#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv, find_dotenv
from crew import Project

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv(find_dotenv())
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(email):
    try:
        result = Project().crew().kickoff(
            inputs={
                "email": email,
            }
        )
        pydantic_result = result.pydantic
        return pydantic_result.dict()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
