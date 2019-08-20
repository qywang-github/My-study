import csv
import random

def writeToCSV(fileName, list):
	with open(fileName, 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerows(list)

def getLables(edges):
	Lables = []
	for edge in edges:
		if edge[0] not in Lables:
			Lables.append(edge[0])
		if edge[1] not in Lables:
			Lables.append(edge[1])
	return Lables

if __name__=='__main__':
	file_1 = "trade_1.csv"
	file_3 = "transcircle.csv"
	file_2 = "prj9.exb13_circle_rela.csv"
	
	commid_list = []
	for i in range(1,10001):
		commid_list.append(i)
	
	count = 0 
	for CommId in commid_list:
		col = 330
		TRADETYPE = 'jiankong'
		MthTRADEAmtSUM = 100000.0
		DataDATE = '2018-06-30'
		
		edges = []
		temp = []
		for i in range(0, col):
			edge = []
			edge.append(random.randint(1+count, 1+count))
			edge.append(str(i+2+count))
			edge.append(TRADETYPE)
			edge.append(DataDATE)
			edge.append(round(random.uniform(0, MthTRADEAmtSUM), 4))
			edges.append(edge)
		
		for i in range(0, col):
			edge = []
			edge.append(random.randint(2+count, 2+count))
			edge.append(str(i+331+count))
			edge.append(TRADETYPE)
			edge.append(DataDATE)
			edge.append(round(random.uniform(0, MthTRADEAmtSUM), 4))
			edges.append(edge)
			
		for i in range(0, col):
			edge = []
			edge.append(random.randint(3+count, 3+count))
			edge.append(str(i+665+count))
			edge.append(TRADETYPE)
			edge.append(DataDATE)
			edge.append(round(random.uniform(0, MthTRADEAmtSUM), 4))
			edges.append(edge)	
		writeToCSV(file_1, edges)
		
		#交易圈编号
		circle_edges = []
		Lables = getLables(edges)
		for lable in Lables:
			edge = []
			edge.append(lable)
			edge.append(CommId)
			edge.append(DATADATE)
			edge.append('jiankong')
			circle_edges.append(edge)
		writeToCSV(file_2, circle_edges)
		
		#优质客户表
		edge = []
		edge.append(str((CommId-1)*1000+1))
		edge.append(CommId)
		edge.append(DATADATE)
		edge.append('jiankong')
		temp.append(edge)
		writeToCSV(file_3, temp)
		count = count+1000

