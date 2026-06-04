from datetime import datetime

class AccessReview:
    # Constructor
    def __init__(self, review_id, review_notes, access_outcome, item):
        self.review_id = review_id
        self.review_notes = review_notes
        self.access_outcome = access_outcome
        self.review_timestamp = datetime.now()   # current date and time
        self.item = item

    # Get AccessReview details
    def get_access_review_details(self):
        return {
            "Review ID": self.review_id,
            "Review Notes": self.review_notes,
            "Access Outcome": self.access_outcome,
            "Review Timestamp": self.review_timestamp
        }


    # __repr__ 
    def __repr__(self):
        return (
            f"\nAccess Review\n"
            f"------------------------\n"
            f"Review ID: {self.review_id}\n"
            f"Item ID: {self.item.item_id}\n"
            f"Notes: {self.review_notes}\n"
            f"Outcome: {self.access_outcome}\n"
            f"Timestamp: {self.review_timestamp}\n"
        )


    # Record outcome (initial setting)
    def record_outcome(self, outcome):
        self.access_outcome = outcome
        self.review_timestamp = datetime.now()
        print("Access outcome recorded.")


    # Update outcome (change existing outcome)
    def update_outcome(self, new_outcome):
        self.access_outcome = new_outcome
        self.review_timestamp = datetime.now()
        print("Access outcome updated.")


    # Add notes
    def add_notes(self, new_notes):
        self.review_notes = self.review_notes + " | " + new_notes
        self.review_timestamp = datetime.now()
        print("Notes added.")
