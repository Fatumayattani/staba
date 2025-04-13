import json
import os
import requests
from dotenv import load_dotenv
from uagents import Agent, Context
from models import IPFSMessage

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
print("🔍 GEMINI_API_KEY loaded:", gemini_api_key if gemini_api_key else "❌ Not Found")

if not gemini_api_key:
    print("❌ Error: GEMINI_API_KEY is not set in your .env file.")
    exit(1)

# Initialize the diagnosis agent
diagnosis_agent = Agent(
    name="DiagnosisAgent",
    port=8001,
    endpoint=["http://127.0.0.1:8001"],
    seed="diagnosis secret phrase",
    public=True
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

    try:
        response = requests.post(
            f"{gemini_url}?key={gemini_api_key}",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            data = response.json()
            print("✅ Gemini response received.")
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print(f"❌ Gemini API error {response.status_code}: {response.text}")
            return f"❌ Gemini API error {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return f"❌ Request error: {e}"
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return f"❌ Unexpected error: {e}"

# Listen for incoming IPFS messages
@diagnosis_agent.on_message(IPFSMessage)
async def handle_ipfs(ctx: Context, message: IPFSMessage):
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
        ctx.logger.info(f"📋 Diagnosis: {diagnosis_text}")

        # Save diagnosis to JSON
        output_path = "diagnosis_output.json"
        with open(output_path, "w") as f:
            json.dump({"diagnosis": diagnosis_text}, f)

        # Upload the diagnosis file to IPFS using Storacha
        if os.path.exists(output_path):
            os.system("w3 space use diagnosis_space")
            os.system(f"w3 up {output_path}")
            ctx.logger.info("✅ Diagnosis completed and uploaded to IPFS.")
        else:
            ctx.logger.error("❌ Diagnosis output file not found.")

    except requests.exceptions.RequestException as e:
        ctx.logger.error(f"❌ Request failed: {e}")
    except Exception as e:
        ctx.logger.error(f"❌ Unexpected error: {e}")

# Start the agent
if __name__ == "__main__":
    diagnosis_agent.run()

