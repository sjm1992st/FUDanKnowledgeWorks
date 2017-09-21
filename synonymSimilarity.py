#coding=utf-8
# import sys, os, io, codecs
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
import math
class SynonymsSimilarity(object):

	'''计算基于同义词词林的相似性'''
	def __init__(self):
		'''初始化map'''
		self.keyword_identifier_path = r'/search/shijing/synonymSimilarity/dict/keyWord_Identifier_HashMap.txt'
		self.first_KeyWord_Depth_path = r'/search/shijing/synonymSimilarity/dict/first_KeyWord_Depth_HashMap.txt'
		self.second_KeyWord_Depth_path = r'/search/shijing/synonymSimilarity/dict/second_KeyWord_Depth_HashMap.txt'
		self.third_KeyWord_Depth_path = r'/search/shijing/synonymSimilarity/dict/third_KeyWord_Depth_HashMap.txt'
		self.fourth_KeyWord_Depth_path = r'/search/shijing/synonymSimilarity/dict/fourth_KeyWord_Depth_HashMap.txt'
		self.keyword_identifier = self.loadMap2(self.keyword_identifier_path)
		self.first_KeyWord_Depth = self.loadMap1(self.first_KeyWord_Depth_path)
		self.second_KeyWord_Depth = self.loadMap1(self.second_KeyWord_Depth_path)
		self.third_KeyWord_Depth = self.loadMap1(self.third_KeyWord_Depth_path)
		self.fourth_KeyWord_Depth = self.loadMap1(self.fourth_KeyWord_Depth_path)
		

	def loadMap1(self,path):
		'''加载map，形如‘a b’情况的'''
		dic = dict()
		with open(path,encoding='utf-8') as fr:
			for line in fr:
				lineArray = line.strip().split(' ')
				if(len(lineArray)==2):
					dic[lineArray[0]] = lineArray[1]
		return dic

	def loadMap2(self,path):
		'''加载map，形如‘宠辱不惊 Ga09A01= Ee29A01=’情况的'''
		dic = dict()
		with open(path,encoding='utf-8') as fr:
			for line in fr:
				lineArray = line.strip().split(' ')
				if(len(lineArray)>1):
					tempSet = set()
					for i in range(1,len(lineArray)):
						tempSet.add(lineArray[i])
					dic[lineArray[0]] = tempSet
		return dic

	def calcWordsSimilarity(self,word1,words2):
		'''计算两个词间的相似性得分'''
		if(word1 == words2):
			return 1
		if(word1 not in self.keyword_identifier or words2 not in self.keyword_identifier):
			return 0.1
		return self.getMaxSimilarity(self.keyword_identifier[word1],self.keyword_identifier[words2])

	def getMaxSimilarity(self,set1,set2):
		'''计算最大相似性得分'''
		maxSimilarity = 0
		similarity = 0
		for item1 in set1:
			for item2 in set2:
				similarity = self.getIdentifierSimilarity(item1,item2)
				if(similarity>maxSimilarity):
					maxSimilarity = similarity
		return maxSimilarity

	def  getIdentifierSimilarity(self,item1,item2):
		a = 0.65
		b = 0.8
		c = 0.9
		d = 0.96
		if(item1 == item2):
			if(item1[7:]=='='):
				return 1
			else:
				return 0.5
		elif item1[:5] == item2[:5]:
			n = self.fourth_KeyWord_Depth[item1[:5]]
			n = int(n)
			k = int(item1[5:7]) - int(item2[5:7])
			if(k<0):
				k = -k
			return math.cos(n * math.pi / 180) * ((n-k+1)/n)*d
		elif item1[:4] == item2[:4]:
			n = self.third_KeyWord_Depth[item1[:4]]
			n = int(n)
			k = ord(item1[4:5]) - ord(item2[4:5])
			if(k<0):
				k = -k
			return math.cos(n * math.pi / 180) * ((n-k+1)/n)*c
		elif item1[:2] == item2[:2]:
			n = self.second_KeyWord_Depth[item1[:2]]
			n = int(n)
			k = int(item1[2:4]) - int(item2[2:4])
			if(k<0):
				k = -k
			# print('math.cos:',math.cos(n * math.pi / 180))
			
			return math.cos(int(n) * math.pi / 180) * ((n-k+1)/n)*b
		elif item1[:1] == item2[:1]:
			n = self.first_KeyWord_Depth[item1[:1]]
			n = int(n)
			k = ord(item1[1:2]) - ord(item2[1:2])
			if(k<0):
				k = -k
			return math.cos(n * math.pi / 180) * ((n-k+1)/n)*a

		return 0.1







		



if(__name__=='__main__'):
	synonymsSimilarity = SynonymsSimilarity()



	item1 = '中国'
	item2 = '中华'
	sim = synonymsSimilarity.calcWordsSimilarity(item1,item2)
	print(sim)


					

