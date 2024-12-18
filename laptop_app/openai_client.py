import openai
import os
import json

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAIClient:
    @staticmethod
    def get_summary(data):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Erstelle eine strukturierte JSON-Zusammenfassung der folgenden Laptop-Daten: {json.dumps(data)}",
            max_tokens=150
        )
        return response.choices[0].text.strip()

    @staticmethod
    def get_final_overview(data):
        response = openai.Completion.create(
            model="gpt-4",
            prompt=f"Erstelle eine finale Übersicht über die besten und schlechtesten Laptops und Empfehlungen für verschiedene Nutzergruppen: {json.dumps(data)}",
            max_tokens=300
        )
        return response.choices[0].text.strip()
