# Exercise 4

questions_section = [
             {"question":"What is the capital of Austria?: ", "answer":"A"},
             {"question":"What is the capital of Bulgaria?: ", "answer":"C"},
             {"question":"What is the capital of Croatia?: ", "answer":"B"},
             {"question":"What is the capital of Denmark?: ", "answer":"A"},
             {"question":"What is the capital of Greece?: ", "answer":"D"},
             {"question":"What is the capital of Hungary?: ", "answer":"C"},
             {"question":"What is the capital of Belgium?: ", "answer":"A"},
             {"question":"What is the capital of Italy?: ", "answer":"B"},
             {"question":"What is the capital of Sweden?: ", "answer":"B"},
             {"question":"What is the capital of Ukraine?: ", "answer":"D"}
             ]

options =  [
           ["A. Vienna", "B. London", "C. Warsaw", "D. Helsinki"],
           ["A. Madrid", "B. Bucharest", "C. Sofia", "D. Oslo"],
           ["A. Dublin", "B. Zagreb", "C. Kyiv", "D. Copenhagen"],
           ["A. Copenhagen", "B. Stockholm", "C. Brussels", "D. London"],
           ["A. Warsaw", "B. Sofia", "C. Amsterdam", "D. Athens"],
           ["A. Helsinki", "B. Rome", "C. Budapest", "D. Lisbon"],
           ["A. Brussels", "B. Kyiv", "C. Oslo", "D. Stockholm"],
           ["A. Zagreb", "B. Rome", "C. Warsaw", "D. Dublin"],
           ["A. Sofia", "B. Stockholm", "C. Madrid", "D. Helsinki"],
           ["A. Paris", "B. Copenhagen", "C. London", "D. Kyiv"]
           ]     
score = 0
def check_response(user_guess,correct_response):
    if user_guess==correct_response:
        return True
    else:
        return False


for questions in range(len(questions_section)):
    print("_______________________________")
    print(questions_section[questions]["question"])
    for x in options[questions]:
        print(x)

    guess = input("Choose the correct answer(A/B/C/D): ").upper()
    is_correct = check_response(guess, questions_section[questions]["answer"])
    if is_correct:
        print("Correct answer")
        score+=1
    else:
        print("Incorrect answer")


