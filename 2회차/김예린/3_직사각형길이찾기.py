import sys

t = int(input())
for test_case in range(1, t+1):
  a, b, c = map(int, input().split())

  if a == b:
    print('#{} {}'.format(test_case, c))
  elif b == c:
    print('#{} {}'.format(test_case, a))    
  elif a == c:
    print('#{} {}'.format(test_case, b))    
  else:
    print('#{} {}'.format(test_case, a))
    
sys.stdin = open("_직사각형길이찾기.txt")
