###1-masala

# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#         natija=list(filter(lambda x: x >= passingGrade, grades))
#         return len(natija)


# grades = [45, 60, 75, 30, 90]
# passingGrade = 60

# print(count_passing_students(grades, passingGrade))

##2-masala

# def ends_with_gram(words: list[str]) -> list[str]:
#     natija = list(filter(lambda x: x.lower().endswith("gram"), words))
#     return natija


# words = ["telegram", "Instagram", "hello", "proGram", "diagram", "world"]

# print(ends_with_gram(words))

##3-masala

# def find_top_three_numbers_sorted(data: list) -> list:

#     natija=[tuple(sorted(x, reverse=True)[:3]) for x in data]
#     return natija




# data = [(10, 20, 30, 11), (5, 15), (40,), (7, 8, 50, 3)]
# print(find_top_three_numbers_sorted(data))

##4-masala

# def calculate_painting_time(pattern: list) -> int: 
#     natija=0

#     for i in range(len(pattern)):
#         natija+=2
#         if i < len(pattern) - 1 and pattern[i] != pattern[i+1]:
#             natija += 1

#     return natija

# pattern = ["Red", "Blue", "Red", "Blue", "Red"] 
# print(calculate_painting_time(pattern)) 

##5-masala

def find_nearest_vowel(letter: str) -> str:
    if len(letter) != 1 or letter not in "abcdefghijklmnopqrstuvwxyz":
        return "faqat bitta kichik harf bo‘lishi kerak"

    unlilar = "aeiou"
    natija = "a"

    for i in unlilar:
        if abs(ord(letter) - ord(i)) < abs(ord(letter) - ord(natija)):
            natija = i

    return natija


harf=input("Harf kiriting: ")
print(find_nearest_vowel(harf))


