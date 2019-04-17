from collections import Counter
from collections import defaultdict

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

print( users )

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1),
    (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

for user in users:
    friends = ( friend['name'] for friend in user['friends'] )
    print( user['name'] + '\'s friends:   \t(%s)' % ', '.join(map(str, friends)))

def number_of_friends( user ):
    return len( user['friends'])

total_connections = sum( number_of_friends( user) for user in users )
number_of_users = len(users)
average_connections = total_connections / number_of_users
number_of_friends_byId = [( user['id'], number_of_friends( user ), user['name'] ) for user in users ]
number_of_friends_byId = sorted( number_of_friends_byId, key = lambda list: list[1], reverse = True )

print( 'Number of connections per user sorted by connections (desc): ' + str(number_of_friends_byId))
print( 'Average of connections: ' + str(average_connections) )

def friends_of_friend_ids(user):
    return Counter(friend_of_a_friend["id"]
        for friend in user["friends"] # for each of my friends
        for friend_of_a_friend in friend["friends"] # count *their* friends
        if not_the_same_user(user, friend_of_a_friend) # who aren't me
        and not_friends(user, friend_of_a_friend))

def not_the_same_user(user, other_user):
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    return all(not_the_same_user(friend, other_user)
        for friend in user["friends"])

print( 'Friends of friends for ' + users[3]['name'] + ': ' + str( friends_of_friend_ids( users[3] ) ) )

def data_scientists_who_like(target_interest):
    return [user_id
        for user_id, user_interest in interests
        if user_interest == target_interest]

'''build an index from interests to users'''
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

'''build an index from users to interests'''
interests_by_userId = defaultdict(list)
for user_id, interest in interests:
    interests_by_userId[user_id].append(interest)

def who_has_most_common_interest_with(user):
    return Counter( interested_userId
        for interest in interests_by_userId[user['id']]
        for interested_userId in user_ids_by_interest[interest]
        if interested_userId != user['id'])
    
print( 'Data scientists who like \'machine learning\': ' + str( data_scientists_who_like( 'machine learning' ) ) )

print( 'Data scientist with more interest in common with ' + users[3]['name'] + ': ' + str( who_has_most_common_interest_with( users[3] ) ) )