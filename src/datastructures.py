"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # Métodos ya implementados (add_member, delete_member, get_member, get_all_members)

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # Ensure the member has an ID, generate one if not provided
        if "id" not in member:
            member["id"] = self._generate_id()
        # Add the last name if not provided
        if "last_name" not in member:
            member["last_name"] = self.last_name
        # Append the member to the list
        self._members.append(member)

    def delete_member(self, id):
        # Filter out the member with the given ID
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        # Find and return the member with the given ID
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members