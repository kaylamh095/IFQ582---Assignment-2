class User:
    # Constructor
    def __init__(self, first_name, last_name, email, phone, password, ID=None, is_admin=None):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.email = email
        self.phone = phone
        self.password = password
        self.is_admin = is_admin

    # Get User details
    def get_user_details(self):
        return {
            "Full Name": self.full_name,
            "Email": self.email
        }

    #  __repr__ 
    def __repr__(self):
        return (
            f"Name: {self.full_name}\n"
            f"Email: {self.email}\n"
        )

