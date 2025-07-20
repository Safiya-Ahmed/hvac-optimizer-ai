import os
from dotenv import load_dotenv
from google.generativeai import configure, GenerativeModel

load_dotenv()  # Load variables from .env file

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

configure(api_key=api_key)

model = GenerativeModel("gemini-1.5-flash-latest")


def get_llm_explanation(temp_history):
    prompt = "You are an HVAC expert. Analyze the following temperature and energy usage data and explain the HVAC agent's behavior:\n\n"
    for day, (temp, energy) in enumerate(temp_history, 1):
        prompt += f"Day {day}: Temp={temp}, Energy={energy:.2f}\n"
    prompt += "\nExplanation:"

    try:
        # 🧠 Generate the explanation using Gemini
        response = model.generate_content(prompt)
        explanation = response.text.strip()
        print("📤 Prompt:\n", prompt)
        print("📥 LLM Response:\n", explanation)
        return explanation

    except Exception as e:
        return f"Error generating explanation: {e}"
