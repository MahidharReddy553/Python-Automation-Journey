import l_ops

l = [46, 96, 69, 45, 68, 68, 54, 32, 65, 22, 10]
nf = 0
np = 0

avg = l_ops.l_sum(l)//len(l)
h = l_ops.l_max(l)
low = l_ops.l_min(l)

for i in l:
    if i >= 35:
        np += 1
    else:
        nf += 1

print('avg', avg)
print('highest', h)
print('lowest', low)
print('passed', np)
print('failed', nf)