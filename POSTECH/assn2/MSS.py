import sys
import operator 
from functools import reduce
# seq = tuple(map(int,sys.stdin.readline().split()))

# print(seq)

seq = (1,-2,3,-4,5,-3,8,-9,22)
print(seq)

max = operator.add(seq[0], seq[1])
max_idx = 0
length = 1

for idx in range(1,len(seq)-1,1):

    if max < (operator.add(seq[idx], seq[idx+1])):
        max = operator.add(seq[idx], seq[idx+1])
        max_idx = idx
        length += 1 


print()

    
def find_front(target_idx):
    if operator.eq(target_idx, 0):
        return -1
    
    if operator.gt(seq[target_idx], 0): # seq[target_idx] > 0
        return target_idx
    else:
        return find_front(operator.add(target_idx, -1))
        
    


front = max_idx -1
back = max_idx + length



while front >= 0 : 

    if operator.gt(seq[front], 0 ): # seq
        max_idx = operator.add(max_idx, -1)
        length = operator.add(length, 1)
        front = operator.add(front, -1)

        # 더한 후, 다음 친구도 검사할거임 
    else : # 0 보다 작은 경우 
        #지금 위치로부터, 양수 위치 찾아 주는 함수  있으면 인덱스, 없으면 -1 
        sub_idx = find_front(front)
        print("sub_idx :",sub_idx)
        print("now idx",max_idx)

        if sub_idx:
            print("sum",reduce(operator.add , seq[sub_idx:max_idx]))
            if(reduce(operator.add , seq[sub_idx:max_idx]) > 0):
                print("hi")
                length += operator.sub(max_idx, sub_idx)
                max_idx = sub_idx
                front = max_idx -1
            
            else:
                break
        



print("now idx",max_idx)
print("now length",length)
print("sum",reduce(operator.add , seq[max_idx:max_idx+length]))