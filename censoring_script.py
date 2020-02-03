import re

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "alarmingly", "out of control", "help", "trapped", "unpredictable", "unhappy", "bad",
                  "upset", "awful", "broken", "damage", "damaging", "unconscious", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable", "dead", "alive"]

#########################################################

# Phrase censoring function


def censored_phrase(word, document):
    if word in document:
        document = document.replace(word, '******************')
    return document

# Uncomment to test phrase censor function
# print(censored_phrase('learning algorithms', email_one))


# List censoring function

def censored_list(lst, document):
    for word in lst:
        if word in document:
            document = re.sub(
                r"\b%s\b" % word, '******************', document, flags=re.IGNORECASE)
    return document

# Uncomment to test phrase from list censor function
# print(censored_list(proprietary_terms, email_two))


def censored_negativity(lst, document):
    count = 0
    for word in lst:
        if word in document:
            count += 1
    if count > 2:
        for word in lst:
            if word in document:
                document = re.sub(
                    r"\b%s\b" % word, '******************', document, flags=re.IGNORECASE)
        return document

# Uncomment to test censor negativity function
# print(censored_negativity(negative_words, email_three))


punctuation = [',', '!', '?', '.', '%', '/', '(', ')']


def censor_all(input_text, censored_list):
    input_text_words = []
    for x in input_text.split(' '):
        x1 = x.split('\n')
        for word in x1:
            input_text_words.append(word)
    for i in range(len(input_text_words)):
        checked_word = input_text_words[i].lower()
        for x in punctuation:
            checked_word = checked_word.strip(x)
        if checked_word in censored_list:

            # Censoring the targeted word
            word_clean = input_text_words[i]
            censored_word = ''
            for x in punctuation:
                word_clean = word_clean.strip(x)
            for x in range(len(word_clean)):
                censored_word = '******************'
            input_text_words[i] = input_text_words[i].replace(
                word_clean, censored_word)

            # Censoring the word before the targeted word
            word_before = input_text_words[i - 1]
            for x in punctuation:
                word_before = word_before.strip(x)
            censored_word_before = ''
            for x in range(len(word_before)):
                censored_word_before = censored_word_before + '*'
            input_text_words[i - 1] = input_text_words[i -
                                                       1].replace(word_before, censored_word_before)

            # Censoring the word after the targeted word
            word_after = input_text_words[i + 1]
            for x in punctuation:
                word_after = word_after.strip(x)
            censored_word_after = ""
            for x in range(len(word_after)):
                censored_word_after = censored_word_after + '*'
            input_text_words[i + 1] = input_text_words[i +
                                                       1].replace(word_after, censored_word_after)
    return " ".join(input_text_words)


all_lists = proprietary_terms + negative_words

# Uncomment to test censor negativity function
print(censor_all(email_four, censor_all))
