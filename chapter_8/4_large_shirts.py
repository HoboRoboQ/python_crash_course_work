def make_shirt(message='I love Python', size='large'):
    """Summarize the shirt that's going to be made."""
    print(f"Size: {size}")
    print(f"It will say '{message}.'")

make_shirt()
make_shirt(size='medium')
make_shirt('Platonic Platinum', 'small')