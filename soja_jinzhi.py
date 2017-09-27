#coding:utf-8
#build by LandGrey
#2016-03-12

import sys

#常用的字母代表数字的字典
dic={'10':'A',
     '11':'B',
     '12':'C',
     '13':'D',
     '14':'E',
     '15':'F'}

#将weight进制的某一位的值对应的十进制的值算出来
def PlaceValue(nvalue,scale,digits):
    Quan=1                            #某一位的权值,初始为1
    for i in range(1,digits+1):
        Quan=scale*Quan
    return nvalue*Quan

#scale进制的值value转为对应10进制的值
def N_2_decimal(value,scale):
    sum=0
    n=len(str(value))     #数值的位数长度
    for i in range(1,n+1):
        sum=sum+PlaceValue(int(str(value)[i-1]),scale,n-i)
    return sum

#10进制的值value转为对应scale进制的值
def decimal_2_N(value,scale):
    arr=[]
    i=0
    while value is not 0:
        rem=value%scale
        if rem>=16:
            rem="*"+str(rem)+"*"
        if rem<=15 and rem>=10:
            rem=dic[str(rem)]
        value=value/scale
        arr.append(rem)
        i+=1
    return arr

def anyscale(scale1,value,scale2):
    midvalue=N_2_decimal(value,scale1)
    finvalue=decimal_2_N(midvalue,scale2)
    return finvalue

try:
    variate1=str(sys.argv[1])
    variate2=str(sys.argv[2])
    variate3=str(sys.argv[3])
    if variate1.isdigit() and variate2.isdigit() and\
       variate3.isdigit() and int(variate1)>1 and int(variate3)>1:
        print("输对了呢,输入是数字 \n")
        for item in str(sys.argv[2]):
            if int(item)>=int(str(sys.argv[1])):
                print("别闹,"+str(sys.argv[1])+" 进制怎么可能有 "+str(item)+" ?")
                sys.exit()
        if N_2_decimal(int(variate2),int(variate1))>999999999:
            print("数字太大 电脑君不想工作了......")
            sys.exit()
    else:
        print("别闹,输入的不太对啊 ")
        sys.exit()

    try:
        value=anyscale(int(variate1),int(variate2),int(variate3))
        value.reverse()
        rev_value="".join(str(i) for i in value)
    except:
        print("运算出错了呢 先溜为上.....")
        sys.exit()
    print(str(variate1)+" 进制的 "+str(variate2)+" 转成 "+str(variate3)+" 进制的数为 "+rev_value)
except:
    print("貌似已怀孕......  ")
    print("轻轻的，我走了  ")
    sys.exit()

