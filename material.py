materials = []
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

for m in materials:
	print('異動類型：', m[0], '儲位：', m[1], '料號：', m[2], '數量：', m[3])

with open('materials.csv', 'w') as f: #encoding = 'utf-8'世界語言通用編碼，防止寫成CSV檔時出現亂碼。
	f.write('異動類型,儲位,料號,數量\n',)
	for m in materials:
		f.write(m[0]+ ','+ m[1]+ ','+ m[2]+ ','+ str(m[3])+ '\n')