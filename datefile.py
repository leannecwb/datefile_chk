
def read_file(filename):
	lines=[]
#	with open(filename,'r',encoding='utf-8-sig') as f:
#   utf-8無法讀取天氣紀要，ISO-8859-1可以，但會變encoding碼
	with open(filename,'r',encoding='ISO-8859-1') as f:
		for line in f:

					lines.append(line.strip())

	return(lines)
def read_data_h(item,lines):
	data = []
	if item == 'times':
		for i in range(3,27):
			data.append(lines[i][0:4])
	elif item == 'P2':
		for i in range(3,27):
			data.append(lines[i][5:9])
	elif item == 'P1':
		for i in range(3,27):
			data.append(lines[i][10:14])
	elif item == 'T':
		for i in range(3,27):
			data.append(lines[i][16:19])
	elif item == 'E':
		for i in range(3,27):
			data.append(lines[i][20:24])
	elif item == 'RH':
		for i in range(3,27):
			data.append(lines[i][26:29])		
	elif item == 'Td':
		for i in range(3,27):
			data.append(lines[i][31:34])
	elif item == 'n8':
		for i in range(3,27):
			data.append(lines[i][35:36])
	elif item == 'l':
		for i in range(3,27):
			data.append(lines[i][36:37])
	elif item == 'm':
		for i in range(3,27):
			data.append(lines[i][37:38])
	elif item == 'h':
		for i in range(3,27):
			data.append(lines[i][38:39])
	elif item == 'NN':
		for i in range(3,27):
			data.append(lines[i][40:42])
	elif item == 'WD':
		for i in range(3,27):
			data.append(lines[i][43:45])
	elif item == 'Ws':
		for i in range(3,27):
			data.append(lines[i][46:49])
	elif item == 'R':
		for i in range(3,27):
			data.append(lines[i][50:54])
	elif item == 'RT':
		for i in range(3,27):
			data.append(lines[i][55:57])
	elif item == 'S':
		for i in range(3,27):
			data.append(lines[i][58:60])
	elif item == 'VVV':
		for i in range(3,27):
			data.append(lines[i][61:64])
	elif item == 'E':
		for i in range(3,27):
			data.append(lines[i][65:66])
	elif item == 'C': #thunderstorm
		for i in range(3,27):
			data.append(lines[i][66:67])
	elif item == 'lr': #rain etc.
		for i in range(3,27):
			data.append(lines[i][67:68])
	elif item == 'sor': #snow etc.
		for i in range(3,27):
			data.append(lines[i][69:72])
	elif item == 'ii': #fog etc...
		for i in range(3,27):
			data.append(lines[i][72:73])
	elif item == 'CH': #High Cloud
		for i in range(3,27):
			data.append(lines[i][75:77])
	elif item == 'HT':
		for i in range(3,27):
			data.append(lines[i][78:80])
	elif item == 'CM': #Middle Cloud
		for i in range(3,27):
			data.append(lines[i][81:83])
	elif item == 'MT':
		for i in range(3,27):
			data.append(lines[i][84:86])
	elif item == 'CL':
		for i in range(3,27):
			data.append(lines[i][87:89])
	elif item == 'CIL':
		for i in range(3,27):
			data.append(lines[i][91:94])
	elif item == 'CT':
		for i in range(3,27):
			data.append(lines[i][95:97])
	elif item == 'Rr':
		for i in range(3,27):
			data.append(lines[i][98:102])
	elif item == 'GR':
		for i in range(3,27):
			data.append(lines[i][103:107])
	elif item == 'fx':
		for i in range(3,27):
			data.append(lines[i][108:111])
	elif item == 'xd':
		for i in range(3,27):
			data.append(lines[i][112:114])
	elif item == 'appp':
		for i in range(3,27):
			data.append(lines[i][115:119])
	elif item == 'evop':
		for i in range(3,27):
			data.append(lines[i][120:124])
	elif item == 'ww':
		for i in range(3,27):
			data.append(lines[i][125:127])
	elif item == 'WWp':
		for i in range(3,27):
			data.append(lines[i][128:130])
	elif item == '10D':
		for i in range(3,27):
			data.append(lines[i][136:138])
	elif item == 'F10':
		for i in range(3,27):
			data.append(lines[i][140:143])
	elif item == 'UVI':
		for i in range(3,27):
			data.append(lines[i][144:148])
	else:
		print('你所輸入的item並無在清單裡面，請至read_data_h中確認!')
	return data

def read_max_data_T(item,lines):
	datamax=[]
	if item == 'P2Max':
		maxvalue = lines[30][5:9]
		maxvalueT = lines[31][5:9]
		datamax = [maxvalue,maxvalueT]
		return datamax
	else :
		print('not right!')
	return datamax	

def main():

	lines = read_file('4670520210330_ACOS.txt')
#	for i in range(2,27):
#		print(lines[i])
#		times.append(lines[i][0:4])
#		print(times[k])
#		k = k + 1
	times = read_data_h('times',lines)
#	UVI = read_data_h('UVI',lines)
#	print(times)
#	print(UVI)
#	print('max value ...')
#	P2Max = read_max_data_T('P2Max',lines)
#	print(P2Max[1])
	print('檢查日期檔開始...')
	print('++++++++   1. 檢查P2值的極值時間是否合理   +++++++')
	P2 = read_data_h('P2',lines)
	print(P2)
	p2_findmax = max(P2)
	loc = P2.index(max(P2))
	print(times[loc])
	P2Max = read_max_data_T('P2Max',lines)
	print(P2Max)
	# check if P2Max >= p2_findmax
	if float(P2Max[0]) >= float(p2_findmax) :
		print('P2日極值 >= P2小時最大值，檢查通過...')
	else :
		print('P2日極值(',P2Max,') < P2小時最大值('.p2_findmax,')，數值有問題請進行確認!!!')

main()