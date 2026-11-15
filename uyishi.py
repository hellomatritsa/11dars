###1-masala

def count_passing_students(grades: list[int], passingGrade: int) -> int:
        natija=list(filter(lambda x: x >= passingGrade, grades))
        return len(natija)


grades = [45, 60, 75, 30, 90]
passingGrade = 60

print(count_passing_students(grades, passingGrade))

##2-masala

def ends_with_gram(words: list[str]) -> list[str]:
    natija = list(filter(lambda x: x.lower().endswith("gram"), words))
    return natija


words = ["telegram", "Instagram", "hello", "proGram", "diagram", "world"]

print(ends_with_gram(words))




