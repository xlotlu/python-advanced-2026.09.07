# Write a function that receives two texts and returns a set of common words:
# get_commmon_words("good morning everyone", "everyone was good today")
# should return {"good", "everyone"}


def get_common_words(text1, text2):
    set1 = set(text1.split())
    set2 = set(text2.split())
    return set1 & set2


print(get_common_words("good morning everyone", "everyone was good today"))
