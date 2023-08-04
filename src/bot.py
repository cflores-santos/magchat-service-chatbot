import json
import os
import spacy
import re

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the JSON file
faqs_json_path = os.path.join(current_directory, "../data/FAQs.json")

# Load the JSON file
with open(faqs_json_path) as file:
    faq_data = json.load(file)


def bot_handler():
    print("Bot: Welcome! Please enter your question.")

    while True:
        user_message = input("User: ")

        # Preprocess the user's message
        user_message = user_message.lower()
        # Remove leading/trailing spaces
        user_message = user_message.strip()
        # Remove punctuation
        user_message = re.sub(r"\?", "", user_message)

        # Initialize variables for best match tracking
        best_match_score = 0
        best_match_answer = None

        # Process the user's message with SpaCy
        doc = nlp(user_message)

        # Search for the corresponding answer
        for topic in faq_data["help-topics"]:
            for faq in topic["faqs"]:
                # Preprocess the FAQ question
                faq_question = faq["question"].lower()
                # Remove leading/trailing spaces
                faq_question = faq_question.strip()
                # Remove punctuation
                faq_question = re.sub(r"\?", "", faq_question)

                # Process the FAQ question with SpaCy
                faq_doc = nlp(faq_question)

                # Calculate the similarity score
                similarity = doc.similarity(faq_doc)

                # Update the best match if a better match is found
                if similarity > best_match_score:
                    best_match_score = similarity
                    best_match_answer = faq["answer"]

        # Check if a match was found and the similarity score exceeds a threshold
        if best_match_score >= 0.75:  # Adjust the similarity threshold as needed
            print("Bot:", best_match_answer)
        else:
            print("Bot: Sorry, I couldn't find a matching answer.")

        # Add additional logic or conditions as needed


if __name__ == "__main__":
    bot_handler()
