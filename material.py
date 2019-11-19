import os #載入os功能(operating system)

#讀取檔案
materials = []
if os.path.isfile('materials.csv'): #用OS的功能旗下的檢查路徑(path)及檢查檔案(isfile)來確認檔案是否存在
	print('檔案確認無誤') #此行可不寫
#讀取資料(用來將先前資料讀出後再將新資料一起寫入，避免新資料直接蓋掉舊資料造成舊資料不見)	
	with open('materials.csv','r') as f:
		for line in f:
			if '異動類型,儲位,料號,數量' in line:
				continue
			move, location, material, quantity = line.strip().split(',')
			materials.append([move,location, material, quantity])
else:
	print('檔案不存在，將重新產生新的檔案')

#使用者輸入
while True:
	move = input('請輸入異動類型：')
	if move == 'q':
		break

	while True:
		location = input('請輸入儲位：')
		if location == 'q':
			break

		while True:
			material = input('請輸入料號：')
			if material == 'q':
				break
			quantity = input('請輸入數量：')
			quantity = int(quantity)
			materials.append([move,location, material, quantity])

# 印出目前所有資料內容
for m in materials:
	print('異動類型：', m[0], '儲位：', m[1], '料號：', m[2], '數量：', m[3])

#寫入CSV檔
with open('materials.csv', 'w') as f: 
	f.write('異動類型,儲位,料號,數量\n',)
	for m in materials:
		f.write(m[0]+ ','+ m[1]+ ','+ m[2]+ ','+ str(m[3])+ '\n')