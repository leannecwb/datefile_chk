# 日期檔檢核程式
# Author : Leanne, Tai
# Updated : 2021/05/03

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
	elif item == 'P1Max':
		maxvalue = lines[30][10:14]
		maxvalueT = lines[31][10:14]
		datamax = [maxvalue,maxvalueT]
	elif item == 'TMax':
		maxvalue = lines[30][15:19]
		maxvalueT = lines[31][15:19]
		datamax = [maxvalue,maxvalueT]
	elif item == 'TdMax':
		maxvalue = lines[30][31:34]
		maxvalueT = lines[31][30:34]
		datamax = [maxvalue,maxvalueT]
	elif item == 'fxMax':
		maxvalue = lines[30][46:49]
		maxvalueT = lines[31][45:49]
		datamax = [maxvalue,maxvalueT]
	elif item == 'F10Max':
		maxvalue = lines[35][46:49]
		maxvalueT = lines[36][45:49]
		datamax = [maxvalue,maxvalueT]
	else :
		print('not right!')
	return datamax	

def read_min_data_T(item,lines):
	datamax=[]
	if item == 'P2Min':
		minvalue = lines[33][5:9]
		minvalueT = lines[34][5:9]
		datamin = [minvalue,minvalueT]
	elif item == 'P1Min':
		minvalue = lines[33][10:14]
		minvalueT = lines[34][10:14]
		datamin = [minvalue,minvalueT]
	elif item == 'TMin':
		minvalue = lines[33][15:19]
		minvalueT = lines[34][15:19]
		datamin = [minvalue,minvalueT]
	elif item == 'TdMin':
		minvalue = lines[33][31:34]
		minvalueT = lines[34][30:34]
		datamin = [minvalue,minvalueT]
	else :
		print('not right!')
	return datamin

def locate(loc):
	if loc == 0 :
		loc_inv = [0,1]
	elif loc == 23 :
		loc_inv = [22,23]
	else :
		loc_inv = [loc-1,loc+1]
	return loc_inv

def main():
	inputfile = input('請輸入日期檔:')
	lines = read_file(inputfile)
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
	print('\n\n檢查日期檔開始...\n\n')
	print('=============================================================================\n')
	print('+++++++++++++++   1. 檢查P2值的極值時間是否合理   ++++++++++++++')
	P2 = read_data_h('P2',lines)
#	print(P2)
	p2_findmax = max(P2)
	loc = P2.index(max(P2))
	p2_findmin = min(P2)
	loc2 = P2.index(min(P2))
	loc_inv = locate(loc)
	loc_inv1 = locate(loc2)
