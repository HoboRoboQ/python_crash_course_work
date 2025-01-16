class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store question, prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show responses that have been given."""
        print("Survey results:")
        for responses in self.responses:
            print(f"- {responses}")