from random import choice, sample


def get_jokes(count, flag=False):
    jokes = []
    jokes_no_repeat = []
    for i in range(count):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        res = f"{noun} {adverb} {adjective}"
        jokes.append(res)
        if flag == True and count >= 5:
            jokes_no_repeat = res.split()
            for n in nouns:
                for word in jokes_no_repeat:
                    if n == word:
                        nouns.remove(n)
            for adv in adverbs:
                for word in jokes_no_repeat:
                    if adv == word:
                        adverbs.remove(adv)
            for adj in adjectives:
                for word in jokes_no_repeat:
                    if adj == word:
                        adjectives.remove(adj)
    print(jokes)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(2, True)  #1ый параметр - задает кол-во шуток, 2ой - включает(True) или выключает (False) - флаг
                    # при вклченном флаге шутки не повторяются, по умолчанию flag = False