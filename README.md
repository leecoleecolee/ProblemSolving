<details><summary>팁</summary><blockquote>

- ```help(dir)``` 객체의 사용법과 기능 출력
- ```dir(객체)``` 객체의 속성 정보(메쏘드, 멤버 변수)
- ```type(객체)``` 객체의 타입 출력

- ```collections``` 모듈에 있는 딕셔너리 잘 사용하자!

- 정렬
  - ```메쏘드 sort```와 ```함수 sorted```를 구별하자.
  - ```sort```에 쓰이는 알고리즘은 ```Teamsort```
  - 리스트의 sort를 예로 들어보면
     - b = [ 3,4,5,1]
     - c = b.sort() # 이건 틀린문장. 메쏘드의 sort는 리턴값이 None이다. 자기 자신을 바꾸는 메쏘드
     - c = sorted(b) # 이건 맞다.
  - 정렬에 ```key=```옵션을 지정해서 정렬을 위한 키 또는 함수를 지정해 줄 수 있다.
    ```
    sorted(b, key=len) # 정렬을 하기 위한 기준함수로 len 을 사용
    
    def fn(s): 
      return s[0], s[-1]
    sorted(b, key=fn) # 위에서 정의한 fn을 key로 사용 문자열의 첫번째와 마지막원소로 정렬
    
    위의 정렬을 람다표현식으로도 나타낼 수 있다.
    
    sorted(b, key=lambda s: (s[0], s[-1]))
    ```

</blockquote></details>

<details><summary>파이썬에는 main이 없나?</summary><blockquote>
- 파이썬을 사용하면서 느낀 특이점은
  1. 인덴트를 통해 코드 실행의 레벨을 결정한다.
  2. ```main```이 존재하지 않는다.
  
- C를 이용해 ```haha```를 출력하는 프로그램을 만든다고 해보자. 그러면 아래처럼 만들어질 것이다.
  ```
  void test(void)
  {
    printf("haha");
  }
  
  int main(void)
  {
    test();
    return (0);
  }
  ```
- 당연하게도 ```main```문이 존재한다. 그렇다면 파이썬은 어떨까
  ```
  def test():
    print("haha")
  test()
  ```
  - ```main```이 없다!!
  - 파이썬은 ```main```문이 없는 대신에, 인덴트가 되지 않은 코드를 가장 먼저 실행시킨다.
  
- 그렇다면 어떤 프로그램을 만든다고 할 때, 그냥 단순히 인덴트를 통해서만 코드 실행을 결정해야하나?
  - 그건 아니다!
  - ```내장변수```를 활용하면 ```main```을 사용할 수 있다!
  
- ```__name__```내장변수
  - 파이썬에는 다양한 내장변수가 존재한다.
  - ```__name__``` 내장변수는 ***직접 실행된 파일(Module)에서는 ```__main__```의 값을 갖고, 직접 실행되는게 아닌 ```import```된 모듈에서는 모듈의 이름(파일명)***을 갖는다.
  
- module.py, main.py
  ```
  # module.py
  def hello():
    print("in module: {}".format(__name__))
  ```
  
  ```
  # main.py
  import module
  
  module.hello()
  
  print("in main: {}".format(__name__))
  ```
  - 위와 같이 import해서 사용할 모듈 ```module.py```와 main으로 사용할 ```main.py```을 만들어보자.
  - 먼저 ```module.py```를 실행해보자.
    ```
    python module.py
    
    >>> in module: __main__
    ```
  - 다음으로  ```main.py```를 실행해보자.
    ```
    python main.py
    
    >>> in module: module
    >>> in main: __main__
    ```
  - 차이가 확 드러난다. 처음에 ```module```을 실행했을 때는 분명 ```__name__```의 값이 ```__main__```이었는데, ```main```에서 import해서 사용하니깐 이 값이 ```module```로 바뀌고 main자체의 ```__name__```이 ```__main```으로 되었다. 
- 위에서 말한것처럼 직접 실행하는 파일이냐 import해서 사용하냐에 따라 ```__name__```의 값이 바뀌는걸 알 수 있다.

- 따라서 이 성질을 이용해서 ```main```으로 사용하고 싶은 파일에다가 아래처럼 입력하면 ```main```을 사용할 수 있게 된다.
  ```
  ...
  ...
  ...
  
  if __name__ == "__name__":
    ...
    ...
    
  ...
  ```
</blockquote></details>

<details><summary>list 자료형</summary><blockquote>

