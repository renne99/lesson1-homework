import requests
import json

#Task 1: Fetch data from the API
def get_api_data():
    url = "https://www.ndosiautomation.co.za/APIDEV/groups"
    response = requests.get(url)
    data = response.json()
    print("Data fetched successfully from API.")
    return data

#Task 2: Save the data to a JSON file
def save_data_to_file(data, filename="results.txt"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to '{filename}' successfully.")

#Task 3: Read file and search for a group
def search_group():
    with open("results.txt", "r") as file:
        data = json.load(file)

    search_name = input("\nEnter the group name to search for: ")

    found = False
    for group in data["data"]:
        if group["Name"].lower() == search_name.lower():
            print(f"Group found! Name: '{group['Name']}' | ID: {group['Id']}")
            found = True
            break

    if not found:
        print(f"Error: Group '{search_name}' was not found.")

#Run all tasks
api_data = get_api_data()
save_data_to_file(api_data)
search_group()
