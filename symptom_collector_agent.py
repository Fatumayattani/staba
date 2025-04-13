import json
import os
from uagents import Agent, Context
from models import IPFSMessage  # Import the class we just updated
from dotenv import load_dotenv

# Initialize the agent for symptom collection
symptom_collector_agent = Agent(
    name="SymptomCollector",
    port=8000,  
    endpoint=["http://127.0.0.1:8000"],
    seed="symptom_collector secret phrase"
)

load_dotenv()

# Address of Diagnosis Agent
diagnosis_agent_address = "agent1q05ga3uxukgdzumdnq9dadflgs7dr4ry2p7fafx76s3t2fjscazej2tnpx9"

# Event handler for the symptom collector agent
@symptom_collector_agent.on_event("startup")
async def start(ctx: Context):
    symptoms = input("Enter your symptoms:\n> ")
    with open("symptoms.json", "w") as f:
        json.dump({"symptoms": symptoms}, f)

    # Upload the symptoms file to IPFS via w3
    os.system("w3 space use collector_space")
    os.system("w3 up symptoms.json")

    ipfs_url = input("Paste the IPFS URL from Storacha here:\n> ")
    # Send the IPFS URL to the Diagnosis Agent
    await ctx.send(diagnosis_agent_address, IPFSMessage(ipfs_link=ipfs_url))

if __name__ == "__main__":
    symptom_collector_agent.run()  # Start the symptom collector agent
