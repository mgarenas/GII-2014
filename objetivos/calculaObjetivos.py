import re
import os
import sys

# Calcula el porcentaje de objetivos cumplidos del total de objetivos escritos
# Parámetro: el nombre del fichero de objetivos
# Si no se especifica ninguno se iterará sobre la lista de alumnos

COMPLETADAS = """\[\s?(x|X)\s?\]"""
NOCOMPLETADAS = """\[(\s?)+\]"""
EXCLUDE = ['clean.sh','JJ.md',sys.argv[0],'.DS_Store','README.md']

def getObjetivos(file):
    f = open(file)
    data = f.read()
    f.close()

    completados = len(re.findall(COMPLETADAS, data))
    nocompletados = len(re.findall(NOCOMPLETADAS, data))
    total = completados+nocompletados
    cp = 1.0*completados/total*100
    ncp = 1.0*nocompletados/total*100

    print "Objetivos de " + file[:-3] + ": " + str(total)
    print "  Completados: " + str(completados) + " [" + str(cp) + "%]"
    print "  No completados: " + str(nocompletados) + " [" + str(ncp) + "%]"
    print


if len(sys.argv)==1:
    alumnos = os.listdir("./")
    for al in alumnos:
        if ".md" in al and al not in EXCLUDE:
            getObjetivos(al)
elif len(sys.argv)==2:
    getObjetivos(sys.argv[1])
