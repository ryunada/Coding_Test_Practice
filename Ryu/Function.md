# Function

---
#### sort vs sorted
- sort()  
-> 파이썬 리스트는 sort()라는 메소드를 가지고 이 메소드는 리스트를 정렬된 상태로 변경한다.  
```python
>>> myList = [ 1,4,2,3,5 ]
>>> myList.sort()
>>> print(myList)
[1, 2, 3, 4, 5]
```

- sorted()  
-> 내장함수이다.  
-> 이터러블 객체로부터 정렬된 리스트를 생성한다.   
```python
>>> sorted([4, 2, 3, 5, 1])
[1, 2, 3, 4, 5]
```
---

#### str.isdigit()  
- str.isdigit()  
-> 해당 String이 숫자로만 이루어져 있으면 True를 반환  
-> 하나의 숫자가 아닌 문자가 포함되어있으면 False를 반환  
```python
>>> a = "BlockDMask"  # 문자로만 이루어짐
>>> b = "1234Blog"    # 문자 + 숫자
>>> c = "131231"      # 숫자
>>> d = "-234"        # 음수
>>> e = "1.23"        # 소수점
>>> f = "3²"          # 3의 2제곱 기호 숫자
>>> g = "⅔"           # 수학 기호 숫자 2/3
>>> h = "0"           # 0
>>> i = "0123"        # 0 으로 시작한 숫자

>>> # str.isdigit("문자열")
>>> print(f"str.isdigit('{a}') : {str.isdigit(a)}")
>>> print(f"str.isdigit('{b}') : {str.isdigit(b)}")
>>> print(f"str.isdigit('{c}') : {str.isdigit(c)}")
>>> print(f"str.isdigit('{d}') : {str.isdigit(d)}")
>>> print(f"str.isdigit('{e}') : {str.isdigit(e)}")
>>> print(f"str.isdigit('{f}') : {str.isdigit(f)}")
>>> print(f"str.isdigit('{g}') : {str.isdigit(g)}")
>>> print(f"str.isdigit('{h}') : {str.isdigit(h)}")
>>> print(f"str.isdigit('{i}') : {str.isdigit(i)}")

>>> print()

# "문자열".isdigit()
>>> print(f"'{a}'.isdigit() : {a.isdigit()}")
>>> print(f"'{b}'.isdigit() : {b.isdigit()}")
>>> print(f"'{c}'.isdigit() : {c.isdigit()}")
>>> print(f"'{d}'.isdigit() : {d.isdigit()}")
>>> print(f"'{e}'.isdigit() : {e.isdigit()}")
>>> print(f"'{f}'.isdigit() : {f.isdigit()}")
>>> print(f"'{g}'.isdigit() : {g.isdigit()}")
>>> print(f"'{h}'.isdigit() : {h.isdigit()}")
>>> print(f"'{i}'.isdigit() : {i.isdigit()}")
```
```python
str.isdigit('BlockDMask') : False
str.isdigit('1234Blog') : False
str.isdigit('131231') : True
str.isdigit('-234') : False
str.isdigit('1.23') : False
str.isdigit('3²') : True
str.isdigit('⅔') : False
str.isdigit('0') : True
str.isdigit('0123') : True

'BlockDMask'.isdigit() : False
'1234Blog'.isdigit() : False
'131231'.isdigit() : True
'-234'.isdigit() : False
'1.23'.isdigit() : False
'3²'.isdigit() : True
'⅔'.isdigit() : False
'0'.isdigit() : True
'0123'.isdigit() : True
```

#### math.comb(n,k) nCk | 조합
```python
import math

n = 10
k = 2

nCk = math.comb(n,k)
print(nCk)
```
```python
45
```
