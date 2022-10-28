import requests

# Hakee jason dataa urlista
data = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
data_dict = data.json()

with open("checkpoint.txt", "w") as file_object:
    for row in data_dict["items"]:
        file_object.write("\n"f"{row['parameter']}")