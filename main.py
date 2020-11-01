from mongoengine import *
from datetime import datetime
import json
import os

connect("mongo-dev-db")

# Defining Documents

class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField()
    bio = StringField(required=100)
    categories = ListField()
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "admin": self.admin,
            "registered": self.registered
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-date_created"]
    }

# Dynamic documents

class BlogPost(DynamicDocument):
    item = StringField()
    content = StringField()
    author = ReferenceField(User)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["title"],
        "ordering": ["-date_created"]
    }

# save a document 

'''user = User(
    username= "SmithChris",
    email= "smithchris@gmail.com",
    password=os.urandom(16),
    age=25,
    bio="Working on projects!",
    admin=True
).save()

BlogPost(
    title="MongoDB and Python blog post!",
    content="MongoDB and Python is Awesome!!!",
    author=user,
    tags=["Python", "MongoBD", "Mongoengine"],
    category="MongoBD"
).save()'''

user = User(
    username= "PeterPan",
    email= "peter@gmail.com",
    password=os.urandom(16),
    age=25,
    bio="Peter is an acrobat!",
)

user.admin = True
user.registered = True

# Uncomment to save the data
'''try:
    user.save()
except NotUniqueError:
    print("Username, email or bio is not unique")'''


# Querying the database

'''users = User.objects()
#print(users)

for user in users:
    print(user.username, user.email, user.bio)'''

#Filtering

'''admin_users = User.objects(admin=True, registered=True)

for a in admin_users:
    print(a.username, a.email)'''

#Filtering by single user

'''try:
    peter_pan = User.objects(username="PeterPan").get()
    # e.g. could be used for Validate password
    print(peter_pan.username, peter_pan.email) 
except DoesNotExist:
    print("User not found")'''

'''smith_chris = User.objects(username="SmithChris").get()
#print(jona_jay.username)

posts = BlogPost.objects(author=smith_chris)

for post in posts:
    print(post.author.username)'''

# Query operators

# Less than & greater than / or equal to - (lt,lte,gt,gte)

# Less than or equal to
'''young_users = User.objects(age__lt=30)

for young_user in young_users:
    print(young_user.username, young_user.age)'''

# Greater than or equal to
'''old_users = User.objects(age__gte=22)

for old_user in old_users:
    print(old_user.username, old_user.age)'''


# Query list

'''posts_tagged_python = BlogPost.objects(tags="Python")
   # another example: posts_tagged_python = BlogPost.objects(tags__in=["Python", "MongoDB"])
for post in posts_tagged_python:
    print(post.content, post.tags)'''


# String query

# Content
'''python_posts = BlogPost.objects(content__contains="Python")

for post in python_posts:
    print(post.content)'''

# Title
'''python_posts = BlogPost.objects(title__contains="MongoDB")

for post in python_posts:
    print(post.title)'''

# Limitting and skipping results

# Get the first 

'''first = BlogPost.objects().first()
print(first.title)'''

# Get the first two documents

'''first_2 = BlogPost.objects()[:2]

for post in first_2:
    print(post.title)'''

# Get all but first two 

'''all_but = BlogPost.objects()[2:]

for post in all_but:
    print(post.title)'''

# slicing

'''sliced = BlogPost.objects()[2:4]

for post in sliced:
    print(post.title)'''

# Counting 

'''user_count = User.objects().count()
print(user_count)'''

# Aggregation

# Add rating to BlogPost to see average operation
'''average = BlogPost.objects.average("rating")
print(average)'''

'''total_rating = BlogPost.objects.sum("rating")
print(total_rating)'''

# Some json work for ideas
smith_chris = User.objects(username="SmithChris").get()
print(smith_chris.json())
