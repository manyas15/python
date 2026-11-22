# write a func to remove a given word from a list and strip it at the same time

l = ["Harry", "Rohan" , "Manya", "an"]

def rem(l , word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem(l, "an"))

# strip means it will remove the word or a letter from start or end of the given word
