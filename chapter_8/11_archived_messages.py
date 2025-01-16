def show_messages(messages):
    """Print all messages in the list."""
    print("\nShowing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print message and then move to sent"""
    print("\n Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal list:")
print(messages)
print(sent_messages)