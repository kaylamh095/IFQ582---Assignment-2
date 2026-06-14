class CommunityElder:
    # Constructor
    def __init__(self, community_elder_id, full_name, community_name, email):
        self.community_elder_id = community_elder_id
        self.full_name = full_name
        self.community_name = community_name
        self.email = email


    # Get community elder details
    def get_community_elder_details(self):
        return {
            "Community Elder ID": self.community_elder_id,
            "Full Name": self.full_name,
            "Community Name": self.community_name,
            "Email": self.email
        }


    # __repr__ 
    def __repr__(self):
        return (
            f"\nCommunity Elder\n"
            f"------------------------\n"
            f"ID: {self.community_elder_id}\n"
            f"Name: {self.full_name}\n"
            f"Community: {self.community_name}\n"
            f"Email: {self.email}\n"
        )


    # Review item
    def review_item(self, item):
        print(f"\n{self.full_name} is reviewing item:")
        print(f"Item ID: {item.item_id} | Title: {item.title}")


    # Record outcome decision 
    def record_outcome_decision(self, review, outcome, notes):
        review.update_outcome(outcome)
        review.add_notes(notes)
        print(f"{self.full_name} has recorded a decision.")
