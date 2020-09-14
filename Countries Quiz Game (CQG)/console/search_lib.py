import difflib

'''
search->
    1 - word
        a) lower characters
        b) wrong spelling
    2 - sub-name 
        a) for a country with one word name (Egypt -> egy/eg)
        b) for a country with more than one word (United States of America -> america/amer)
    3 - abbreviation
        (United States of America -> USA, United Arab Emirates -> UAE)
'''


def check_similarity(first_word, second_word):
    diff = difflib.SequenceMatcher(None, first_word.lower(), second_word.lower())
    ratio = diff.ratio()
    return round(ratio * 100, 3)


def word_matches(word, strings, n=5, accuracy_percentage=70):
    cutoff = round(accuracy_percentage / 100, 2)
    lower_strings = [x.lower() for x in strings]
    matches_lower = difflib.get_close_matches(word.lower(), lower_strings, n, cutoff)

    while not matches_lower and accuracy_percentage > 45:
        accuracy_percentage -= 2.5
        cutoff = round(accuracy_percentage / 100, 2)
        matches_lower = difflib.get_close_matches(word, lower_strings, n, cutoff)

    matches = []
    for name in matches_lower:
        index = lower_strings.index(name)
        matches.append(strings[index])
    return matches


def sub_word(word, name):
    subs = name.split(' ')
    percentage = 0
    for i in subs:
        percentage = max(percentage, check_similarity(word, i))
    return percentage


def sub_word_list(word, strings):
    matches = []
    high_sim = False
    for name in strings:
        subs = name.split(' ')
        for i in subs:
            percentage = check_similarity(word, i)
            if percentage >= 75:
                matches.append(name)
            if percentage >= 90:
                high_sim = True
    return matches


def abbreviation(word, name):  # UAE United Arabic Emirates
    name = name.replace('of ', '')
    subs = name.split(' ')
    abb = ''.join([str(x[0]) for x in subs])
    percentage = check_similarity(word, abb)
    return percentage


def abbreviation_list(word, strings):
    matches = []
    high_sim = False
    for name in strings:
        temp = name.replace('of ', '')
        subs = temp.split(' ')
        abb = ''.join([str(x[0]) for x in subs])
        percentage = check_similarity(word, abb)
        if percentage >= 85:
            matches.append(name)
        if percentage >= 90:
            high_sim = True
    return matches


def conclusion_with_percentage(word, strings, per=70):
    whole_words = word_matches(word, strings)
    abbrevs = abbreviation_list(word, strings)
    subs = sub_word_list(word, strings)
    matches = set()

    for i in whole_words:
        if check_similarity(i, word) >= per:
            matches.add(i)

    for i in subs:
        if sub_word(word, i) >= per:
            matches.add(i)

    for i in abbrevs:
        if abbreviation(word, i) >= per:
            matches.add(i)

    return list(matches)


def conclusion(word, strings):
    whole_words = word_matches(word, strings)
    abbrevs = abbreviation_list(word, strings)
    subs = sub_word_list(word, strings)
    matches = set(whole_words + abbrevs + subs)
    return list(matches)


def exact_match_list(word, strings):
    conc = conclusion(word, strings)
    match = []
    for i in conc:
        flag = (check_similarity(word, i) >= 95) or (abbreviation(word, i) >= 95) or (sub_word(word, i) >= 95)
        if flag:
            match.append(i)
    return match


def exact_match(first_word, second_word):
    flag = (check_similarity(first_word, second_word) >= 95) or (abbreviation(first_word, second_word) >= 95) or (
            sub_word(first_word, second_word) >= 95)
    return flag
