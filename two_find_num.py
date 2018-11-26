
####列表
l = [0,11,22,33,43,56,78,99,120]
#要查找的数字
n = 78
#查找数字的下标
c = 0
def two_find_num(lst,n):
	global c
	mid = len(lst)//2
	c += mid
	if len(lst) == 2:
		if lst[0] == n:
			c = c -1
			print(n,'找到了，下标是',c)
			return
		elif lst[1] == n:
			print(n,'找到了，下标是',c)
			return
		else:
			print('没有找到')
	elif lst[mid] > n:
		c = c - mid
		two_find_num(lst[mid:],n)
	elif lst[mid] < n:
		two_find_num(lst[:mid],n)
	elif lst[mid] == n:
		print(n,'找到了，下标是',c)
		return
two_find_num(l,n)




