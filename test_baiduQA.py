#coding=utf8
import re
import gzip
cc=gzip.open('/media/shin/新加卷1/DeepLearning/数据集/WebQA.v1.0/data/test.ann.json.gz','r').read()
print len(cc)

ccc=cc.split('{"q_key')[1:]

for cc in ccc:
    print '\n\n'
    sent=re.findall('evidence_tokens": \[(.*?)\],',cc)[0].split(',')
    q=re.findall('question_tokens": \[(.*?)\],',cc)[0].split(',')
    a=re.findall('answers": \[(.*?)\],',cc)[0].split(',')

    print 'Sent: ',
    for i in sent:
        print i.strip()[1:-1].encode("utf-8").decode('unicode_escape'),
    print '\nQuestion: ',
    for i in q:
        print i.strip()[1:-1].encode("utf-8").decode('unicode_escape'),
    print '\nAnswer: ',
    for i in a:
        print i.strip()[1:-1].encode("utf-8").decode('unicode_escape'),


