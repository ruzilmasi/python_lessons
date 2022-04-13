from itertools import zip_longest


def names_gen(tutors, klasses):
    if len(tutors) > len(klasses):
        for tutor, klass in zip_longest(tutors, klasses):
            yield (tutor, klass)
    else:
        for tutor, klass in zip(tutors, klasses):
            yield (tutor, klass)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Станислав']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = names_gen(tutors, klasses)
# print(*result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
