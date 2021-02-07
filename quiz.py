score = 0
questions = 0

number = int(input("What year is it? "))
questions += 1
if number == 2021:
    score += 1
    print("That's right!")
elif number > 2021:
    print("Oh man, you're from the future!")
elif number < 2021:
    print("Have you been in a coma?")
else:
    print("Hmm... Let's move on.")

text = input("Who is President? ")
questions += 1
answer = "biden"
if answer in text.lower():
    score += 1
    print("That's right!")
else:
    print("Hmm... Let's move on.")

mult_response = input("Which is correct: \n A. \n B. \n C.")
questions += 1
if mult_response.lower() == "a" or mult_response.lower() == "b" or mult_response.lower() == "c":
    score += 1
    print("Good enough!")
else:
    print("That wasn't a choice.")

print("Your score is: ", round(score / questions, 2))
print("We're done here.")