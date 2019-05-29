import random

responses = {
    "question":[
        "You tell me!",
        "I don't know"
    ]
    ,
    "statement":[
        ":)",
        "How's that possible?",
        "It's not like yesterday then!"
    ]
}


def respond(message):
    # Check for a question mark
    if message[-1] != "?":
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


if __name__ == "__main__":
    # Send messages ending in a question mark
    send_message("what's today's weather?")
    send_message("what's today's weather?")

    # Send messages which don't end with a question mark
    send_message("I love building chatbots")
    send_message("I love building chatbots")
