# 대문자, 소문자 구분없이 이 단어에서 가장 많이 사용된 알파벳 알아내기
# 가장 많이 사용된 알파벳이 여러 개면 ? 을 출력
word = list(input())
converted = []
for el in word:
    if el.isupper():
        converted.append(el)
    else:
        up_el = el.upper()
        converted.append(up_el)
cnt_dict = dict()
for el in converted:
    if el not in cnt_dict.keys():
        cnt_dict[el] = 1
    else:
        cnt_dict[el] += 1
values = [value for value in cnt_dict.values()]
max_v = max(values)
result = ''
for key, value in cnt_dict.items():
    if value == max_v:
        result += key
if len(result) > 1:
    print('?')
else:
    print(result)