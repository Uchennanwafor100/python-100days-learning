import random
words = ['uchenna','peter','chibuike','ebube']
main_word = random.choice(words)
print(f'chosen word is "{main_word}"')
word_length = len(main_word)
display = []
for a in range(word_length):
    display += '_'
print(display)
while True:
    choose = input('guess the letter of the word?....')
    for position in range(word_length):
        letter = main_word[position]
        if letter == choose:
            display[position] = letter
    print(display)
    if '_' not in display:
        print('you won bro')
        break

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"
student_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[score] = "outstanding"
    elif score > 80:
        student_grade[score] = "expectation"
    elif score > 70:
        student_grade[score] = "acceptable"
    else:
        student_grade[score] = "fail"

 print(student_grade)

def my_function():
    print("hello")
    print("wow")

my_function()




operator = True
while operator:
    first_number = int(input("First Number?  "))
    operation = input("which operation do you which to do.(+, -, *, /.) ")
    second_number = int(input("Second number?  "))


    def calculation():
        if operation == "+":
            print(first_number + second_number)
        elif operation == "-":
            print(first_number - second_number)
        elif operation == "*":
            print(first_number * second_number)
        elif operation == "/":
            print(first_number / second_number)
        else:
            print("incorrect operation")


    calculation()


else:
    print("invalid output")







