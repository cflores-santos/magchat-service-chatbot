
import json
import os
import spacy
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
faqs_json_path = os.path.join(current_directory, "../data/FAQs.json")

# Load the JSON file
with open(faqs_json_path) as file:
    faq_data = json.load(file)

# Load the DialoGPT model and tokenizer
dialoGPT = "gpt2"
model = GPT2LMHeadModel.from_pretrained(dialoGPT)
tokenizer = GPT2Tokenizer.from_pretrained(dialoGPT)

# Set the model to evaluation mode
model.eval()


def generate_dialogpt_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    response = model.generate(
        inputs, max_length=250, pad_token_id=tokenizer.eos_token_id
    )
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)
    return response_text


def bot_handler():
    print("Welcome! Please enter your question.")

    while True:
        user_message = input("User: ")

        # Process the user's message with SpaCy
        doc = nlp(user_message)

        # Search for the corresponding answer
        for topic in faq_data["help-topics"]:
            for faq in topic["faqs"]:
                # Process the FAQ question with SpaCy
                faq_question = faq["question"].lower()
                faq_doc = nlp(faq_question)

                # Compare the processed question and FAQ question
                similarity = doc.similarity(faq_doc)
                if similarity >= 0.8:  # Adjust the similarity threshold as needed
                    print("Bot:", faq["answer"])
                    break

            if similarity >= 0.8:
                break
        else:
            # No matching FAQ found, generate response using DialoGPT
            dialogpt_response = generate_dialogpt_response(user_message)
            print("Bot:", dialogpt_response)


if __name__ == "__main__":
    bot_handler()
