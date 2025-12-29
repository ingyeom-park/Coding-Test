def solution(age):
    alphabet_age = []
    list_age = [int(x) for x in str(age)]
    for i in list_age:
        alphabet_age.append(chr(i + ord("a")))
    return "".join(alphabet_age)