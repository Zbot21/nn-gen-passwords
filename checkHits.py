
possiblePasswords = set()
with open("generated/permuted_removed_repeats.out") as testFile:
    for line in testFile:
        possiblePasswords.add(line.rstrip())

print("Loaded %d generated passwords" % len(possiblePasswords))

actualPasswords = set()
with open("password_lists/crackstation-human-only.txt", errors='ignore') as targetFile:
    for line in targetFile:
        actualPasswords.add(line.rstrip())

print("Loaded %d from password list" % len(actualPasswords))

sharedPasswords = set()
for potential in possiblePasswords:
    if potential in actualPasswords:
        sharedPasswords.add(potential)

print("Found: %d shared passwords" % len(sharedPasswords))
print("Hit Percentage: %f" % (len(sharedPasswords) / len(possiblePasswords)))
with open("generated/shared_passwords_from_permuted.out", "w") as outfile:
    outfile.write("\n".join(sharedPasswords))

