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
