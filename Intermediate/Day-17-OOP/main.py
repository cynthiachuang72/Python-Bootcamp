# PascalCase: First letter capitalized
# camelCase: First letter of first word is lower case and the rest are capitalized
# snake_case: All words are lower case connected by underscore
class User:
    def __init__(self, user_id, username):
        # Create the starting values of the object
        # Always get triggered every time the object is created
        self.id = user_id
        self.username = username
        self.followers = 0  # Set to a default value
        self.following = 0

    # Create methods to change certain attributes
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Cynthia")
# Creating attributes, they are variables associated with certain objects
# user_1.id = "001"
# user_1.username = "cynthia"

print(user_1.id, " ", user_1.username)

user_2 = User("002", "Brian")
# user_2.id = "002"
# user_2.username = "jack"

print(user_2.id, " ", user_2.username)


user_1.follow(user_2)
print("User 1 followers count = ", user_1.followers)
print("User 1 following counts = ", user_1.following)
print("User 2 followers count = ", user_2.followers)
print("User 2 following counts = ", user_2.following)