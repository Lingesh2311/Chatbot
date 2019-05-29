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


if __name__ == "__main__":
    # Send messages ending in a question mark
    send_message("what's today's weather?")
    send_message("what's today's weather?")

    # Send messages which don't end with a question mark
    send_message("I love building chatbots")
    send_message("I love building chatbots")
