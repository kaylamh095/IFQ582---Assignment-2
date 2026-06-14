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
