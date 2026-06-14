from app.models.AccessRequest import AccessRequest

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
