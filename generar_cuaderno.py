print('CREACION DE CUADERNILLOS LATEX')

###########################################################################
# Este codigo crea N cuadernillos de M hojas para imprimir.
# N = numero de cuadernillos completos
# M = numero de hojas por cada N cuadernillo
# pdf = nombre del archivo PDF a leer
# pag = numero de paginas del archivo PDF
# indicador = indica si el ultimo cuadernillo es distinto (0=no, 1=si)
# MM = numero de hojas del cuadernillo extra
#
#
# EXPLICACION
# Se ingresan los parametros N y M, el programa crear un archivo '.tex'
# que permite crear N archivos PDF de M hojas cada uno. Esta primera version
# se trabaja con un PDF previamente modificado para usarse. El PDF tiene  
# una cantidad par de hojas, se crean los primeros pag/N cuadernillos.
# el resto, es decir, pag%N (que corresponde a un numero par) se formara 
# por un cuadernillo con menos hojas
# 
#
# EJEMPLO: se quiere imprimir 16 paginas en un cuadernillo de 4 hojas
# (4 paginas por cuadernillo). El orden es el siguiente
# 16 - 1
# 2 - 15
# 14 - 3
# 4 - 13
# 12 - 5
# 6 - 11
# 10 - 7
# 8 - 9
#
#
# FUTURAS CONSIDERACIONES: 
# -generalizar el codigo
# -automatizar el proceso de impresion
# -trabajar con cualquier documento, sean cant. de hojas pares o impares
# -...
#
###########################################################################



#INPUT
N=4 #numero de cuadernillos
M=3	#numero de hojas por cuadernillo
pdf='manual_escenotecnia'
pag=60
indicador=1 
MM=3

contador=0

for i in range(N): 			#numero de cuadernillos
	string='c'+str(i)
	a=open(string+'.tex','w')	#crea los cuadernillos
	a.write('\documentclass{article}')	#preambulo latex
	a.write('\n')
	a.write('\usepackage{pdfpages}')		#preambulo latex
	a.write('\n')
	a.write(r'\begin{document}')		#preambulo latex
	a.write('\n')
	a.write('\n')
	

	aux=4*M
	for j in range(2*M):	
		contador=contador+1
		if (contador+1)%2==0:
			a.write('\includepdf[pages={'+str(i*aux+(aux-j))+'}]{'+pdf+'}\n')
			a.write('\includepdf[pages={'+str(i*aux+1+j)+'}]{'+pdf+'}\n')	
		else:
			a.write('\includepdf[pages={'+str(i*aux+1+j)+'}]{'+pdf+'}\n')
			a.write('\includepdf[pages={'+str(i*aux+(aux-j))+'}]{'+pdf+'}\n')

	a.write('\end{document}')
	a.close()


if(indicador==1):
	contador=0
	i=i+1
	string='c'+str(i)
	a=open(string+'.tex','w')	#crea los cuadernillos
	a.write('\documentclass{article}')	#preambulo latex
	a.write('\n')
	a.write('\usepackage{pdfpages}')		#preambulo latex
	a.write('\n')
	a.write(r'\begin{document}')		#preambulo latex
	a.write('\n')
	a.write('\n')
	aux2=4*MM
	for j in range(2*MM):
		contador=contador+1
		if (contador+1)%2==0:
			a.write('\includepdf[pages={'+str(i*aux+(aux2-j))+'}]{'+pdf+'}\n')
			a.write('\includepdf[pages={'+str(i*aux+1+j)+'}]{'+pdf+'}\n')	
		else:
			a.write('\includepdf[pages={'+str(i*aux+1+j)+'}]{'+pdf+'}\n')
			a.write('\includepdf[pages={'+str(i*aux+(aux2-j))+'}]{'+pdf+'}\n')
	a.write('\end{document}')
	a.close()
	
	
	
	
