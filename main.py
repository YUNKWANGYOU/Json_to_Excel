import pandas as pd
import json

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


print(res.index('{'))
print(res)
