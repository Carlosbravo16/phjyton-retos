from xml.dom.minidom import Notation


totalnota=0
for i in range(0,4,1):
    nota=float(input("digitar la nota \n"))
    print(f"la sumatoria de las  notas es, {nota}")
    totalnota=totalnota+nota
final=totalnota/4
print(f"su nota final es, {final}")
if final<=0 and final<=2.90:
        print("si la nota esta de 0.0 hasta 2.9, reprobaste la asignatura!.. ")
elif final<=4.0:
        print("si la nota esta entre 3.0 hasta 4.0, pasaste raspando la asignatura!... ")
elif final>4.0 and final<=5:
        print("si la nota esta de 4.0 para arriba, aprobaste con buenos resulatdos!... ")
else:
    print("si la nota es mayor a 5, es error de sintaxis!...")
print(f"hay una falla{final}")