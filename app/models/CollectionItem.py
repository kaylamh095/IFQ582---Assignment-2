
class CollectionItem:
    # Constructor
    def __init__(self, item_id, title, description, image_link,
                 item_type, item_category, review_status,
                 access_status, access_considerations, sensitivity_level):

        self.item_id = item_id
        self.title = title
        self.description = description
        self.image_link = image_link
        self.item_type = item_type
        self.item_category = item_category
        self.review_status = review_status
        self.access_status = access_status
        self.access_considerations = access_considerations
        self.sensitivity_level = sensitivity_level
        self.access_reviews = []
        self.access_requests = []    

    # Get item details
    def get_item_details(self):
        return {
            "ID": self.item_id,
            "Title": self.title,
            "Description": self.description,
            "Image Link": self.image_link,
            "Type": self.item_type,
            "Category": self.item_category,
            "Review Status": self.review_status,
            "Access Status": self.access_status,
            "Access Considerations": self.access_considerations,
            "Sensitivity Level": self.sensitivity_level
        }

 
    def __repr__(self):
        return (
            f"\nCollection Item\n"
            f"------------------------\n"
            f"ID: {self.item_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Image Link: {self.image_link}\n"
            f"Type: {self.item_type}\n"
            f"Category: {self.item_category}\n"
            f"Review Status: {self.review_status}\n"
            f"Access Status: {self.access_status}\n"
            f"Access Considerations: {self.access_considerations}\n"
            f"Sensitivity Level: {self.sensitivity_level}\n"
        )


    # Display details
    def display_details(self):
        print("Collection Item Details")
        print("----------------------")
        for key, value in self.get_item_details().items():
            print(key + ":", value)


    # Update access status
    def update_access_status(self, new_status):
        self.access_status = new_status
        print("Access status updated to:", new_status)


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



