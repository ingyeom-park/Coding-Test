def solution(before, after):
    before_list = sorted([x for x in before])
    after_list = sorted([x for x in after])
    count = 0
    for letter in range(len(before)):
        if before_list[letter] == after_list[letter]:
            count += 1
        else:
            return 0
            break
    if count == len(before_list):
        return 1