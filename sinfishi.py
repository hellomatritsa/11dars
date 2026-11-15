##1-masala

def clean_and_title_text(matn: str)->str:
    return matn.strip().title()

matn=input("Matn kiriting: ")
print(clean_and_title_text(matn))



##2-masala

def calculate_average_grade(baho: dict) -> float:
    return(sum(baho.values()) / len(baho))



data={"Matematika": 85, "Fizika": 90, "Tarix": 78}
natija=calculate_average_grade(data)
print(round(natija,2))

##3-masala

def remove_duplicates(items: list) -> list:
    return list(dict.fromkeys(items))


element=["olma", "banan", "olma", "anor", "banan"]
print(remove_duplicates(element))


###4-masala

import json
with open("fayl.json") as ptr:
    data=json.load(ptr)

def filter_active_employees(file_path: str, min_salary: int = 1000) -> list:
    lst=[]
    for i in file_path:
        if i["is_active"] == True and i["salary"] >= min_salary:
            lst.append(i)

    return lst


print(filter_active_employees(data))














