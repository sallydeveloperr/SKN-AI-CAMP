#raise 예외 발생하기
try:
    print("정상코드")
    print("예외발생")
    #raise "내가 발생시킨 오류"
    raise ValueError("테스트")
except Exception as e:
    print(f'에러 : {e} {e.__class__} {e.__class__.__name__}')  #에러 종류(.__class__)랑 에러 이름만(.__class__.__name__)
#계후 2개
#고사리
#닭가슴살
#파예 요거트
#히비스커스티
#단백질쉐이크
#곰곰단백질바
#파리바게트 샐러드
#고품격커피공장 아이스아메리카노

