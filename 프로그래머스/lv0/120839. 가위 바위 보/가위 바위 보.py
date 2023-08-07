def solution(rsp):
    dict = {'2':'0', '0':'5', '5':'2'}
    return ''.join([dict.get(i) for i in rsp])
    