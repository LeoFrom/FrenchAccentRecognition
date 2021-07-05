#/usr/bin/env python
# coding : utf-8

import glob as glb
import pandas as pd
import os
import shutil

files_path = "F:\\Projet RNN\\Datas\\clips\\"
tableauLangue = ["france","belgium","canada","switzerland"]
datas = []

def lecture(tableurTSV, dossierPath):
	with open(tableurTSV, encoding ="utf-8") as file:
		for line in file :
			line = line.strip("\n").split("\t")
			if line[7] in tableauLangue:
				name, sentence, age , sex , accent = line[1], line[2], line[5] , line[6] , line[7]
				sound = files_path + name
				datas.append([name, sentence, age , sex , accent, sound])


# lecture("validated.tsv",files_path)

# datas = pd.DataFrame(datas, columns = ["name","sentence","age","sex","accent","path"])
# datas.to_csv("datas.tsv", index = None, sep='\t')

vocal_fr = []
vocal_ca = []
vocal_sw = []
vocal_bl = []

vocal_fr_sorted = []
vocal_ca_sorted = []
vocal_sw_sorted = []
vocal_bl_sorted = []

needed = ["twenties","thirties","fourties"]

def separate(datas):
	not_found_fr = 0
	not_found_bl = 0
	not_found_sw = 0
	not_found_ca = 0
	with open(datas, encoding="utf-8") as file:
		for line in file:
			line = line.strip("\n").split("\t")

			if line[4] == "france":
				vocal_fr.append(line)
				files_path = "F:\\Projet RNN\\Datas\\france"
				if glb.glob(line[5]) != []:
					shutil.copy(line[5], files_path)
					#sorted
					if line[3] == "male" and line[2] in needed:
						vocal_fr_sorted.append(line)
						files_path = "F:\\Projet RNN\\Datas\\france\\france_sorted"
						shutil.copy(line[5], files_path)
				else :
					not_found_fr+=1

			if line[4] == "belgium":
				vocal_bl.append(line)
				files_path = "F:\\Projet RNN\\Datas\\belgium"
				if glb.glob(line[5]) != []:
					shutil.copy(line[5], files_path)
					#sorted
					if line[3] == "male" and line[2] in needed:
						vocal_bl_sorted.append(line)
						files_path = "F:\\Projet RNN\\Datas\\belgium\\belgium_sorted"
						shutil.copy(line[5], files_path)
				else :
					not_found_bl+=1

			if line[4] == "switzerland":
				vocal_sw.append(line)
				files_path = "F:\\Projet RNN\\Datas\\switzerland"
				if glb.glob(line[5]) != []:
					shutil.copy(line[5], files_path)
					#sorted
					if line[3] == "male" and line[2] in needed:
						vocal_sw_sorted.append(line)
						files_path = "F:\\Projet RNN\\Datas\\switzerland\\switzerland_sorted"
						shutil.copy(line[5], files_path)
				else :
					not_found_sw+=1

			if line[4] == "canada":
				vocal_ca.append(line)
				files_path = "F:\\Projet RNN\\Datas\\canada"
				if glb.glob(line[5]) != []:
					shutil.copy(line[5], files_path)
					#sorted
					if line[3] == "male" and line[2] in needed:
						vocal_ca_sorted.append(line)
						files_path = "F:\\Projet RNN\\Datas\\canada\\canada_sorted"
						shutil.copy(line[5], files_path)
				else :
					not_found_ca+=1

	
	print(not_found_fr, ": Nombre de fichiers FR sans sons")
	print(not_found_sw, ": Nombre de fichiers SW sans sons")
	print(not_found_bl, ": Nombre de fichiers BL sans sons")
	print(not_found_ca, ": Nombre de fichiers CA sans sons")			
	print(not_found_fr + not_found_sw + not_found_ca + not_found_bl , ": Nombre de fichiers n'ayant pas de sons")

separate("datas.tsv")

#all
# vocal_fr = pd.DataFrame(vocal_fr, columns = ["name","sentence","age","sex","accent","path"])
# vocal_fr.to_csv("france.tsv", index = None, sep='\t')

# vocal_ca = pd.DataFrame(vocal_ca, columns = ["name","sentence","age","sex","accent","path"])
# vocal_ca.to_csv("canada.tsv", index = None, sep='\t')

# vocal_sw = pd.DataFrame(vocal_sw, columns = ["name","sentence","age","sex","accent","path"])
# vocal_sw.to_csv("switzerland.tsv", index = None, sep='\t')

# vocal_bl = pd.DataFrame(vocal_bl, columns = ["name","sentence","age","sex","accent","path"])
# vocal_bl.to_csv("belgium.tsv", index = None, sep='\t')

#sorted
# vocal_fr_sorted = pd.DataFrame(vocal_fr_sorted, columns = ["name","sentence","age","sex","accent","path"])
# vocal_fr_sorted.to_csv("france_sorted.tsv", index = None, sep='\t')

# vocal_ca_sorted = pd.DataFrame(vocal_ca_sorted, columns = ["name","sentence","age","sex","accent","path"])
# vocal_ca_sorted.to_csv("canada_sorted.tsv", index = None, sep='\t')

# vocal_sw_sorted = pd.DataFrame(vocal_sw_sorted, columns = ["name","sentence","age","sex","accent","path"])
# vocal_sw_sorted.to_csv("switzerland_sorted.tsv", index = None, sep='\t')

# vocal_bl_sorted = pd.DataFrame(vocal_bl_sorted, columns = ["name","sentence","age","sex","accent","path"])
# vocal_bl_sorted.to_csv("belgium_sorted.tsv", index = None, sep='\t')

