import sys

N = int(sys.stdin.readline())
new_list=[]
for i in range(N):
    input_str = sys.stdin.readline()
    check = input_str[:3]
    if check == 'pus':
        new_list.append(int(input_str[5:]))
    elif check == 'top':
        if len(new_list) == 0:
            print(-1)
        else:
            print(new_list[-1])
    elif check == 'siz':
        print(len(new_list))
    elif check == 'emp':
        if len(new_list) == 0:
            print(1)
        else:
            print(0)
    elif check == 'pop':
        if len(new_list) == 0:
            print(-1)
        else:
            print(new_list[-1])
            new_list=new_list[:-1]