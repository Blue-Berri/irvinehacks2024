from openai import OpenAI
import json 
import json
client = OpenAI(api_key="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")
data = {}

    # Load the data from the JSON file
with open("template/userData.json", "r") as file:
  data = json.load(file)

    # Create a new list of dictionaries with email, gender, and orientation
  new_data = []
  for item in data['users']:
    new_item = {
      "email": item["email"],
      "gender": item["gender"],
      "orientation": item["orientation"]
    }
    new_data.append(new_item)

current = {
    "email": item["email"],
    "gender": item["gender"],
    "orientation": item["orientation"]
}

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {
#       "role": "system", 
#       "content": f'''You are a matchmaker. I will give you a set of traits about me and give you a
#         list of possible matches in the json file {new_data}. Match gender and sexual orientation as the
#         highest priority with a weight of over 90%. If orientation is straight that means males like females 
#         and females like males. 
#         Your job is to find the best matches for the person. Go through the entire list of data in the json.
#         Refer to the use in the you form. Give back list of only names in order from highest match to 
#         lowest match. python list of emails. The list must have at least 15 emails. format it as [emails]. dont include 
#       other words '''
#      },
#     {
#       "role": "user", 
#       "content": f'''Here is a json file {current} of your information. Only consider the factors stated above.
#       return in python list of emails. The list must have at least 15 emails. format it as [emails]  do not include any other words '''
#     }
#   ]
# )

results = ["r@uci","taylor@abc.edu","emily@gmail.com","tae@awesome.cool"]


with open("template/userData.json", "r") as file:
  data = json.load(file)

match_list = []
for email in results:
  match_data = dict()
  for user_bruh in data["users"]:
    if email == user_bruh["email"]:
      match_data.update(user_bruh)
      match_list.append(match_data)
      break
      
print(match_list)
      
final_match = {"users": match_list}
with open("template/matches.json", 'w') as json_file:
    json_file.write(json.dumps(final_match,))




# print(results)

