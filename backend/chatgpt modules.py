from openai import OpenAI
import json 
client = OpenAI(api_key="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")
data = {}
with open("backend/userData.json", "r") as file:
    data = json.load(file)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system", 
      "content": f'You are a matchmaker. I will you a set of traits about a person and give you a list of possible matches in the json file {data}. your job is to find the best matches for the person. Refer to the use in the you form. Format entire response in the JSON format:  results: name, age, gender, sexual orientation, major,  bio ' 
     },
    {
      "role": "user", 
      "content": "Me: 18, Male, Male, Computer Science,  I love to code!"
    }
  ]
)

results = completion.choices[0].message

print(completion.choices[0].message)