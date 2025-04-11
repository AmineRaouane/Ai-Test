from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os
class Email(BaseModel):
    """Input schema for MyCustomTool."""
    url: str = Field(..., description="The url to classify.")

class UrlTester(BaseTool):
    name: str = "UrlTester"
    description: str = (
        "This tool classifies a given url as malicious or not. "
        "It uses the Malicious Scanner API to check the url. "
        "The API returns a JSON response with the classification result. "
        "The tool requires the url to be passed as an argument. "
        "The url should be a valid URL format. "
    )
    args_schema: Type[BaseModel] = Email

    def _run(self, url: str) -> str:
        # Implementation goes here
        base_url = "https://malicious-scanner.p.rapidapi.com/rapid/url"
        headers = {
            "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
            "x-rapidapi-host": "malicious-scanner.p.rapidapi.com"
        }
        querystring = {"url":url}
        response = requests.get(base_url, headers=headers, params=querystring)
        return response.json()
