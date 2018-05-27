import os

n=4

for i in range(n)
	os.system('lp -o PageSize=Letter -o page-set=odd -o number-up=2 -o fit-to-page c'+i+'.pdf)