- 파이썬에는 리스트 자료형이 있다.
- 간단하게 C++의 ```std::vector<T>```와 같은 동적 배열이라고 생각하면 된다.
- 하지만 속도면에서 파이썬의 ```list```와 C++의  ```vector```은 엄청난 차이가 있다.
  - 왜 이런 차이가 생길까?
    - 자료형에 대한 이해가 필요하다. Cpp에서의 ```int```와 같은 자료형들은 ```원시타입```이다. 하지만 파이썬에서의 자료형들은 ```객체```로 이루어져 있다. 따라서 ```a = 1```이라는 문구가 있을 때 cpp에서는 ```int형 변수 a는 1의 의 값을 갖는다```라고 말할 수 있지만, 파이썬에서는 ```a는 메모리 어딘가에 있는 1의 값을 참조한다```의 형태로 되는것이다.
  
    - 두 번째로 알아야 할 것은 cpp에서의 ```vector```는 하나의 자료형을 갖는다. ```std::vector<int> vec```로 선언한 ```vec```벡터에는 ```int```형 밖에는 담지 못한다는 의미. 이렇게 구현이 됨으로써 ***연속되는 메모리에 값이 저장된다.*** 하지만 파이썬의 리스트는 ```test = [1, 'str', True, ('tuple', 'test')]``` 처럼 여러 자료형을 같이 넣는게 가능하다. 따라서 ```vector```처럼 연속된 메모리상에 값이 있는게 아닌 참조하는 포인터만 있고, 리스트의 각 변수에 접근하면 참조하는 주소의 값을 리턴해주는 것이다.
    
- 존재하지 않는 인덱스를 조회하면 ```IndexError```가 발생한다.
  ```
  a = [1,2,3]
  try:
    print(a[4])
  except IndexError:
    print("존재하지 않는 index")
  ```  
- ```슬라이싱```을 잘 사용하자. 슬라이싱은 내부적으로 C언어로 구현되어 있기 때문에 속도가 다른 방법보다 훨씬 빠르다.

- reverse
  - 뒤집는 건 간단하게 ```s.reverse()```를 하면 된다. 하지만 이렇게 할 경우 시간초과가 뜰 수 있다.
  ```s[:] = s[::-1]```이렇게 하도록 하자.
</blockquote></details>

<details><summary>Dictionary</summary><blockquote>

- 파이썬의 딕셔너리는 키/값 구조로 이뤄진 자료형이다.
- 내부적으로는 해시 테이블로 구현되어 있다.
- 파이썬의 딕셔너리는 숫자를 포함해 여러가지 자료형이 ```key``` 값이 될 수가 있다.
- 해쉬 테이블을 사용하므로 ```입력, 조회```와 같은 작업은 ```O(1)```의 속도를 갖는다. 물론 최악의 경우에는 ```O(n)```을 갖을수도 있음
- 문제풀이를 할 때 딕셔너리를 효율적으로 사용해야한다.
- 특징으로는 ```python 3.6``` 이하 버전에서는 키값의 순서가 보존되지 않는다는 것. 주의하자.
- 존재하지 않는 키를 조회할 경우 ```KeyError```가 발생한다.


- 사용할 수 있는 모듈 ```from collections import defaultdict, Counter, OrderedDict```
  - defaultdict
    - 존재하지 않는 키를 조회할 경우, throw를 던지지 않고 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.
    
  - Counter
    - 아이템에 대한 개수를 계산해 딕셔너리 형탤 리턴한다.
    ```
    a = [1, 2,3, 4, 5, 5, 5, 6, 6]
    b = collections.Counter(a)
    b
    b.most_common(2) // 빈도가 가장 높은 2개 추출
    ------
    Counter({5:3, 6:2, 1:1, 2:1, 3:1, 4:1})
    [(5, 3), (6, 2)]
    ```
  - OrderedDict
    - 입력 순서가 유지된다.

</blockquote></details>

<details><summary>여러가지 자료형을 잘 사용하자</summary><blockquote>

- list에는 ```pop``` 메쏘드가 있다.
  ```
  a = [1, 2, 3, 4]
  a.pop(0)
  ```
- 위 처럼 첫 번째 인덱스의 값을 ```pop```하는 경우의 시간복잡도는 ```O(n)```이 된다.
- pop은 맨 뒤에서부터 작업하기 때문에 이런 현상이 발생.
- 그러면 어떻게하지? -> ```Deque```를 사용하자.
  ```
  from typing import *
  import collections
  b: Deque = collections.deque()
  
  b.popleft()
  ```
</blockquote></details>
<details><summary>유효한 팰린드롬</summary><blockquote>
  
1. 유효한 팰린드롬(p. 138)

- 앞 뒤가 똑같으면 참, 아니면 거짓을 리턴하는 함수를 만드는 문제.
- 함수의 인자로 문자열이 주어지면 이 문자열을 ```list```형태로 만들어서 ```s.pop(0) == s.pop()``` 이렇게 문제를 풀면 안된다.

- 리스트의 ```pop```메쏘드는 인자가 들어가는 순간 인덱스를 찾아가야 하므로 ```O(n)```의 시간복잡도가 걸린다.
- 따라서 ```Deque```를 이용해서 문제를 풀도록 하자.

