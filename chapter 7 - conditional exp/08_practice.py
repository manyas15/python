# a spam comment is defined as a text containing the words "make a lot of money", "buy now", "subscribe this", or "click this"
# write a program to detect these spam comments
# in this program "in" operator is used to check if a substring is present in a string or not

s1 = "make a lot of money"
s2 = "buy now"
s3 = "subscribe this"
s4 = "click this"

message = input("enter comment: ")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# we have made a kind of spam filter here
# this kind of logics are written in social media platforms to detect spam comments and block them 