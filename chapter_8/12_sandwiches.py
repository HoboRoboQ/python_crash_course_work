def sandwich_builder(*fillings):
    """Print list of requested fillings"""
    print("\nMaking you a sick as heck sandwich!")
    for filling in fillings:
        print(f"...adding {filling} now.")

sandwich_builder('ham', 'cheese','mayo')
sandwich_builder('chicken', 'honey mustard')
sandwich_builder('toast')