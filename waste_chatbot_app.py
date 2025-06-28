import streamlit as st
import json

# Load the waste data
with open("waste_segregation_starter.json", "r") as f:
    waste_data = json.load(f)

# Preprocess data into a dictionary
waste_lookup = {}
for item in waste_data:
    waste_lookup[item["item"].lower()] = item

# Function to get response
def get_response(user_input):
    user_input = user_input.strip().lower()
    for key in waste_lookup:
        if key in user_input:
            item = waste_lookup[key]
            return f"'{item['item']}' is categorized as *{item['category']}* waste.\nDisposal advice: {item['disposal']}"
    return "Sorry, I couldn't find that item. Try something like 'banana peel' or 'plastic bottle'."

# Streamlit app UI
st.title("WasteSegBot - Waste Segregation Assistant")
st.write("Ask me how to dispose of household waste items properly.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.text_input("Your question:", key="input")

if user_input:
    response = get_response(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**{sender}:** {msg}")
    else:
        st.markdown(f"> **{sender}:** {msg}")
