import re
import os
from utils.llm_model import invoke_claude
from prompts.agent_prompt import AGENT_PROMPT


action_re = re.compile(r'^Action: (\w+): (.*)$')

class Agent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message, max_turns=5):
        self.messages.append({"role": "user", "content": message})
        result = None
        for _ in range(max_turns):
            result = self.execute()
            self.messages.append({"role": "assistant", "content": result})

            # Look for an Action line in the response
            actions = [action_re.match(line) for line in result.split('\n') if action_re.match(line)]
            if not actions:
                # No action found — LLM is done, return the answer
                break

            # Run the first action found
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise ValueError(f"Unknown action: {action}: {action_input}")

            observation = known_actions[action](action_input)
            obs_message = f"Observation: {observation}"
            self.messages.append({"role": "user", "content": obs_message})

        return result

    def execute(self):
        return invoke_claude(self.messages)

def calculate(what):
    return eval(what)

def average_dog_weight(name):
    name = name.strip()
    if "Scottish Terrier" in name:
        return "Scottish Terriers average 20 lbs"
    elif "Border Collie" in name:
        return "a Border Collies average weight is 37 lbs"
    elif "Toy Poodle" in name:
        return "a toy poodles average weight is 7 lbs"
    else:
        return "An average dog weights 50 lbs"

known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}

if __name__ == "__main__":
    abot = Agent(AGENT_PROMPT)
    result = abot("How much does a toy poodle weigh?")
    print(result)