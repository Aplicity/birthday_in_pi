
## 找出你出生日期的数字在圆周率的哪个位置
from mpmath import mp

mp.dps = 1000000
Pi=list(str(mp.pi))
n=len(Pi)
birth = input('输入你的生日(格式为yymmdd，比如98年1月1日的输入为‘980101’):')
s=list(birth)
if len(s) !=6:
    print('sorry,你的输入有误，请重新运行程序')
index=[]
for i in range(n-6):
    if Pi[i:i+6]==s:
        print('你的生日的生日在圆周率pi中的第 %i 到第 %i 位'%(i+1,i+2))
        index.append(i)
if len(index)==0 and len(s)==6:
    print('抱歉,请提高pi的精度')
