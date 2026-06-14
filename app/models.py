from datetime import datetime

class AccessRequest:
    # Constructor
    def __init__(self, request_id, request_reason, item):
        self.request_id = request_id
        self.request_reason = request_reason
        self.request_status = "Draft"   # default status
        self.request_timestamp = datetime.now()   # current date/time
        self.item = item

    # Get AccessRequest details
    def get_access_request_details(self):
        return {
            "Request ID": self.request_id,
            "Item ID": self.item.item_id,
            "Request Reason": self.request_reason,
            "Request Status": self.request_status,
            "Request Timestamp": self.request_timestamp
        }


    # __repr__ 
    def __repr__(self):
        return (
            f"\nAccess Request\n"
            f"------------------------\n"
            f"Request ID: {self.request_id}\n"
            f"Item ID: {self.item.item_id}\n"
            f"Reason: {self.request_reason}\n"
            f"Status: {self.request_status}\n"
            f"Timestamp: {self.request_timestamp}\n"
        )


    # Submit request
    def submit_request(self):
        self.request_status = "Submitted"
        self.request_timestamp = datetime.now()
        print("Access request submitted.")


    # Cancel request
    def cancel_request(self):
        self.request_status = "Cancelled"
        self.request_timestamp = datetime.now()
        print("Access request cancelled.")

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


class LibraryCurator:
    # Constructor
    def __init__(self, curator_id, full_name, email):
        self.curator_id = curator_id
        self.full_name = full_name
        self.email = email
        self.collection_items = []   


    #  Get curator details
    def get_curator_details(self):
        return {
            "Curator ID": self.curator_id,
            "Full Name": self.full_name,
            "Email": self.email
        }


    #  __repr__ 
    def __repr__(self):
        return (
            f"\nLibrary Curator\n"
            f"------------------------\n"
            f"ID: {self.curator_id}\n"
            f"Name: {self.full_name}\n"
            f"Email: {self.email}\n"
            f"Number of Items Managed: {len(self.collection_items)}\n"
        )


    # Add item
    def add_item(self, item):
        self.collection_items.append(item)
        print("Item added successfully.")


    # Edit item (simple example: update title)
    def edit_item(self, item_id, new_title):
        for item in self.collection_items:
            if item.item_id == item_id:
                item.title = new_title
                print("Item updated successfully.")
                return
        print("Item not found.")


    #  View review status of all items
    def view_review_status(self):
        print("\nReview Status of Items")
        print("------------------------")

        for item in self.collection_items:
            print(f"Item ID: {item.item_id} | Title: {item.title} | Review Status: {item.review_status}")


class PublicUser:
    # Constructor
    def __init__(self, public_user_id, full_name, email):
        self.public_user_id = public_user_id
        self.full_name = full_name
        self.email = email


    # Get PublicUser details
    def get_public_user_details(self):
        return {
            "Public User ID": self.public_user_id,
            "Full Name": self.full_name,
            "Email": self.email
        }


    #  __repr__ 
    def __repr__(self):
        return (
            f"\nPublic User\n"
            f"------------------------\n"
            f"ID: {self.public_user_id}\n"
            f"Name: {self.full_name}\n"
            f"Email: {self.email}\n"
        )


    # View approved item
    def view_approved_item(self, item):
        if item.access_status == "Open":
            print(f"\nViewing Item: {item.title}")
            print(f"Description: {item.description}")
        else:
            print("Item is not available for public access.")


    # Request access (creates AccessRequest)
    def request_access(self, request_id, reason, item):
        request = AccessRequest(request_id, reason, item)
        item.add_access_request(request)

        print(f"{self.full_name} has submitted an access request.")
        return request
