import sys


T = int(input())
for test_case in range(1, T + 1):
    card_nums = input().split()
    result=[]
    for i in card_nums:
        result += i
    
        if result[0] == '3' or '4' or '5' or '6' or '9': 
            if len(result) == 16:
                print('#{} {}'.format(test_case, '1'))
            elif '-' in result:
                for _ in result:
                    result.remove('-')
                    
                    if len(result) == 16:
                        break
                    
                print('#{} {}'.format(test_case, '1'))
            
            else:
                print('#{} {}'.format(test_case, '0'))
        else:
            print('#{} {}'.format(test_case, '0'))
            
sys.stdin = open("_신용카드만들기2.txt")

# 시도 2
t = int(input())
for test_case in range(1, t+1):
  card_nums = input()

  if card_nums[0] != '3' or '4' or '5' or '6' or '9': # or에서 맨 앞 조건이 충족하여 다른 or를 보지 않고 넘어감
    print('#{} {}'.format(test_case, '0'))
    if '-' in card_nums:
      card_nums = card_nums.replace('-', '')
      if len(card_nums) != 16:
        print('#{} {}'.format(test_case, '0'))

  elif len(card_nums) != 16:
    print('#{} {}'.format(test_case, '0'))

  else:
    print('#{} {}'.format(test_case, '1'))