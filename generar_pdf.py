import os
print('CREACION DE CUADERNILLOS PDF')

######################################################################
# Este codigo compila los archivos '.tex' en '.pdf' utilizando
# el comando 'pdflatex' en el terminal
#
# c = numero de cuadernillos final (inclusive cuadernillo extra)
# 	(c = N si indicador = 0 ; c = N +1 si indicador = 1)
#
######################################################################

c=4
for k in range(c):
	os.system("pdflatex c"+str(k)+".tex")

os.system("find . -name '*.log' -delete ")
os.system("find . -name '*.aux' -delete ")
os.system("find . -name '*.tex' -delete ")
