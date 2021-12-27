# coding:utf-8

la = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
lb = ['个','拾','佰','仟','万']

num_origin = '01234'
num_list = list(num_origin)

size = len(num_list)

num_str_list = []

for i in range(size):
    n = num_list[i]
    n = int(n)

    n_a = la[n]
    n_b = lb[size - 1 - i]

    if size - 1 - i == 0:
        n_str = n_a
    else:
        n_str = f'{n_a}{n_b}'
    
    num_str_list.append(n_str)

result = ''.join(num_str_list)

print(result)