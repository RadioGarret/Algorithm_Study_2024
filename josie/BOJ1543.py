def solution2():
    doc = input()
    word = input()
    start_index = 0
    count = 0
    while True:
        find_index = doc.find(word, start_index)
        if find_index < 0:
            break
        start_index = find_index + len(word)
        count += 1
    return count

def solution3():
    doc = input()
    word = input()
    replaced = doc.replace(word, "")
    length = len(doc) - len(replaced)
    return length // len(word)
