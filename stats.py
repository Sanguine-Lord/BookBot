def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    cleantext = text.lower()
    answer = {}
    for char in cleantext:
        if char in answer:
            answer[char] += 1
        else:
            answer[char] = 1
    return answer
