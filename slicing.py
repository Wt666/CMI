
a="ABCD"

b="my name is wt"
reverse_a=a[::-1]
print(reverse_a)
print(b.title())
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
print('\n'.join([''.join([('lovelovelove'[(x-y)%12]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))


