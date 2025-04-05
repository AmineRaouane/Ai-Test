from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from transformers import pipeline
import torch

class Email(BaseModel):
    """Input schema for MyCustomTool."""
    email: str = Field(..., description="The email to classify.")

class EmailClassifier(BaseTool):
    name: str = "EmailClassifier"
    description: str = (
        "This tool classifies an email as spam,or not spam."
        " It uses a pre-trained model to perform the classification."
        " The input should be a string containing the email text."
        " The output will be a dictionary with the classification label 1 for spam and 0 for not spam. and a score from 0 to 1 indicating the confidence of the classification."
    )
    args_schema: Type[BaseModel] = Email

    def _run(self, email: str) -> str:
        # Implementation goes here
        pipe = pipeline(task="text-classification", model="mrm8488/bert-tiny-finetuned-sms-spam-detection")
        result = pipe(email)
        print(result)
        return result
