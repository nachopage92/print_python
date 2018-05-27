import os

n=4

for i in range(n-1,-1,-1)
	os.system('lp -o PageSize=Letter -o page-set=even -o number-up=2 -o fit-to-page c'+i+'.pdf)

