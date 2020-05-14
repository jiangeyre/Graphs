def add_friendship(self, user_id, friend_id):
    if user_id == friend_id:
        #print("WARNING: You cannot be friends with yourself")
        return False
    elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
        #print("WARNING: Friendship already exists")
        return False
    else:
        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True
​
def populate_graph_linear(self, num_users, avg_friendships):
    # Reset graph
    self.last_id = 0
    self.users = {}
    self.friendships = {}
​
    # Add users
    for i in range(num_users):
        self.addUser(f"User {i+1}")
​
    target_friendships = num_users * avg_friendships
​
    total_friendships = 0
    collisions = 0
​
    while total_friendships < target_friendships:
        # Keep trying to add friendships
        user_id = random.randint(1, self.last_id)
        friend_id = random.randint(1, self.last_id)
​
        if self.add_friendship(user_id, friend_id):
            total_friendships += 2
        else:
            collisions += 1
​
    print(f"COLLISIONS: {collisions}")
​
if __name__ == '__main__':
sg = SocialGraph()
​
num_users = 1000
avg_friendships = 995
​
start_time = time.time()
sg.populate_graph_linear(num_users, avg_friendships)
#sg.populate_graph(num_users, avg_friendships)
end_time = time.time()
​
print (f"runtime: {end_time - start_time:.2f} seconds")