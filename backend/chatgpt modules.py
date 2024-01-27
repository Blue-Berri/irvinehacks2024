from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system", 
      "content": "You are a matchmaker. I will you a set of traits about a person and give you a list of possible matches. your job is to find the best matches for the person. Refer to the use in the you form. Format entire response in the JSON format: { results: {name}, {age}, {gender}, {sexual orientation}, {major},  {bio} }" 
     },
    {
      "role": "user", 
      "content": "Me: 18, Male, Male, Computer Science,  I love to code! "
    }
  ]
)

print(completion.choices[0].message)