print('EDITA EL PDF INICIAL')
#################################################################
# Este codigo genera un archivo '.tex' que permita facilitar
# la tarea de edicion preliminar, es decir, agregar/quitar hojas
# en blanco, girar paginas, etc.
#
# n = numero de paginas del documento
#
#################################################################

nombre_input='manual_escenotecnia.pdf'
nombre_output='latex_edit.tex'
n=136

a=open(nombre_output+'.tex','w')	#crea los cuadernillos
a.write('\documentclass{article}')	#preambulo latex
a.write('\n')
a.write('\usepackage{pdfpages}')		#preambulo latex
a.write('\n')
a.write(r'\begin{document}')		#preambulo latex
a.write('\n')
a.write('\n')

for i in range(1,n+1):
	a.write('\includepdf[pages={'+str(i)+'}]{'+nombre_input+'}\n')

a.write('\end{document}')
a.close()

# SI SE QUIERE AGREGAR UNA PAGINA EN BLANCO, ESCRIBIR
#\newpage
#\thispagestyle{empty}
#\mbox{}
