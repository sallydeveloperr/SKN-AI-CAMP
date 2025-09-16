#리스트에서 짝수만 출력
list_1 = []
print([i for i in range(5) if i % 2 == 0])

#또 다른 방법
list_1 = [1,2,3,1,2,3,5,4,8]
#값 2에 해당하는 인덱스를 찾아서 리스트로 반환
#[1,4]
print([idx for idx, value in enumerate(list_1) if value == 2])

#성년/미성년자 구분
age = 24
if age > 18:
    result = "성인"
else:
    result = "미성년자"


#컴프리핸션
result = "성인" if age > 18 else "미성년자"
print(result)

list_1 = [1,2,1,5,3,2,1,5,4]
print([ '1' if i % 2 == 0 else '0' for i in list_1 ])

[ '성인' if age > 18 else '미성년' for i in list_1 ]
