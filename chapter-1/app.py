import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

question = input("What would you like to ask ChatGPT? ")
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=question,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.8
)

answer = response["choices"][0]["text"]
print(answer)