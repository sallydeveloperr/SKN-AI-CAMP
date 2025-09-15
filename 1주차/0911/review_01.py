#딕셔너리
    # .items() .keys(), values()
#정렬
    #sorted
#max
    #max()
#enumerate
    #순환문에서 리스트를 감싸면 (인덱스, 리스트의 값)
#zip
    #여러개의 iterable들을 각 원소를 쌍으로 하는 집합
    #파이썬에서 iterable 예시
    #리스트(list): ['사과', '포도', '딸기']
    #튜플(tuple): (1, 2, 3)
    #문자열(str): "Sally" (문자 하나씩 꺼낼 수 있음)
    #딕셔너리(dict): {"이름": "Sally", "나이": 24} (키, 값, 항목 등 순회 가능)
    #세트(set): {1, 2, 3}
#map()
    #함수명, iterable한 각 요소에 특정 함수를 적용
    #예를 들면, map(int,['1','2'])  -> [1,2]

import collections
datas = [1,1,1,1,2,1,3,4,1,2,4,1]
print(collections.Counter(datas))