# 좋은 소프트웨어 만들기
## d3.js 실습
- 함수의 객체성(1급 객체)
- 중첩 암수
- 함수 오버로딩
- 덕타이핑
- 클로저
- this : 호출하는 점 앞의 객체.
- 싱글스레드 : 어떤 이벤트가 끝나자마자 실행할 함수를 큐에 넣는게 고작이다.
- 스코프는 중첩 함수로 다스린다.


## SOLID 원칙
1. Single Responsibility Principle(단일 책임 원칙)
2. Open/Closed Principle(개방/폐쇄 원칙)
3. Liskov Substitution Principle(리스코프 치환 원칙)
4. Interface Segregation Principle(인터페이스 분리 원칙)
5. Dependency Inversion Principle(의존성 역전 원칙)


### Single Responsibility Principle(단일 책임 원칙)
- 모든 클래스(함수)는 반드시 한가지 변경 사유가 있어야 한다.
- 유일한 관심사 하나만 가지고 있을 것.

### Open/Closed Principle(개방 폐쇄 원칙)
- 모든 소프트웨어 개체는 확장 가능성은 열어두되, 수정 가능성은 닫아야 한다.
- 실행 코드를 변경하지 않고 어떻게든 재사용하고 확장해야 한다.

### Liskov Substitution Principle(리스코프 치환 원칙)
- 어떤 타입에서 파생된 타입의 객체가 있다면 이 타입을 사용하는 코드는 변경하면 안된다.
- 한 객체를 다른 객체에서 파생하더라도 그 기본 로직이 변경되어서는 안된다.
- 서로 파생 관계가 없는 타입간에는 상관 없음

### Interface Segregation Principle(인터페이스 분리 원칙)
- 인터페이스 : 클래스에서 어떤 기능을 구현하지 않고 명칭, 파라미터, 반환 타입만 서술한 코드 조각
- 기능이 많은 인터페이스는 더 작게 응축시킨 조각으로 나누어야 한다는 발상.
- 인터페이스 기능이 없는 자바스크립트에서는 '덕타이핑 기법'으로 대체하기도 함

### Dependency Inversion Principle(의존성 역전 원칙)
- 상위 수준 모듈은 하위 수준 모듈에 의존해서는 안되며, 이 둘은 추상화에 의존해야 한다.
- 의존성 주입은 이를 실현하기 위한 메커니즘으로 이용됨


## DRY 원칙
- Don't Repeat Yourself : 모든 지식 조각은 딱 한번만 나와야 한다.


## 단위 테스트 Unit Test
- unit : 특정 조건에서 어떻게 동작해야하는 지 정의해둔 것. 보통은 함수로 표현.
- 준비(Arrange) -> 실행(act) -> 단언(assert)의 과정
  1) 준비 : 단위 테스트 조건을 확실히 하고, 의존성 및 함수 입력 데이터를 설정
  2) 실행 : 단위를 실행
  3) 단언 : 미리 정한 조건에 따라 단위가 작동하는지 확인. (리턴값이 예상값이랑 같은지 확인)


## 테스트 주도 개발(Test Driven Develop)
- 애플리케이션 코드를 짜기 전에 이 코드가 통과해야 할 단위 테스트를 먼저 작성한다.
- 적색(Red) -> 녹색(Green) -> 리팩터(Refactor) 과정을 반복
- 테스트 하기 쉬운 코드를 작성하려면 관심사를 분리해야 한다.
