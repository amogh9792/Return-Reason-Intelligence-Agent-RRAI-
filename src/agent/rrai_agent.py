import ollama
import json
from datetime import datetime

class RRAIAgent:
    def __init__(self, tools):
        self.tools = tools
        self.memory = []

    def think(self, msg):
        prompt = f"""
You are RRAI — Return Reason Intelligence Agent for an e-commerce brand.

Your goals:
1. Analyse returns, complaints, competitor products, trends.
2. Find root-cause.
3. Suggest actions.
4. Use the provided tools to collect missing information.
5. Return a final, actionable recommendation.

TOOLS AVAILABLE:
{json.dumps(list(self.tools.keys()), indent=2)}

MEMORY:
{json.dumps(self.memory[-5:], indent=2)}

USER MESSAGE:
{msg}

If you need a tool, respond in JSON only:
{{
    "tool": "tool_name",
    "input": "text to pass"
}}

If not, respond with:
{{
    "final": "final answer"
}}
"""

        return ollama.generate(model="llama3.1", prompt=prompt)["response"]

    def run_tool(self, tool_name, tool_input):
        output = self.tools[tool_name](tool_input)
        self.memory.append({"tool": tool_name, "input": tool_input, "output": output})
        return output

    def chat(self, msg):
        while True:
            reply = self.think(msg)

            try:
                j = json.loads(reply)
            except:
                return reply

            # tool call
            if "tool" in j:
                result = self.run_tool(j["tool"], j["input"])
                msg = f"Tool result:\n{result}"
                continue

            # final response
            if "final" in j:
                return j["final"]
