import json

# Load the waste data
with open("waste_segregation_starter.json", "r") as f:
    waste_data = json.load(f)

# Preprocess data into a dictionary for quick lookup

waste_lookup = {}
for item in waste_data:
    waste_lookup[item["item"].lower()] = item

# Simple chatbot loop
print("  Welcome to WasteSegBot! Ask me how to dispose of an item.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "exit":
        print("Bot: Thanks for using WasteSegBot! Stay eco-friendly. 🌍")
        break
    found = False
    for key in waste_lookup:
        if key in user_input:
            item = waste_lookup[key]
            print(f"Bot: '{item['item']}' is categorized as *{item['category']}* waste.")
            print(f"     Disposal advice: {item['disposal']}\n")
            found = True
            break
    if not found:
        print("Bot: Sorry, I couldn't find that item. Try something like 'banana peel' or 'plastic bottle'.\n")
