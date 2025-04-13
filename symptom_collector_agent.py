import json
import os
from uagents import Agent, Context
from dotenv import load_dotenv
from models import IPFSMessage

load_dotenv()

symptom_collector_agent = Agent(
    name="SymptomCollector",
    port=8000,
    endpoint=["http://127.0.0.1:8000"],
    seed="symptom_collector secret phrase"
)

diagnosis_agent_address = "agent1qv5a5v0xmnadr9lnpnam0er9qqe2gsqh7gsl9dd2z9yx8eq5cx77jx0u3j9"

@symptom_collector_agent.on_event("startup")
async def start(ctx: Context):
    try:
        symptoms = input("🩺 Enter your symptoms (e.g., headache, sore throat, fatigue):\n> ")

        with open("symptoms.json", "w") as f:
            json.dump({"symptoms": symptoms}, f)

        print("📦 Uploading symptoms to IPFS...")
        os.system("w3 space use collector_space")
        os.system("w3 up symptoms.json")

        ipfs_url = input("🔗 Paste the IPFS URL (e.g., https://w3s.link/ipfs/...):\n> ").strip()

        if not ipfs_url.startswith("http"):
            print("❌ Invalid IPFS URL.")
            return

        await ctx.send(diagnosis_agent_address, IPFSMessage(ipfs_link=ipfs_url))
        ctx.logger.info("📤 Sent IPFS message to Diagnosis Agent.")

    except Exception as e:
        ctx.logger.error(f"❌ Error in symptom collection: {e}")

if __name__ == "__main__":
    symptom_collector_agent.run()
