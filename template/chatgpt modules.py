from openai import OpenAI
import json 
client = OpenAI(api_key="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")
data = {}
you = {}
with open("template/userData.json", "r") as file:
    data = json.load(file)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system", 
      "content": f'''You are a matchmaker. I will give you a set of traits about me and give you a
        list of possible matches in the json file {data}. Match gender and sexual orientation as the
        highest priority with a weight of over 90%. If orientation is straight that means males like females 
        and females like males. 
        Your job is to find the best matches for the person. Go through the entire list of data in the json.
        Refer to the use in the you form. Give back list of only names in order from highest match to 
        lowest match. return in json format: {"name", "gender", "sexual orientation", "age", "major", "bio"} dont include 
      other words '''
     },
    {
      "role": "user", 
      "content": f'''Here is a json file {you} of your information. Only consider the factors stated above.
      return in json format: {"name", "gender", "sexual orientation", "age", "major", "bio"} dont include 
      other words'''
    }
  ]
)

results = completion.choices[0].message.content
with open("backend/matches.json", 'w') as json_file:
    json.dump(results, json_file)


print(results)

