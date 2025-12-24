# 후보2
# 코드 정리
def solution(id_list, report, k):
    answer = [0] * len(id_list)# [0,0,0,0] ==> 전체 유저에 대한 카운팅
    reported_dict = {}
    for id in id_list:
        reported_dict[id] = set([]) # ***************
    for report_pair in report:
        reporter = report_pair.split(" ")[0]
        reported = report_pair.split(" ")[1]
        reported_dict[reported].add( reporter ) # ****** set에서 추가 add
    k_reported = []
    for key_id, v in reported_dict.items():
        if len(v) >= k:
            k_reported.append(key_id)
    for ban_id in k_reported:
        mail_res_ids = reported_dict[ban_id]
        for id in mail_res_ids: # ["muzi", "apeach"]
            id_index = id_list.index( id )
            answer[ id_index ] += 1
    return answer