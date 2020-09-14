import questions as qs
import random
import time
import temp

''' 
NOTES:
    Title need to be standardized
    choices need to be quit close
'''


def mode_message():
    temp.clear()
    print(temp.line())
    print(temp.title("Practice Mode"))
    print(temp.line())


def initialization():
    data = temp.read_data()
    return data


def valid_input(n):
    try:
        n = int(n)
        return n > 0
    except:
        return False


def take_from_user():
    n = input("Enter number of Questions!\n")
    while not valid_input(n):
        print("please enter valid number")
        n = input("Enter number of Questions!\n")
    return int(n)


def question(i, questions, answers, user_answers):
    global score
    idx = random.randrange(0, n_of_rows)
    print("Q#{} ".format(i + 1), end='')
    question, answer, user_answer = qs.random_question(idx)

    questions.append(question)
    answers.append(answer)
    user_answers.append(user_answer)

    if user_answer == answer:
        score += 1


def right_answers(i, questions, answers, user_answers):
    print(questions[i])
    print("answer:\t\t", answers[i], "\nYour answer:\t{}".format(user_answers[i]).title())
    print("status:".title(), end=' ')
    if answers[i] == user_answers[i]:
        print("Correct Answer!")
    else:
        print("Wrong Answer!!")
    print('-' * 20)


def right_answers2(i, questions, answers, user_answers):
    print(questions[i])
    answer = answers[i]
    user_answer = user_answers[i]
    width = max([len(str(answer)), len(str(user_answer)), len('answer'), len('your answer')])
    status = (answers[i] == user_answers[i])
    if status:
        status = "Correct!"
    else:
        status = "Wrong!"
    # '{:{align}{width}}'.format('test', align='^', width='10')
    print("{:{align}{width}} | {:{align}{width}} | Status".format('answer'.title(), 'your answer'.title(), align='^',
                                                                  width=str(width)))
    print("{:{align}{width}} | {:{align}{width}} | {}".format(str(answer).title(), str(user_answer).title(),
                                                              str(status).title(), align='^', width=str(width)))
    print('_' * (width * 3 + 3))


def wanna_know_right_answers():
    print("show the right answers?\n".title())
    temp.print_yes_no()
    return temp.choices_0_1()


def print_score_time(score, start_time, end_time):
    time = temp.token_time(start_time, end_time)
    print('-' * 44)
    print("You finished in {}".format(time))
    print(temp.center_word(
        "({}) out of ({})".format(score, n),
        'Your score is: \n', '', position='^', width=44).title())
    print(temp.center_word(
        "{}%".format((score / n) * 100),
        '', '', position='^', width=44))
    print('-' * 44)


def clear_screen():
    temp.clear()


def again():
    print("do you want to practice again?\n".title())
    temp.print_yes_no()
    return temp.choices_0_1()


def main():
    global score, df, n_of_rows, n
    df = initialization()
    n_of_rows = df.shape[0]
    mode_message()
    Continue = True
    while Continue:
        score = 0
        questions, answers, user_answers = [], [], []
        n = take_from_user()
        start_time = time.time()
        for i in range(n):
            clear_screen()
            question(i, questions, answers, user_answers)
        end_time = time.time()
        clear_screen()
        print_score_time(score, start_time, end_time)
        if wanna_know_right_answers():
            for i in range(len(questions)):
                print("Question Number {}".format(i + 1))
                right_answers2(i, questions, answers, user_answers)
        Continue = again()
        clear_screen()