#	print('TIMES:',times[loc2])
	P2Max = read_max_data_T('P2Max',lines)
	P2Min = read_min_data_T('P2Min',lines)
	#print(P2Min)
	# check if P2Max >= p2_findmax
	if float(P2Max[0]) >= float(p2_findmax) :
		print('     o  P2日極大值(',P2Max[0],') >= P2小時最大值(',p2_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! P2日極大值(',P2Max[0],') < P2小時最大值(',p2_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(P2Max[1]) >= float(times[loc_inv[0]]) and  float(P2Max[1]) <= float(times[loc_inv[1]]):
		print('     o  P2日極大值時間(',P2Max[1],') 接近P2小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! P2日極大值時間(',P2Max[1],') 離P2小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
#   P2 日極小值檢查
	if float(P2Min[0]) <= float(p2_findmin) :
		print('     o  P2日極小值(',P2Min[0],') <= P2小時最小值(',p2_findmin,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! P2日極小值(',P2Min[0],') > P2小時最小值(',p2_findmin,')，數值可能有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(P2Min[1]) >= float(times[loc_inv1[0]]) and  float(P2Min[1]) <= float(times[loc_inv1[1]]):
		print('     o  P2日極小值時間(',P2Min[1],') 接近P2小時最小值時間(',times[loc2],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! P2日極小值時間(',P2Min[1],') 離P2小時最小值時間(',times[loc2],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')

	print('+++++++++++++++   2. 檢查P1值的極值和時間是否合理   ++++++++++++++')
	P1 = read_data_h('P1',lines)
	p1_findmax = max(P1)
	loc = P1.index(max(P1))
	p1_findmin = min(P1)
	loc1 = P1.index(min(P1))
	loc_inv = locate(loc)
	loc_inv1 = locate(loc1)
#	print('TIMES:',times[loc2])
	P1Max = read_max_data_T('P1Max',lines)
	P1Min = read_min_data_T('P1Min',lines)
	#print(P1Min)
	# check if P1Max >= p1_findmax
	if float(P1Max[0]) >= float(p1_findmax) :
		print('     o  P1日極大值(',P1Max[0],') >= P1小時最大值(',p1_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! P1日極大值(',P1Max[0],') < P1小時最大值(',p1_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(P1Max[1]) >= float(times[loc_inv[0]]) and  float(P1Max[1]) <= float(times[loc_inv[1]]):
		print('     o  P1日極大值時間(',P1Max[1],') 接近P1小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! P1日極大值時間(',P1Max[1],') 離P1小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
#   P1 日極小值檢查
	if float(P1Min[0]) <= float(p1_findmin) :
		print('     o  P1日極小值(',P1Min[0],') <= P1小時最小值(',p1_findmin,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! P1日極小值(',P1Min[0],') > P1小時最小值(',p1_findmin,')，數值可能有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(P1Min[1]) >= float(times[loc_inv1[0]]) and  float(P1Min[1]) <= float(times[loc_inv1[1]]):
		print('     o  P1日極小值時間(',P1Min[1],') 接近P1小時最小值時間(',times[loc1],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! P1日極小值時間(',P1Min[1],') 離P1小時最小值時間(',times[loc1],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
	print('+++++++++++++++   3. 檢查P1的值是否皆小於P2   ++++++++++++++')
	j = 0
	for i in range(0,24):
		if float(P1[i]) < float(P2[i]) :
			continue
		else:
			print('------------------------------------------------------------------------------------')	
			print('     !!! P1',P1[i],'>= P2',P2[i],'at TIME:',times[i],'請檢查!!!')
			print('------------------------------------------------------------------------------------')
			j = j + 1
	if j == 0 :
		print('     o  測站氣壓P1值皆小於海平面氣壓P2,檢查通過...')
	print('+++++++++++++++   4. 檢查T的極值與時間是否合理   ++++++++++++++')
	T = read_data_h('T',lines)
	T_findmax = max(T)
	loc = T.index(max(T))
	T_findmin = min(T)
	loc1 = T.index(min(T))
	loc_inv = locate(loc)
	loc_inv1 = locate(loc1)
#	print('TIMES:',times[loc2])
	TMax = read_max_data_T('TMax',lines)
	TMin = read_min_data_T('TMin',lines)
	#print(P1Min)
	# check if P1Max >= p1_findmax
	if float(TMax[0]) >= float(T_findmax) :
		print('     o  T之日極大值(',TMax[0],') >= T之小時最大值(',T_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! T之日極大值(',TMax[0],') < T之小時最大值(',T_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(TMax[1]) >= float(times[loc_inv[0]]) and  float(TMax[1]) <= float(times[loc_inv[1]]):
		print('     o  T之日極大值時間(',TMax[1],') 接近T之小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! T之日極大值時間(',TMax[1],') 離T之小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
#   T 極小值檢查
	if float(TMin[0]) <= float(T_findmin) :
		print('     o  T之日極小值(',TMin[0],') <= T之小時最小值(',T_findmin,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! T之日極小值(',TMin[0],') > T之小時最小值(',T_findmin,')，數值可能有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(TMin[1]) >= float(times[loc_inv1[0]]) and  float(TMin[1]) <= float(times[loc_inv1[1]]):
		print('     o  T之日極小值時間(',TMin[1],') 接近T之小時最小值時間(',times[loc1],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! T之日極小值時間(',TMin[1],') 離T小時最小值時間(',times[loc1],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')

	print('+++++++++++++++   5. 檢查Td的極值與時間是否合理   ++++++++++++++')
	Td = read_data_h('Td',lines)
	Td_findmax = max(Td)
	loc = Td.index(max(Td))
	loc_inv = locate(loc)
	Td_findmin = min(Td)
	loc1 = Td.index(min(Td))
	loc_inv1 = locate(loc1)
#	print('TIMES:',times[loc2])
	TdMax = read_max_data_T('TdMax',lines)
	TdMin = read_min_data_T('TdMin',lines)
	#print(P1Min)
	# check if P1Max >= p1_findmax
	if float(TdMax[0]) >= float(Td_findmax) :
		print('     o  Td之日極大值(',TdMax[0],') >= Td之小時最大值(',Td_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! Td之日極大值(',TdMax[0],') < Td之小時最大值(',Td_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(TdMax[1]) >= float(times[loc_inv[0]]) and  float(TdMax[1]) <= float(times[loc_inv[1]]):
		print('     o  Td之日極大值時間(',TdMax[1],') 接近Td之小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! Td之日極大值時間(',TdMax[1],') 離Td之小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
#   Td 極小值檢查
	if float(TdMin[0]) <= float(Td_findmin) :
		print('     o  Td之日極小值(',TdMin[0],') <= Td之小時最小值(',Td_findmin,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! Td之日極小值(',TdMin[0],') > Td之小時最小值(',Td_findmin,')，數值可能有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')

# 需處理 index out of range 的問題...
	if  float(TdMin[1]) >= float(times[loc_inv1[0]]) and  float(TdMin[1]) <= float(times[loc_inv1[1]]):
		print('     o  Td之日極小值時間(',TdMin[1],') 接近Td之小時最小值時間(',times[loc1],')，檢查通過...')
	else:
		print('---------------------------------,---------------------------------------------------')	
		print('     !!! Td之日極小值時間(',TdMin[1],') 離Td小時最小值時間(',times[loc1],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')



	print('+++++++++++++++   6. 檢查fx的極值與時間是否合理   ++++++++++++++')
	fx = read_data_h('fx',lines)
	xd = read_data_h('xd',lines)
	fx_findmax = max(fx)
	loc = fx.index(max(fx))
	fxMax = read_max_data_T('fxMax',lines)
	xdMax = lines[32][47:49]
	loc_inv = locate(loc)
	
	
	# check if P1Max >= p1_findmax
	if float(fxMax[0]) == float(fx_findmax) :
		print('     o  fx之日極大值(',fxMax[0],') = fx之小時最大值(',fx_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! fx之日極大值(',fxMax[0],')不等於fx之小時最大值(',fx_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if  float(fxMax[1]) >= float(times[loc_inv[0]]) and  float(fxMax[1]) <= float(times[loc_inv[1]]):
		print('     o  fx之日極大值時間(',fxMax[1],') 接近fx之小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! fx之日極大值時間(',fxMax[1],') 離fx之小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')

	if float(xd[loc]) == float(xdMax) :
		print('     o  fx之極值風向xd(',xdMax,') = fx之最大值時的風向(',xd[loc],')，檢查通過...')
	else :
		print('------------------------------------------------------------------------------------')	
		print('     !!! fx之日極值風向xd(',xdMax,') 與fx_Max發生時間:',times[loc],'之風向(',xd[loc],')不同，請檢查!!!')
		print('------------------------------------------------------------------------------------')

	print('+++++++++++++++   7. 檢查F10的極值與時間是否合理   ++++++++++++++')
	F10 = read_data_h('F10',lines)
	D10 = read_data_h('10D',lines)
	Ws = read_data_h('Ws',lines)
	F10_findmax = max(F10)
	loc = F10.index(max(F10))
	F10Max = read_max_data_T('F10Max',lines)
	D10Max = lines[37][47:49]
	loc_inv = locate(loc)
	
	# check if P1Max >= p1_findmax
	if float(F10Max[0]) == float(F10_findmax) :
		print('     o  F10之日極大值(',F10Max[0],') = F10之小時最大值(',F10_findmax,')，檢查通過...')
	else :
		print('-------------------------------------------------------------------------------------')	
		print('     !!! F10之日極大值(',F10Max[0],')不等於F10之小時最大值(',F10_findmax,')，數值有問題請進行確認!!!')
		print('--------------------------------------------------------------------------------------')


	if float(F10Max[1]) >= float(times[loc_inv[0]]) and  float(F10Max[1]) <= float(times[loc_inv[1]]):
		print('     o  F10之日極大值時間(',F10Max[1],') 接近F10之小時最大值時間(',times[loc],')，檢查通過...')
	else:
		print('------------------------------------------------------------------------------------')	
		print('     !!! F10之日極大值時間(',F10Max[1],') 離F10之小時最大值時間(',times[loc],')稍遠，請檢查!!!')
		print('------------------------------------------------------------------------------------')
	
	if float(D10[loc]) == float(D10Max) :
		print('     o  F10之極值風向10D(',D10Max,') = F10之最大值時的風向(',D10[loc],')，檢查通過...')
	else :
		print('------------------------------------------------------------------------------------')	
		print('     !!! F10之日極值風向10D(',D10Max,') 與10D_Max發生時間:',times[loc],'之風向(',D10[loc],')不同，請檢查!!!')
		print('------------------------------------------------------------------------------------')

	print('+++++++++++++++   8. 檢查是否 Ws < F10 < fx  ++++++++++++++')
	j = 0
	for i in range(0,24):
		if float(Ws[i]) <= float(F10[i]) :
			continue
		else:
			print('------------------------------------------------------------------------------------')	
			print('     !!! 10分鐘風速 Ws',Ws[i],'>= 小時最大平均風F10',F10[i],'at TIME:',times[i],'請檢查!!!')
			print('------------------------------------------------------------------------------------')
			j = j + 1
	if j == 0 :
		print('     o  整點前10分鐘風速值Ws皆小於小時內最大平均風速,檢查通過...')

	j = 0
	for i in range(0,24):
		if float(F10[i]) <= float(fx[i]) :
			continue
		else:
			print('------------------------------------------------------------------------------------')	
			print('     !!! 小時最大平均風F10',F10[i],'>= 小時瞬間最大風fx',fx[i],'at TIME:',times[i],'請檢查!!!')
			print('------------------------------------------------------------------------------------')
			j = j + 1
	if j == 0 :
		print('     o  小時最大平均風F10皆小於小時瞬間最大風,檢查通過...')

main()