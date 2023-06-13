from rasa.core.agent import Agent
import asyncio
agent = Agent.load(model_path='/home/csk/IdeaProjects/python-unittest/legabot/models/20230607-162104-mild-gofer.tar.gz')
text = "hi"
response = agent.handle_text(text)
print(asyncio.run(agent.handle_text(text)))

from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string

class Model:
    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")
    def message(self, message: str) -> str:
        message = message.strip()
        # result = asyncio.run(self.agent.parse_message(message))
        result = asyncio.run(self.agent.handle_text(message))
        return json_to_string(result)

mdl = Model("/home/csk/IdeaProjects/python-unittest/legabot/models/20230607-162104-mild-gofer.tar.gz")
sentence = "hello"
print(mdl.message(sentence))
