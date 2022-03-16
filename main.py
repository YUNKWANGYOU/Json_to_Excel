import pandas as pd
import json


def collect_http_packet():
    file_path = "./trace_log.txt"

    data = ''
    res = ''
    with open(file_path, 'r') as file:
        while 1 :
            b = file.readline()
            if b == '' : # 마지막 줄이면 프로그램 종료
                break
            elif b == '   PROTOCOL             = HTTP\n' : # 프로토콜이 HTTP면
                while 1 :
                    c = file.readline()
                    if c == 'END\n' : # END 가 나올때까지 조회해서 결과값에 붙여줌
                        break
                    res+=c

    return res

def preprocessing(res) :
    pointer = res.index('{')

    tmp = ''
    cnt = 1
    while 1 : # 괄호 갯수 세서 괄호갯수 같으면 json파일 끝난걸로 확인하고 끝냄
        if cnt == 0 :
            break
        else :
            pointer+=1
            tmp+=res[pointer]
            if res[pointer] == "{" :
                cnt+=1
            if res[pointer] == "}" :
                cnt-=1
    tmp = '{'+tmp

    return tmp

if __name__ == '__main__':
    raw_data = collect_http_packet()
    res = preprocessing(raw_data) # TODO: 데이터 전처리가 완벽히 안됐음 앞 공백 4자리가 문제인 것 같다.
    print(res)
    # json_objcet = json.loads(res)
