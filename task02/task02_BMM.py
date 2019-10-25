# -*- coding: UTF-8 -*-
import jieba

dict = {}
maxLen = 7
minLen = 3
punc = {}

def inputDict():
    file = open('sougodict.txt', 'r', encoding='utf-8')
    while (True):
        line = file.readline()
        if(len(line)==0): break
        term = line.strip()
        dict[term] = 1
    file.close()
    print("词库大小： ",len(dict))

def puncGenesis():
    i = 0
    punclist = ['，', '。', '“', '”', '；', '（', '）', ',', '.', '"', ';', '(', ')', ':', '：', '、', '?', '？', '!', '！']
    while (i<len(punclist)):
        punc[punclist[i]] = 1
        i = i + 1



def sp(sentence):
    res = ""
    temp = ""
    i = len(sentence)
    while (i>0):
        temp = sentence[max(i-maxLen,0):i]
        j = 0
        while(j<len(temp)and((max(i-maxLen,0)>0 and len(temp)>minLen) or max(i-maxLen,0)==0)):
            if temp[j:] in dict:
                res=temp[j:]+"/"+res
                temp = temp[0:j]
                j = 0
            elif j==len(temp)-1:
                if temp[j:] in punc:
                    if(i==len(sentence)): res = temp[j:]+res
                    else: res = temp[j:]+"/"+res
                    temp = temp[0:j]
                    j = 0
                else:
                    res = temp[j:] + "/" + res
                    temp = temp[0:j]
                    j = 0
            else:
                j+=1
        i = max(i-maxLen+len(temp),0)

    return res

def check(res,ans):
    i = 0
    j = 0
    correct = 0
    rescnt = 0
    anscnt = 0
    while ( i<len(res) and j<len(ans) ):
        if (res[i]=='/'and ans[j]=='/'):
            correct+=1
            rescnt+=1
            anscnt+=1
            i+=1
            j+=1
        elif (res[i]=='/'):
            rescnt+=1
            i+=1
        elif (ans[j]=='/'):
            anscnt+=1
            j+=1
        elif(res[i]==ans[j]):
            i+=1
            j+=1
        else:
            i=len(res)
            j=len(ans)
    if (rescnt==0): rescnt = 1
    if (anscnt==0): anscnt = 1
    c = correct/rescnt
    p = correct/anscnt
    f = 2*c*p/(c+p)
    print(correct, rescnt, anscnt)
    print("正确率=",c)
    print('召回率=',p)
    print("F=",f)



def main():
    inputDict()
    puncGenesis()
    sentence = input("待分词句子：\n")
    res = sp(sentence)
    print(res)
    ans = '/'.join(list(jieba.cut(sentence, cut_all=False)))
    print("正确答案： ", ans)
    check(res,ans)


if __name__ == '__main__':
    main()


