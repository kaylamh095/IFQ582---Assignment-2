from datetime import datetime

class AccessRequest:
    # Constructor
    def __init__(self, request_id, item_id, member_id, request_status,review_timestamp):
        self.request_id = request_id
        self.item_id = item_id
        self.member_id = member_id
        self.request_status = request_status
        self.review_timestamp = review_timestamp

    # Get AccessRequest details
    def get_access_request_details(self):
        return {
            "Request ID": self.request_id,
            "Item ID": self.item_id,
            "Member ID": self.member_id,
            "Request Status": self.request_status,
            "Review Timestamp": self.review_timestamp
        }


    # __repr__ 
    def __repr__(self):
        return (
            f"\nAccess Request\n"
            f"------------------------\n"
            f"Request ID: {self.request_id}\n"
            f"Item ID: {self.item_id}\n"
            f"Member ID: {self.member_id}\n"
            f"Status: {self.request_status}\n"
            f"Review Timestamp: {self.review_timestamp}\n"
        )


    # Submit request
    def submit_request(self):
        self.request_status = "Submitted"
        self.review_timestamp = datetime.now()
        print("Access request submitted.")


    # Cancel request
    def cancel_request(self):
        self.request_status = "Cancelled"
        self.review_timestamp = datetime.now()
        print("Access request cancelled.")
