# Mapping friends to numbers for simplicity Alice: 0, Bob: 1, Carol: 2
n = 3 # number of friends
M = [[0] * n for _ in range(n)] # Adjacency Matrix

# Alice is friends with Bob and Carol
M[0][1] = M[0][2] = 1
M[1][0] = M[2][0] = 1

# Print the Matrix
for row in M:
  print(row)

# Output: [0, 1, 1], [1, 0, 0], [1, 0, 0]

# Solution 2
users = 4 # A: 0, B: 1, C: 2, D: 3
M = [[0] * users for _ in range(users)] # Adjacency Matrix

# Add friendships A-B, B-C
M[0][1] = M[1][0] = 1
M[1][2] = M[2][1] = 1

# Print adjacent matrix
print("\nFriendship zone")
for row in M:
  print(row)

# Output: [0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]

# Check for friend suggestions
for i in range(users):
  for j in range(i + 1, users):
    if i != j and M[i][j] == 0 and any(M[i][k] == 1 and M[j][k] == 1 for k in range(users)):
      print(f"Suggesting User {j} to User {i} based on mutual friends.")

# Output: Suggesting User 0 to User 2 based on mutual friends.

print("\nProject Zone")
# Number of projects
n = 7

# Initialize the adjacency matrix
M = [[0] * n for _ in range(n)]

# TODO: Map the overlapping project teams in the adjacency matrix. Consider that projects that have overlapping team members are: 
# 1) projects at indices 0 and 1
# 2) projects at indices 2 and 6 
M[0][1] = M[1][0] = 1  # Project 0 and Project 1
M[2][6] = M[6][2] = 1  # Project 2 and Project 6

# Print the adjacency matrix
for row in M:
  print(row)

print("\nSuggest Friends")
# Let's consider a different graph for 5 people: A: 0, B: 1, C: 2, D: 3, E: 4
# A is friends with B and C
# B is friends with A, C and D
# C is friends with A, B and E
# D is friends with B
# E is friends with C

# Number of people
n = 5
users = ['A', 'B', 'C', 'D', 'E']

# Initialize the adjacency matrix
M = [[0] * n for _ in range(n)]

# Map the relationships
# A
M[0][1] = M[0][2] = 1
# B
M[1][0] = M[1][2] = M[1][3] = 1
# C
M[2][0] = M[2][1] = M[2][4] = 1
# D
M[3][1] = 1
# E
M[4][2] = 1

# Print the Graph
for row in range(n):
  print(M[row])

# Suggest friends for each user, avoiding cases where users are suggested to be friends with themselves
for i in range(n):
  for j in range(n):
    if i != j:
      if M[i][j] == 0 and any(M[i][k] and M[k][j] for k in range(n)):
        print(
          f"Based on the mutual friends, "
          f"User {users[i]} and User {users[j]} may know each other."
        )