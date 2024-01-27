from openai import OpenAI
client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", 
     "content": "You are a matchmaker. I will you a set of traits about a person and give you a list of possible mathces."
     "your job is to find the best matches for the person. Refer to the use in the you form. Format entire response in the JSON format: { results: name, age, major, gender, sexual orientation, bio }" },
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)


print(completion.choices[0].message)