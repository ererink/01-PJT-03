import sys

T = int(input())
for test_case in range(1, T + 1):


    list1 = ['b', 'd', 'p', 'q']
    list2 = ['d', 'b', 'q', 'p']
    
    list1 = list2
    
    chars = input()
    result = []
    
    for i in range(len(list1)):
        result.append(chars[i])
        
    print(result[::-1])

sys.stdin = open("_문자열의거울상.txt")

# 시도 2
t = int(input())
for test_case in range(1, t+1):
  chrs = input() #bdppq
  origin_list = ['b', 'd', 'p', 'q']
  new_list = ['d', 'b', 'q', 'p']

  result = []
  for i in chrs:
    for j in origin_list:
     if i in j: 
      result.append(new_list.index(j)) # new_list의 값을 불러와 저장하지 못함

  print(result[::-1])