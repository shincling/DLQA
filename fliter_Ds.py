#coding=utf8
import re
from tqdm import tqdm
file=open('baike.txt').read()
file_fliter=open('file_aim_total','w')
cc=re.split('\d*?<->',file)
cc=cc[1:]
# cc=cc[:10]
idx_list=[]
for idx,one in tqdm(enumerate(cc)):
    bb=''
    one=one.strip()
    if '\t\t\t\t' in one[:50]:
        name=re.findall('(.*?)\t\t\t\t',one)[0]
    elif '-' in one[:50]:
        name=re.findall('(.*?)-',one)[0]
        name=name.strip()
    elif ' ' in one[10:50]:
        name=re.findall('(.*?) ',one)[0]
    else:
        name=one[:50]

    # print name
    # print re.findall('仪|器|系统|表|电|泵|阀|机|车|波导|试',name)
    if re.findall('仪|器|系统|表|电|泵|阀|机|车|波导|试',name):
        idx_list.append(idx)
        bb+=name
        bb+='\n'
        bb+=one
        bb+='\n\n\n\n'
        file_fliter.write(bb)

