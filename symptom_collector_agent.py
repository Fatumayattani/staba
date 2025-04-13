import json
import os
from uagents import Agent, Context
from dotenv import load_dotenv
from models import IPFSMessage  # Ensure this has: class IPFSMessage(Model): ipfs_link: str

# Load environment variables
load_dotenv()

# Initialize the agent
symptom_collector_agent = Agent(
    name="SymptomCollector",
    port=8000,
    endpoint=["http://127.0.0.1:8000"],
    seed="symptom_collector secret phrase"
)

# Replace with the actual address of the diagnosis agent
diagnosis_agent_address = "http://127.0.0.1:8001/submit"  # Use the Diagnosis Agent's endpoint

@symptom_collector_agent.on_event("startup")
async def start(ctx: Context):
    try:
        # Collect symptoms
        symptoms = input("🩺 Enter your symptoms (e.g., headache, sore throat, fatigue):\n> ")

        # Save to JSON file
        with open("symptoms.json", "w") as f:
            json.dump({"symptoms": symptoms}, f)

        # Upload file to IPFS via w3
        print("📦 Uploading symptoms to IPFS...")
        os.system("w3 space use collector_space")
        os.system("w3 up symptoms.json")

        # Prompt for IPFS URL
        ipfs_url = input("🔗 Paste the IPFS URL (e.g., https://w3s.link/ipfs/…):\n> ").strip()

        if not ipfs_url.startswith("http"):
            print("❌ Invalid IPFS URL. Make sure it starts with http.")
            return

        # Send the IPFS link to the Diagnosis Agent
        await ctx.send(diagnosis_agent_address, IPFSMessage(ipfs_link=ipfs_url))
        print("✅ Sent IPFS link to Diagnosis Agent.")

    except Exception as e:
        ctx.logger.error(f"❌ Error in symptom collection: {e}")

if __name__ == "__main__":
    symptom_collector_agent.run()
