#coding=utf8
import re
import os
from tqdm import tqdm
import random
# path='corpus/1_产品使用说明文档/'
# path='corpus/2_产品制作工艺流程/'
# path='corpus/3_产品原材料需求文档/'
# path='corpus/4_产品外观外形设计文档/'
# path='corpus/5_产品相关专利文档/'
path='corpus/6_产品工艺设计/'

new_path=path[:-1][7:]+'_clean'
print new_path
try:
    os.mkdir(new_path)
except:
    pass

files=os.listdir(path)
# random.shuffle(files)
# files=files[:40]
# files=['pdf-1-106-conv.txt']
# files=['pdf-4-4-conv.txt']
print files

def filter_file(cont):
    print cont

def split(cont):
    final_list=[]
    result=re.split('\r|\n|\r\n',cont)
    for one in result:
        one_clean=one.strip()
        if len(one_clean)>30:
            final_list.append(one_clean)
    return final_list

def clear_para(para):
    para=re.sub('\s+',' ',para)#去掉多余的空格，多个转一个
    para=para.replace('　',' ')
    para=para.replace('［','[').replace('］',']')
    len_para=len(para)
    '''去掉目录页码那种东西'''
    if '.' in para:
        max_dot_length=max(len(i) for i in re.findall('\.+',para))
        if max_dot_length>10:
            # print para
            return None

    '''去掉全是英文和数字的'''
    max_number_length=len(re.findall('\d',para))
    if max_number_length>0.8*len_para:
        # print para
        return None
    max_eng_length=len(re.findall('[a-zA-Z]',para))
    if max_eng_length>0.8*len_para:
        # print para
        return None
    if max_eng_length>len(para.replace(' ','').replace('　',''))*0.9:
        return None

    '''几乎没有中文的'''
    num_chiese=len(re.findall(u'[\u4e00-\u9fa5]'.encode('utf8'),para))
    if num_chiese<10:
        # print para,'hhhh'
        return None

    '''参考文献'''
    if re.findall('^\[[1-9]\d*\].*',para):
        # print para
        return None

    '''中文中的空格'''
    if len(re.findall(u' [\u4e00-\u9fa5]'.encode('utf8'),para))>6:
        # print para
        # print 'ssss'
        # print '*******************************************************'
        para=para.replace(' ','')

    return para
    pass


for file in tqdm(files):
    print '\n\n\n'
    print file
    cont=open(path+file).read()
    cont=split(cont)
    final_cont=''
    for para in cont:
        para_clear=clear_para(para)
        if para_clear!=None:
            final_cont+='\n'
            final_cont+=para
            # print para_clear
            # print '*******************************************************'
    # open(new_path+'/clean_'+file,'w').write(final_cont)

    # print final_cont




