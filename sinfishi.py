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














