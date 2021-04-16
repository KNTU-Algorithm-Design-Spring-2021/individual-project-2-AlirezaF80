# YThLQYQ4zj0qg
global dictionary


def is_valid_word(word: str):
    return word in dictionary


def wordBreak(s: str):
    T = []
    for i in range(len(s) + 1):
        T.append([False, ''])
    T[0][0] = True
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if T[j][0] and is_valid_word(s[j:i]):
                T[i][0] = True
                T[i][1] = T[j][1] + " " + s[j:i]
                break
    return T[len(s)][1].strip()


if __name__ == '__main__':
    dictionary = open('words_alpha.txt', 'r').readlines()
    dictionary = [word.strip() for word in dictionary]
    print(wordBreak(input().lower().strip().replace(' ', '')))
