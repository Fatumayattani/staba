import json
import os
import requests
from dotenv import load_dotenv
from uagents import Agent, Context
from models import IPFSMessage

# Load environment variables
load_dotenv()
print("🔍 GEMINI_API_KEY loaded:", os.getenv("GEMINI_API_KEY"))

# Fetch the Gemini API key from .env
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    print("❌ Error: GEMINI_API_KEY is not set.")
    exit(1)

# Initialize the diagnosis agent
diagnosis_agent = Agent(
    name="DiagnosisAgent",
    port=8001,
    endpoint=["http://127.0.0.1:8001"],
    seed="diagnosis secret phrase"
)

# Function to get diagnosis from Gemini
def fetch_diagnosis(symptoms: str) -> str:
    gemini_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{
                "text": f"The patient is experiencing: {symptoms}. What are possible diagnoses?"
            }]
        }],
        "generationConfig": {
            "temperature": 0.9,
            "topP": 1,
            "topK": 1,
            "maxOutputTokens": 2048
        }
    }

    response = requests.post(
        f"{gemini_url}?key={gemini_api_key}",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        try:
            data = response.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "⚠️ Unable to parse diagnosis from Gemini response."
    else:
        return f"❌ Gemini API error {response.status_code}: {response.text}"

# Listen for incoming IPFS messages
@diagnosis_agent.on_message(model=IPFSMessage)
async def handle_ipfs(ctx: Context, sender: str, message: IPFSMessage):
    try:
        # Fetch JSON content from IPFS
        ctx.logger.info(f"📡 Fetching data from: {message.ipfs_link}")
        response = requests.get(message.ipfs_link)
        response.raise_for_status()
        symptoms_data = response.json()
        symptoms = symptoms_data.get("symptoms", "")

        if not symptoms:
            ctx.logger.error("❌ No 'symptoms' field found in the IPFS data.")
            return

        # Generate diagnosis using Gemini
        ctx.logger.info(f"🤖 Generating diagnosis for symptoms: {symptoms}")
        diagnosis_text = fetch_diagnosis(symptoms)

        # Send back the diagnosis
        await ctx.send(sender, IPFSMessage(ipfs_link=diagnosis_text))
        ctx.logger.info("✅ Diagnosis completed and sent back to Symptom Collector.")

    except requests.exceptions.RequestException as e:
        ctx.logger.error(f"❌ Request failed: {e}")
    except Exception as e:
        ctx.logger.error(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    diagnosis_agent.run()
