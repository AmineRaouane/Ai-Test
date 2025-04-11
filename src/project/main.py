#!/usr/bin/env python
import sys
import warnings
from crew import Project

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
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
        return pydantic_result.model_dump()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")



if __name__ == "__main__":
    email = '''
    Hey,

    The following is an update from the Lovable team ❤️

    Introducing Dev Mode


    Lovable now has a Dev Mode. Enabling Dev Mode lets you not only read your project's code, but also edit it directly inside Lovable.

    Read more about it here.

    Buying Custom Domains


    You can now purchase a domain directly from your project settings — just click “Buy a domain”, search for what you want, and complete the checkout in a few clicks.

    We’ve partnered with IONOS to make this possible.

    Read more here.

    Lovable Status Page


    Wondering if something’s down? You can now check our status page for live updates.

    Check it out here.

    Lovable Livestream tomorrow (Thursday)


    ​This livestream isn’t about building live — it’s about learning from someone who’s already done it.

    ​Mindaugas has used Lovable to prototype and launch tools that scale his expertise, automate his value, and generate real outcomes — both for himself and the communities he serves.

    Register here.

    That's all for this time.

    Best,

    The Lovable Team


    Turn ideas into Lovable products at Lovable.dev

    Start building

    𝕏 TwitterLinkedInYouTubeDiscord'''
    result = run(email)
    print(result)
