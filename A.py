strings = ['a','as','bat','car','dove','python']
[print(x.upper()) for x in strings if len(x) > 2]

unique_lengths = {len(x) for x in strings}
print(unique_lengths)

print(set(map(len, strings)))

loc_mapping = {val : index for index, val in enumerate(strings)}
print(loc_mapping)

all_data = [['John','nn'],['qq,gb,ng']]
all = {n for name in all_data for n in name if n.count('n') >=2}
print(all)

some_touple = [(1,2,3) , (4,5,6) , (7,8,9)]

flattend = [x for tup in some_touple for x in tup]
print(flattend)

print([[x for x in tup] for tup in some_touple])

nums = [(1,1,1) , (2,2,2) , (3,3,3)]
print([[n for n in num] for num in nums])

states = ['Alabama','Georgia!','Georgia','georgia','FlOrIda','southcarolina##','West virginia?']

import re

def clean_strings(strings) :
    result = []
    for value in strings :
        value = value.strip()   #strip() 앞뒤 공백 제거
        value = re.sub('[#?!]','',value) #re.sub문자열 치환
        value = value.title()
        result.append(value)
    return result
print(clean_strings(states))
print('-------------------------------------------------------------')
def remove_punctuation(value) :
    return re.sub('[#?!]','',value)

clean_ops = [str.strip,remove_punctuation,str.title]    # 함수로 객체 저장

def cleanstrings(string, ops):
    result = []
    for value in string:
        for func in ops:
            value = func(value)
        result.append(value)
    return result

print(cleanstrings(states,clean_ops))
print('-------------------------------------------------------------')
for x in map(remove_punctuation,states) :
    print(x)
print('-------------------------------------------------------------')

def short_function(x):
    return x * 2
equiv_anon = lambda x: x * 2

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4,0,1,5,6]
a = apply_to_list(ints, lambda x:x * 2)
print(a)
print('-------------------------------------------------------------')

ss = [1,2,3,4,5]

s = apply_to_list(ss, lambda x:x+1)
print(s)
print('-------------------------------------------------------------')

strings = ['foo','card','bar','aaaa','abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)
print('-------------------------------------------------------------')
st = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'
st_list = list(st)
t = list(map(lambda c: ord('E')-ord(c),st_list)) #ord는 아스키코드값을 반환
print(sum(t))
print('-------------------------------------------------------------')

#1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
# 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.

target = list(range(1,11))

result = list(filter(lambda x: x%2==0, target)) #filter
print(result)
print('-------------------------------------------------------------')
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
# 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
result2 = list(map(lambda x: pow(x,2), target)) # pow() x의 제곱
print(result2)
print('-------------------------------------------------------------')
# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
# 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는
# 프로그램을 작성하십시오.

result3 = list(map(lambda x: pow(x,2), result))
print(result3)
print('-------------------------------------------------------------')

def add_numbers(x, y):
    return x + y
add_five = lambda y: add_numbers(5, y)

from functools import partial #함수를 만들어 넘길때 자주 사용 partial(함수,매개변수값)
add_five = partial(add_numbers, 5)
print(str(add_five))
print('-------------------------------------------------------------')

some_dict = {'a':1, 'b':2, 'c':3}
for key in some_dict:
    print(key)
dict_iterator = iter(some_dict)
print(list(iter(dict_iterator))) #순환하는 객체 iter

def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n**2))
    for i in range(1, n+1):
        yield i**2              # yield는 return과 비슷한 뜻
gen = squares()
print(list(gen))

gen = (x ** 2 for x in range(100))
print(list(gen))
print('-------------------------------------------------------------')
import itertools        # 일반 데이터 알고리즘을 위한 많은 제너레이터를 포함하고 있다.
first_letter = lambda x: x[0]
names = ['Alan','Adam','Wes','Will','Albert','Steven']
for letter, names in itertools.groupby(names,first_letter):
    print(letter, list(names))

#유용한 itertools 함수
#combinations(iterable, k) : iterable에서 순서를 고려하지 않고 길이가 k인 모든 가능한 조합을 생성한다.
#permutations(iterable, k) : iterable에서 순서를 고려하여 길이가 k인 모든 가능한 조합을 생성한다.
#groupby(iterable[, keyfunc]) : iterable에서 각각의 고유한 키에 따라 그룹을 생성한다.
#product(*iterables, repeat=1) : iterable에서 카테시안 곱을 구한다. 중첩된 for문 사용과 유사하다.
