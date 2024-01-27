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
      "content": f'You are a matchmaker. I will you a set of traits about me and give you a list of possible matches in the json file {data}. Match gender first. Then orientation. Then match around the same age. Then similar bio. Then major your job is to find the best matches for the person. Go through the whole list. Refer to the use in the you form. Format entire response in the JSON format:  results: name, age, gender, sexual orientation, major,  bio ' 
     },
    {
      "role": "user", 
      "content": "Me: 18, Male, Straight, Computer Science,  I love to code!"
    }
  ]
)

results = completion.choices[0].message

print(completion.choices[0].message)