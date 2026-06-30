
class Item:
    # Constructor
    def __init__(self, item_id, title, description, image_link,
                 item_category, cultural_group, sensitivity_notes, 
                 review_status, access_level):

        self.item_id = item_id
        self.title = title
        self.description = description
        self.image_link = image_link
        self.item_category = item_category
        self.cultural_group = cultural_group
        self.sensitivity_notes = sensitivity_notes
        self.review_status = review_status
        self.access_status = access_level
        self.access_reviews = []
        self.access_requests = []    

    # Get item details
    def get_item_details(self):
        return {
            "ID": self.item_id,
            "Title": self.title,
            "Description": self.description,
            "Image Link": self.image_link,
            "Category": self.item_category,
            "Cultural Group": self.cultural_group,
            "Sensitivity Notes": self.sensitivity_notes,
            "Review Status": self.review_status,
            "Access Level": self.access_level
        }

 
    def __repr__(self):
        return (
            f"\nCollection Item\n"
            f"------------------------\n"
            f"ID: {self.item_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Image Link: {self.image_link}\n"
            f"Category: {self.item_category}\n"
            f"Cultural Group: {self.cultural_group}\n"
            f"Sensitivity Notes: {self.sensitivity_notes}\n"
            f"Review Status: {self.review_status}\n"
            f"Access Level: {self.access_level}\n"
        )


    # Display details
    def display_details(self):
        print("Collection Item Details")
        print("----------------------")
        for key, value in self.get_item_details().items():
            print(key + ":", value)


    # Update access level
    def update_access_level(self, new_level):
        self.access_level = new_level
        print("Access level updated to:", new_level)


    # Submit for review (boolean)
    def submit_for_review(self):
        self.review_status = "Pending Review"
        return True

    # link a review to item
    def add_access_review(self, review):
        self.access_reviews.append(review)
        print("Access review added to item.")

    # view all reviews
    def view_access_reviews(self):
        print(f"\nAccess Reviews for Item ID: {self.item_id}")
        print("------------------------")

        for review in self.access_reviews:
            print(review)

    # link request to item
    def add_access_request(self, request):
        self.access_requests.append(request)
        print("Access request added to item.")

    # view all access requests
    def view_access_requests(self):
        print(f"\nAccess Requests for Item ID: {self.item_id}")
        print("------------------------")

        for request in self.access_requests:
            print(request)



