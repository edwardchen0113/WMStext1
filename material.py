materials = []
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
		materials.append([location, material, quantity])

for m in materials:
	print('儲位：', m[0], '料號：', m[1], '數量：', m[2])

with open('materials.csv', 'w') as f:
	for m in materials:
		f.write(m[0]+ ','+ m[1]+ ','+ str(m[2])+ '\n')