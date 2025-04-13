import json
import os
import requests
from dotenv import load_dotenv
from uagents import Agent, Context
from models import IPFSMessage

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

print("🔍 GEMINI_API_KEY loaded:", gemini_api_key)

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
        "contents": [
            {
                "parts": [
                    {
                        "text": f"The patient is experiencing the following symptoms: {symptoms}. What possible illnesses or conditions could this indicate?"
                    }
                ]
            }
        ]
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
        except (KeyError, IndexError) as e:
            print("⚠️ Failed to parse Gemini response:", e)
            return "⚠️ Unable to parse diagnosis from Gemini response."
    else:
        print("❌ Gemini API error response:", response.text)
        return f"❌ Gemini API error {response.status_code}: {response.text}"

# Listen for incoming IPFS messages
@diagnosis_agent.on_message(IPFSMessage)
async def handle_ipfs(ctx: Context, message: IPFSMessage):
    try:
        ctx.logger.info(f"📡 Fetching data from IPFS: {message.ipfs_link}")
        response = requests.get(message.ipfs_link)
        response.raise_for_status()
        symptoms_data = response.json()

        symptoms = symptoms_data.get("symptoms", "")
        ctx.logger.info(f"📋 Extracted symptoms: {symptoms}")

        if not symptoms:
            ctx.logger.error("❌ No 'symptoms' field found in IPFS data.")
            return

        # Generate diagnosis using Gemini
        ctx.logger.info(f"🤖 Sending symptoms to Gemini for diagnosis...")
        diagnosis_text = fetch_diagnosis(symptoms)
        ctx.logger.info(f"💡 Diagnosis from Gemini: {diagnosis_text}")

        # Save to file
        output_path = "diagnosis_output.json"
        with open(output_path, "w") as f:
            json.dump({"diagnosis": diagnosis_text}, f)

        # Upload to IPFS using Storacha
        if os.path.exists(output_path):
            ctx.logger.info("📤 Uploading diagnosis to IPFS via Storacha...")
            os.system("w3 space use diagnosis_space")
            os.system(f"w3 up {output_path}")
            ctx.logger.info("✅ Diagnosis uploaded to IPFS successfully.")
        else:
            ctx.logger.error("❌ Output file not found.")

    except requests.exceptions.RequestException as e:
        ctx.logger.error(f"❌ Request error: {e}")
    except Exception as e:
        ctx.logger.error(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    diagnosis_agent.run()
