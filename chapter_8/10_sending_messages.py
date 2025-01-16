def show_messages(unsent_messages, sent_messages):
    """Prints a list of messages and send to new list"""
    for message in unsent_messages:
        sending_message = unsent_messages.pop()
        print(sending_message)
        sent_messages = sending_message.pop()

unsent_messages = ["hello there", "how are u?", ":)"]
sent_messages = []

show_messages(unsent_messages, sent_messages)

print(sent_messages)