- 그리고 가장 좋은 방법은 ```s[::-1]``` 처럼 문자열을 인덱싱으로 뒤집어서 원래의 문자열과 비교하는 방법이 가장 좋다.

2. 문자열 뒤집기

- ```s[::-1]

3. 로그파일 재정렬

- ```람다표현식```: 람다표현식이란 식별자 없이 실행 가능한 함수를 말한다. 함수 선언 없이도 하나의 식을 함수를 단순하게 표현할 수 있다.

4. 가장 흔한 단어
-

5. 애너그램

- 애너그램이란 문자를 재배열했을 때 같은 문자가 나오는 문자들.
  ```ate, eat, tea``를 같은 애너그램이라고 할 수 있다.
  
- ```[eat, ate, tea, nat, tan, bat]``` 가 있을 때 가장 많은 수의 애너그램은?

  1. ```key - value```의 쌍으로 만들어서 ```key```는 하나의 애너그램, ```value```는 애너그램의 등장 숫자 로 표현하면 쉽게 해결 할 수 있다.

  2. 일반 딕셔너리는를 사용하면 키 밸류가 항상 있어야 하므로 디폴트 밸류가 주어지는 ```defaultdict```를 사용하자.

```
import collections

anagrams = collections.defaultdict(list)

for word in strs:
  anagrams[''.join(sorted(word))].append(word)
return anagrams.values()

```

- 애너그램은 동일한 알파뱃들이 있는 단어들이므로 단어들을 정렬한다. 정렬한 단어를 딕셔너리의 ```key```로 사용하고, 그 ```key```에 단어를 append 하자.

6. 가장 긴 팰린드롬 부분 문자열 찾기

- 다이나믹프로그래밍으로 해결할 수 있지만, 다이나믹은 코드로 구현하기가 은근 어렵다.
- 투 포인터 기법으로 문제를 해결하자(맨 앞 포인터, 맨 뒤 포인터를 이용해서 문제 해결)
</blockquote></details>

<details><summary>배열 문제</summary><blockquote>

- 투포인터스 란?
  - 투포인터스는 두 개의 포인터를 이용해서 문제를 해결하는 것을 말함.
  - 보통 시작점과 끝점을 두 개의 포인터로 만들고 문제를 해결하는 경우가 많다.

</blockquote></details>

<details><summary>우선순위 큐</summary><blockquote>

- heappush - ```O(log n)```

  - 첫 번째 인자로는 데이터가 담겨질 ```list```, 두 번째 인자는 push 할 데이터.
  - 두 번째 인자는 튜플 형식으로 첫 번째값은 우선순위 값, 두 번째 값이 데이터다.
  ```
  h = []
  heapq.heappush(h, (3, 'haha'))
  heapq.heappush(h, (1, 'zz'))
  heapq.heappush(h, (10, 'final'))
  print(h)
  ```
  출력결과
  ```
  [(1, 'zz'), (3, 'haha'), (10, 'final')]
  ```
- heappop
  ```
  import heapq
  h = []
  heapq.heappush(h, (3, "Go to home"))
  heapq.heappush(h, (10, "Do not study"))
  heapq.heappush(h, (1, "Enjoy!"))
  heapq.heappush(h, (4, "Eat!"))
  heapq.heappush(h, (7, "Pray!"))
  first = heapq.heappop(h)
  second = heapq.heappop(h)
  third = heapq.heappop(h)
  print("first:", first)
  print("second:", second)
  print("third:", third)
  
  -----
  
  first: (1, 'Enjoy!')
  second: (3, 'Go to home')
  third: (4, 'Eat!')
  ```

</blockquote></details>

|   날짜   | 챕터 |      문제      | 발표자  | 풀이/해설 |       복습        |
| :------: | :--: | ------------ | :-----: | :--: | :---------------: |
| 20.10.07 | 12장 | 37번. 부분집합 | :ghost: | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/sanam/Problem/DFS_BFS/78.py) | :ghost: |
| 20.10.09 | 13장 | 40번. 네트워크 딜레이 타임 | 👻 | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/gmoon/python_algorithm_interview/13_shortest_way/40_743.py) | 👻 |
|          |      | 41번. K 경유지 내 가장 저렴한 항공권 | 👻 | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/gmoon/python_algorithm_interview/13_shortest_way/41_787.py)     | 👻 |
| 20.10.12 |  14장 | 42번. 이진 트리의 최대 깊이 | :ghost: | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/sanam/Problem/Tree/104.py)     |  |
|          |      | 43번. 이진 트리의 직경 | :ghost: | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/sanam/Problem/Tree/543.py)     |  |
|          |      | 44번. 가장 긴 동일 값의 경로 | :ghost: | [링크](https://github.com/leecoleecolee/ProblemSolving/blob/sanam/Problem/Tree/687.py)     |  |



