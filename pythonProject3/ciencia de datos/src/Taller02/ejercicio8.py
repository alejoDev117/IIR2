import shutil

shutil.copy("IIR2.txt", "IIR2Colombia/IA")
shutil.copy("IIR2Colombia/IA/IIR2.txt", "IIR2Colombia/scripts")
shutil.move("IIR2Colombia/scripts/IIR2.txt", "IIR2Colombia/scripts/dataset.txt")
