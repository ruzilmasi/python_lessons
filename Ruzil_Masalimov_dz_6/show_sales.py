import sys

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    param = len(sys.argv)
    print(param)
    if param == 1:
        print(f.read())
    elif param == 2:
        for line in f.readlines()[int(sys.argv[1]) - 1:]:
            print(line)
    elif param == 3:
        i = 0
        for line in f:
            i += 1
            if i >= int(sys.argv[1]):
                if i > int(sys.argv[2]):
                    break
                print(line)
#признаюсь, пытался делать сам, но зашел в тупик, скопировал дз с разбора и вникал
