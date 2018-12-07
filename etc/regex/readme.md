# 정규표현식 문법 간단정리
## 수량
* {min, max} : 해당 패턴의 최소, 최대 등장회수 지정. 최대는 생략 가능(무한이라는 뜻)
* ? : 0개 or 1개(={1,2})
* + : 1개 이상(={1,})
* * : 0개 이상(={0,})

## 위치
* ^ : 시작
* $ : 끝

## 클래스
* \s : 공백문자(\n,\r,\f,\b,\t)
* \b : 단어의 시작
* \d : 숫자
* \w : 글자(\d제외)
* 대문자로 쓰면 반대를 의미함 ex. \S : 공백문자 제거. 하지만 사용을 추천하진 않음.
* 사용자 클래스는 []에 정의함

## 플래그
* g : 글로벌. 패턴에 매칭되는 부분을 전체에서 찾는다는 말.
* i : ignore case
* u : 유니코드 인정(\w에만 영향을 미침)

## 기타
* () : 그룹
* (?:) : 비캡쳐 그룹
* | :선택
*. : 탐욕(최대로 얻어버리자)
* 수량자 뒤의 ? :겸허모드(뒤가 일치하는지 먼저 확인)


### 포인트
* 정규표현식은 자신이 표현하고 싶은 패턴의 구조를 정확하게 나타내는 것.
* 핵심은 모든 케이스를 꼼꼼하게 나누고, 그것을 식으로 위에 정해진 패턴으로 표현하면 됨.
* 작은 케이스에서부터 복잡한 케이스로 점점 붙여나가도록 한다.
  ex. [정수] -?(0|[1-9][0-9]*)
      [실수 포함] -?(0|[1-9][0-9]*)(\.[0-9]+)?
      [지수표기법 포함] 0|-?[1-9][0-9]*(\.[0-9]+)?([eE][+-]?[1-9]+)?