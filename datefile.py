
def read_file(filename):
	lines=[]
#	with open(filename,'r',encoding='utf-8-sig') as f:
#   utf-8無法讀取天氣紀要，ISO-8859-1可以，但會變encoding碼
	with open(filename,'r',encoding='ISO-8859-1') as f:
		for line in f:
#			for line in f :
#				if 'METEO' in line:
#					continue
#				elif 'DATE :' in line:
#					continue
#				elif 'TIME  P2' in line:
#					continue
#				else:
#					range(24)
					lines.append(line.strip())

	return(lines)
def main():
	times = []
#	k = 0
	lines = read_file('4670520210330_ACOS.txt')
	for i in range(2,27):
		print(lines[i])
		times.append(lines[i][0:4])
#		print(times[k])
#		k = k + 1
	print(times)
main()