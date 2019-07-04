n, c = input().split()
b = int(c)
[print((i*'.|.').rjust(b//2-1, '-')+'.|.'+(i*'.|.').ljust(b//2-1, '-')) for i in range(int(n)//2)]
print('WELCOME'.center(b, '-')) # ei line ta ke upore, nice kono line a dea jabe ??
[print((i * '.|.').rjust(b//2-1, '-') + '.|.' + (i * '.|.').ljust(b//2-1, '-')) for i in range(int(n)//2,-1,-1)]
[print(i)for i in range(5,-1,-1)]
