import os
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

with open("document.txt", "r", encoding="utf-8") as file:
    document = file.read()

question = input("Ask a question about the document: ")

prompt = f"""
You are a helpful assistant.
Answer the user's question using ONLY the information in the document.
If the answer is not found in the document, reply:
"I don't know based on the document."

Document:
{document}

Question:
{question}

Answer:
"""

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

print("\nAnswer:", response.text)
