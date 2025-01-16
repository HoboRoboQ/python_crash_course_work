"""Functions related to printing 3D models"""

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until there are none left. Move each
    design to completed_models after printing."""

    while unprinted_designs:
        current_models = unprinted_designs.pop()

        # Simulate a 3D print from the design
        print(f"Printing model: {current_models}")
        completed_models.append(current_models)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)