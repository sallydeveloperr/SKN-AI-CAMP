# 선거시스템
# 유권자  들은 기호로 투표를 진행 결과를 리스트에 저장
#  ex 1,2,3
# 투표는 순환문은 이용해서 유권자가 10이라면 10번순환하면서 후보자(1~5)선택
# [1,1,2,3,4,1,5,1]
# 리스트에있는 각 번호의 횟수를 구해서 당선자를 출력

cadidate = ['홍길동','이순신','강감찬','율곡','신사임당']
vote = []       #투표용지
counts = 10     #유권자
result = {}     #투표 카운트 딕셔너리
# for _ in counts:
#     vote.append(int(input('투표를 하세요(1~5) : ')))
vote = [1,2,3,4,2,2,1,2,2,4]
print(f'vote = {vote}')

# dict 기능을 이용

for i in vote:      #vote있는거 하나씩 순환하면서 가져오는 거
    if i in result: #result는 키와 벨류를 모두 가지고 있고 기준은 키이다. 키 중에서 i가 있냐는 뜻
        result[i] += 1  #해당 키벨류에 추가 1표 더 들어왔으니까 1표 추가
    else:
        result[i] = 1   #딕셔너리에 키벨류 1로 한표가 들어왔으니까 1로 세팅
print(f'result = {result}') 

#라이브러리를 이용하자
#키의 값을 가져올 때 딕셔너리 변수 ['키값']
#딕셔너리 변수.get('키값')
print(result[2])
print(result.get(2))
def find_max(key):
    return max
print(max(result, key=result.get))  #가장 큰 값을 출력 키 2의 값 5개를 출력

def test(data, key):
    for i in data:
        key(i)