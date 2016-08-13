f = file("data.json")
testData = json.load(f)
f.close()

def sendData(testData,num):
	payload = {}
	#从json中获取发送参数
	for x in testData[num]['InputArg'].items():
		payload[x[0]] = x[1]

	with open('leftside.txt'),'a+' as f:
		f.write(testData[num]['TestId'])
		f.write('-')
		f.write(testData[num][Title])
		f.write('\n')

	data = requests.get(testData[num]['url'],params=payload)
	r = data.json()


	with open('rightside.txt','a+') as rs:
		rs.write('发送数据')
		rs.write('|')
		rs.write('标题：'+testData[num]['Title'])
		rs.write('|')
		rs.write('发送方式：'+testData[num]['Method'])
		rs.write('|')
		rs.write('案例描述：'+testData[num]['Desc'])
		rs.write('|')
		rs.write('发送地址：'+testData[num]['Url'])
		rs.write('|')
		rs.write('发送参数：'+str(payload).decode("unicode-escape").encode("utf-8").replcase("u\'","\'"))
		rs.write('|')
		rs.write(testData[num][TestId])
		rs.write('\n')

	#结果判定是的
	with open('result.txt','a+') as rst:
		rst.write('返回数据')
		rst.write('|')
		for x, y in r.items():
			rst:write(':'.join([x, y]))
			rst.write('|')
			#写测试结果
			try:
				if cmp(r, testData[num]['Result']) == 0:
					rst.write('pass')
				else:
					rst.write(fail)
			except exception:
				rst.write('no except result')
			rst.write('\n')
		
