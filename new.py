#-*- coding:utf-8 -*-
import urllib2
import chardet
import json
import re
import time
def write_():
    space = ''
    out_p1="out_concept.txt"
    out_p2="out_entity.txt"
    inp=u"百度分词词库.txt"
    output1 = open(out_p1, 'w')
    output2 = open(out_p2, 'w')
    inp = open(inp, 'r')
    k=0
    for line in inp.readlines():

        temp = line.decode('utf8')
        #print temp
        xx=u"([\u4e00-\u9fa5]+)"
        pattern = re.compile(xx)
        results =  pattern.findall(temp)
        print results[0]
        url1='http://kw.fudan.edu.cn/probaseplus/pbapi?dbname=probase&kw='
        url2='&start=0'
        url1=url1+results[0].encode("UTF-8")+url2

        proxy = urllib2.ProxyHandler({'https': '127.0.0.1:1082'})
        opener = urllib2.build_opener(proxy)
        maxTryNum=10
        for tries in range(maxTryNum):
            try:
                html = opener.open(url1).read()
                break
            except:
                if tries <(maxTryNum-1):
                    continue
                else:
                    print ("Has tried %d times to access url %s, all failed!")
                    break

        if html=="":
            continue
        output1.write(results[0].encode("UTF-8") +" ")
        output2.write(results[0].encode("UTF-8") +" ")
        ##print html.decode(charset).encode('GB18030')
        charset = chardet.detect(html)['encoding']
        print html
        d = json.loads(html)
        print d.keys()
        a=d[d.keys()[2]]
        b=d[d.keys()[3]]
        #print b
        for a_temp in a[0:5]:
            output1.write(a_temp[0].encode("UTF-8") +" ")
        output1.write("\n")
        for b_temp in b[0:5]:
            output2.write(b_temp[0].encode("UTF-8") +" ")
        output2.write("\n")
        time.sleep(3)
    output1.close()
    output2.close()
    inp.close()



write_()
