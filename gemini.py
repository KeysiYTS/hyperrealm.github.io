import google.generativeai as genai
import json

gemini_api_key = "AIzaSyDgxMDC9dEBHaOZx5YH0nFUKvkedZjsakk"

genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash',
                              # Set the `response_mime_type` to output JSON
                              generation_config={"response_mime_type": "application/json"})

user_input()
    prompt = input()

prompt = user_input

response = model.generate_content("escreva um review em markdown do samsumg galaxy s23")
print(response.json)