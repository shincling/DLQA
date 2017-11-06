#coding=utf8
import re
import jieba
import jieba.posseg as pseg
import jieba.analyse

def tf_idf(keyword,line,passage):
    '''这里留下了一个隐患，具体就是计算idf的时候，是否要把目标行去掉
    这个函数的输入是：
    keywork:一个词
    line:目标句子，
    passage:句子所在的document,是Line的集合
    用来计算一个词在一个已知文档里的一个具体句子的tf-idf值'''

    keyword=keyword.encode('utf8')
    # passage=''.join([each for each in passage])
    passage=''.join([each for each in passage if each!=line])#找到除了当前句子以外的其他所有句子

    # tf=len(re.findall(keyword,line)) #这两个是选择tf到底是作为一个开关而是频率有用．
    tf=1 if (re.findall(keyword,line)) else 0
    if keyword=='时间' or  keyword=='时候':
        # tf+=len(re.findall('[年月日时分秒]',line))
        if re.findall('[年月日时分秒]',line):
            tf=0.5

    if keyword=='地方' or  keyword=='地点':
        # tf+=len(re.findall('[省市县国村镇乡区]',line))
        if (re.findall('[省市县国村镇乡区]',line)):
            tf=0.8
    # if keyword=='名字' or '名' in keyword:
    #     postag=jieba.posseg.cut(line)
    #     postag=[i.flag for i in postag]
    #     if ('nr' in postag or 'ns' in postag or 'nt' in postag or 'nz' in postag):
    #         tf=0.2
    df=len(re.findall(keyword,passage))
    idf=1.0/((df+1)**3)
    # print tf,idf
    return tf*idf

def rela_extend(line):
    postag=jieba.posseg.cut(line)
    words=[]
    postags=[]
    for i in postag:
        word=i.word
        words.append(word)
        postags.append(i.flag)
        print word,
    print '\n',postags

question='世界上第一流的LED制造商是哪家？'
rela_extend(question)


