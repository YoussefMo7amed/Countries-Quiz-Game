import pandas as pd
import random
import temp

df = pd.DataFrame()
n_of_rows = df.shape[0]


def question_formula(questions, idx, type):
    n = int(random.randint(0, len(questions) + 1)) % len(questions) + 1
    detail = questions[n]
    question = detail[0]
    first = detail[1]
    if type != 3:
        second = detail[2]
    if type == 1:
        question = question.format(df.iloc[idx][first])
    elif type == 3:
        question = question.format(df.iloc[idx][first])
        return detail, question, first, df.iloc[idx][first]
    else:
        if second == 'all':
            if type == 4:
                question = question.format(first)
            else:
                question = question.format(str(df.iloc[idx][first]))
        else:
            if type == 4:
                question = question.format(first, df.iloc[idx][second])
            else:
                question = question.format(str(df.iloc[idx][first]), str(df.iloc[idx][second]))
    return detail, question, first, second


def answer_and_choices(idx, first, second):
    answer = df.iloc[idx][second]
    choices = set()
    choices.add(answer)
    while len(choices) < 4:
        rand = random.randrange(0, n_of_rows)
        while df.iloc[rand][second] in choices:
            rand = random.randrange(0, n_of_rows)
        temp = df.iloc[rand][second]
        if pd.isna(temp):
            temp = "{} has no official {}".format(df.iloc[idx][first], second)
        choices.add(temp)

    return answer, list(choices)


def take_input():
    Continue = True
    while Continue:
        respond = input()
        try:
            respond = int(respond)
            if respond > 0 and respond < 5:
                Continue = False
            else:
                print("please enter valid choice")
        except:
            print("please enter valid choice")
    return respond


def type_one_question(idx):
    questions = {  # A
        1: ("where is {}?", 'country', 'continent'),  # 1
        2: ("{} official language/s is/are ___", 'country', 'language'),  # 2
        3: ("{} uses ___ as there official currency", 'country', 'currency'),  # 3
        4: ("{} is capital of ___", 'capital', 'country')}  # 4

    detail, question, first, second = question_formula(questions, idx, 1)
    print(question)

    answer, choices = answer_and_choices(idx, first, second)

    choices = random.sample(choices, 4)

    for i in range(4):
        print(i + 1, '- ', choices[i])

    res = take_input()
    return question, answer, choices[res - 1]


def answer_and_choices_2(idx, first, second, type, question):
    answer = 0
    choices = set()

    if second == 'all':
        if type == 2:
            first_value = str(df.iloc[idx][first]).strip()
            answer = len(df.query('{} == "{}"'.format(first, first_value)))
            question = question.format(first_value)
        elif type == 4:
            try:
                answer = int(df[df[first].isnull()].count()[0])
            except:
                answer = 0
            question = question.format(first)
    else:
        second_value = df.iloc[idx][second]
        if type == 2:
            try:
                first_value = str(df.iloc[idx][first]).strip()
                temp = df.query('{} == "{}"'.format(first, first_value))
                answer = len(temp.query("{} == '{}'".format(second, second_value)))
            except:
                answer = 0
            question = question.format(first_value, second_value)
        elif type == 4:
            try:
                answer = int(df[df[first].isnull()][second].value_counts()[second_value])
            except:
                answer = 0
            question = question.format(first, second_value)

    choices.add(answer)
    while len(choices) < 4:
        rand = random.randrange(0, max(answer + 50, int(n_of_rows / 2.5)))
        while rand in choices:
            rand = random.randrange(0, max(answer + 50, int(n_of_rows / 2.5)))
        choices.add(rand)

    return answer, list(choices), question


def type_two_question(idx):
    questions = {  # B
        1: (
        "what is the number of countries that has {} as their official language/s in the world?", 'language', 'all'),
        # 1
        2: ("what is the number of countries that use {} as currency in the world?", 'currency', 'all'),  # 2
        3: ("what is the number of countries that has {} as their official language/s in {}?", 'language', 'continent'),
        # 3
        4: ("what is the number of countries that use {} as official currency/ies in {}?", 'currency', 'continent')  # 4
    }
    while df.iloc[idx].isnull().any():
        idx = random.randint(0, n_of_rows)
    detail, question, first, second = question_formula(questions, idx, 2)
    answer, choices, question = answer_and_choices_2(idx, first, second, 2, question)
    print(question)
    choices = random.sample(choices, 4)
    for i in range(len(choices)):
        print(i + 1, "- ", choices[i])

    res = take_input()
    return question, answer, choices[res - 1]


def type_three_question(idx):
    questions = {
        1: ("what is the number of countries in {}?", 'continent')
    }
    detail, question, first, continent = question_formula(questions, idx, 3)

    answer = len(df.query("continent == '{}'".format(continent)))
    mx = df.groupby('continent')['country'].describe().max()['count']

    choices = set()
    choices.add(answer)
    while len(choices) < 4:
        rand = random.randrange(0, mx + 1)
        while rand in choices:
            rand = random.randrange(0, mx + 1)
        choices.add(rand)
    print(question)
    choices = random.sample(choices, 4)
    for i in range(len(choices)):
        print(i + 1, "- ", choices[i])

    res = take_input()
    return question, answer, choices[res - 1]


def type_four_question(idx):
    questions = {
        1: ("what is the number of countries that has no official {} in {}?", 'capital', 'continent'),
        2: ("what is the number of countries that has no official {} in {}?", 'currency', 'continent'),
        3: ("what is the number of countries that has no official {} in {}?", 'language', 'continent'),
        4: ("what is the number of countries that has no official {} in the world?", 'capital', 'all'),
        5: ("what is the number of countries that has no official {} in the world?", 'currency', 'all'),
        6: ("what is the number of countries that has no official {} in the world?", 'language', 'all')
    }
    detail, question, first, second = question_formula(questions, idx, 4)
    answer, choices, question = answer_and_choices_2(idx, first, second, 4, question)
    print(question)
    choices = random.sample(choices, 4)
    for i in range(len(choices)):
        print(i + 1, "- ", choices[i])

    res = take_input()
    return question, answer, choices[res - 1]


def random_question(idx):
    global df, n_of_rows
    number_of_types = 4
    df = temp.read_data()
    n_of_rows = df.shape[0]
    n = random.randrange(0, n_of_rows) % number_of_types + 1
    if n == 1:
        return type_one_question(idx)
    elif n == 2:
        return type_two_question(idx)
    elif n == 3:
        return type_three_question(idx)
    else:
        return type_four_question(idx)
