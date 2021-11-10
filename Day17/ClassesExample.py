class Practice:
    def __init__(self, userid, username):
        self.id = userid
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = Practice("001", "Niha")
user2 = Practice("002", "Kowshi")
user3 = Practice("003", "Chandu")
user4 = Practice("004", "Nikki")
user5 = Practice("005", "Kamal")
user6 = Practice("006", "Deepu")
user7 = Practice("007", "Teja")
user8 = Practice("008", "Keerthi")
user9 = Practice("009", "Pranavi")
user10 = Practice("010", "Ritvik")
user11 = Practice("011", "Yatika")
user2.follow(user1)
user3.follow(user1)
user4.follow(user2)
print(user1.followers)
print(user2.following, " , ", user2.followers)
