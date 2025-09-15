#딕셔너리의 성질을 이용한 리스트의 요소를 카운트
#max 함수를 이용해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 키
#매소드 .get() 사용

#키를 이용해서 값을 가져오는 방법
dict_1 = {'사과' : 10, '포도' : 20}
#포도의 값
print(dict_1['포도'])   #인덱스 방식 없으면 keyerror
print(dict_1.get('포도'))   #메소드 방식 없으면 None
print(dict_1.get('파인애플', 0))

#자료구조에서 가장 큰 값을 찾는 max
print(max([1,5,2,4,8,7,1,5,4]))

dict_1 = {'국어' : 80, '영어' : 100}
print(max(dict_1, key=dict_1.get))

#정렬-리스트
list_1 = [3,2,5,1]  #정렬은 오름차순이 디폴트
print(sorted(list_1))
print(sorted(list_1, reverse=True))
print(sorted(list_1)[::-1])     #처음부터 끝까지 역순으로 출력하라[::-1]

#dict
dict_1 = {'국어' : 80, '국사' : 100, '영어' : 98, '수학' : 88}
print(sorted(dict_1))   #키 가나다라 오름차순으로 정렬
print(sorted(dict_1, key=dict_1.get))   #벨류값 순서대로 오름차순으로 정렬

