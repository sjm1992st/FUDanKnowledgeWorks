#coding=utf-8
# import sys, os, io, codecs
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
from synonymSimilarity import SynonymsSimilarity
import copy
class SynonymDictionary(object):
	def __init__(self):
		self.similarityThres = 0.8

	def obtainWordsSet(self,rpath,wpath):
		'''从同义词词林中获取所有词构成的词典'''
		dic = set()
		with open(rpath,encoding='utf-8') as fr:
			for line in fr:
				lineArray = line.strip().split(' ')
				if(len(lineArray)<1):
					continue
				for i in range(1,len(lineArray)):
					dic.add(lineArray[i])

		with open(wpath,'w',encoding='utf-8') as fw:
			for item in dic:
				fw.writelines(item+'\n')

	def loadDict(self,path):
		'''加载词典'''
		dic = set()
		with open(rpath,encoding='utf-8') as fr:
			for line in fr:
				dic.add(line.strip())
		return dic

	def calPairSim(self,dic):
		'''对词典中的词逐对计算相似性'''
		dic = list(dic)
		target_dic = dict()
		synonySim = SynonymsSimilarity()
		for i in range(len(dic)):
			print('i=========:',i)
			tempMap = dict()
			for j in range(i+1,len(dic)):

				item1 = dic[i]
				item2 = dic[j]
				if item1 == item2:
					continue

				# print('item1,item2:',item1,item2)
				sim = synonySim.calcWordsSimilarity(item1,item2)
				print('similairy:',sim)
				if(sim >= self.similarityThres):
					tempMap[item2] = sim
					target_dic[item1] = tempMap
		return target_dic


	def obtainAllSim(self,rpath,wpath):
		dic = self.loadDict(rpath)
		target_dic = self.calPairSim(dic)
		all_dic = copy.deepcopy(target_dic)

		for key ,value in target_dic.items():
			for key2,value2 in value.items():
				if(key2 not in all_dic):
					tempMap = dict()
					tempMap[key] = value2	
					all_dic[key2]= tempMap
				else:
					tempMap = all_dic[key2]
					if(key not in tempMap):
						tempMap[key] = value2

		with open(wpath,'w',encoding='utf-8') as fw:				
			for key ,value in all_dic.items():
				value = sorted(value.items(),key=lambda item:item[1],reverse=True)
				tempStr = ''
				for item in value:
					tempStr += str(item)
					tempStr += '\t'

				fw.writelines(key+'\t'+tempStr+'\n')













if(__name__=='__main__'):
	synonymDictionary = SynonymDictionary()

	'''从同义词词林中获取词典'''
	rpath = r'哈工大信息检索研究中心同义词词林扩展版.txt'
	wpath = r'words_set.txt'
	# synonymsDictionary.obtainWordsSet(rpath,wpath)

	#rpath = r'/search/shijing/synonymSimilarity/cilin/words_set.txt'
	#wpath = r'/search/shijing/synonymSimilarity/cilin/words_similarity.txt'
	synonymDictionary.obtainAllSim(rpath,wpath)
