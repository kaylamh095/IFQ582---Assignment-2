class User:
    # Constructor
    def __init__(self, first_name, last_name, email, phone, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password # TODO: hash the password, possibly here


    # Get User details
    def get_public_user_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "Email": self.email
        }

    #  __repr__ 
    def __repr__(self):
        return (
            f"\User\n"
            f"------------------------\n"
            f"ID: {self.first_name}\n"
            f"Name: {self.last_name}\n"
            f"Email: {self.email}\n"
        )

