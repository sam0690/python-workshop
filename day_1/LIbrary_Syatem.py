from datetime import datetime, timedelta

# Base Class
class LibraryItem:
    def __init__(self, title, item_id):
        self._title = title
        self._item_id = item_id
        self._is_borrowed = False

    @property #read only attribute
    def title(self):
        return self._title

    @property
    def item_id(self):
        return self._item_id

    @property
    def is_borrowed(self):
        return self._is_borrowed

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_item(self):
        self._is_borrowed = False


# Derived Classes
class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self._author = author
        self._pages = pages

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self._director = director
        self._duration = duration  # in minutes

    @property
    def director(self):
        return self._director

    @property
    def duration(self):
        return self._duration


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self._issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number


# Member Class
class Member:
    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name
        self._borrowed_items = {}

    @property
    def member_id(self):
        return self._member_id

    @property
    def name(self):
        return self._name

    def borrow_item(self, item: LibraryItem):
        if item.is_borrowed:
            print(f"'{item.title}' is already borrowed.")
            return False
        if item.borrow():
            due_date = datetime.now() + timedelta(days=14)
            self._borrowed_items[item.item_id] = (item, due_date)
            print(f"{self._name} borrowed '{item.title}' (Due: {due_date.date()})")
            return True
        return False

    def return_item(self, item_id):
        if item_id in self._borrowed_items:
            item, due_date = self._borrowed_items.pop(item_id)
            item.return_item()
            print(f"{self._name} returned '{item.title}'")
        else:
            print("No such item borrowed.")

    def list_borrowed_items(self):
        print(f"\n{self._name}'s Borrowed Items:")
        for item, due in self._borrowed_items.values():
            print(f" - {item.title} (Due: {due.date()})")
        if not self._borrowed_items:
            print(" - No items borrowed.")


# ----------- TESTING CODE -----------
if __name__ == "__main__":
    # Create items
    b1 = Book("Python Programming", "B101", "John Doe", 500)
    d1 = DVD("Inception", "D202", "Christopher Nolan", 148)
    m1 = Magazine("Tech Monthly", "M303", 42)

    # Create member
    alice = Member("M001", "Alice")

    # Borrow and return
    alice.borrow_item(b1)
    alice.borrow_item(d1)
    alice.borrow_item(m1)
    alice.list_borrowed_items()

    alice.return_item("B101")
    alice.list_borrowed_items()
