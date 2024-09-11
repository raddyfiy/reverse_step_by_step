import sys
code=input("请输入注册码：\n")

targetlist1=[2,6,3,117,64,20,20,27,72,7,97,111,75,79,64,61,109,111,97,107,3,125,65,75,75,111,101,119,23,101,65]
targetlist2=[0, 0, 0, 0, 0, 0, 0, 0, 11, 0, -25, 0, -30, 0, 47, 0, 0, 0, 0, 0, 17, 0, 0, -48, 0, 0, 0, 0, 0, 30, 0, 0, 36, 0, 0, -17, 12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def check_serial(serial):
    flagnumberList=[]
    calclist=[]
    if len(serial)!=32:
        return False
    for i in serial:
        flagnumberList.append(ord(i))
    #--------------check1, must in A-Z a-z
    for i in flagnumberList:
        if i<65 or i>122:
            return False
        elif i>90 and i<97:
            return False
    #---CHECK 2
    for index in range(len(flagnumberList)-1):
        if flagnumberList[index]%2==0:
            calclist.append(flagnumberList[index]^flagnumberList[index+1])
        elif flagnumberList[index]%2==1 and index%2==0:
            calclist.append((flagnumberList[index]&flagnumberList[index+1]))
        else:
            calclist.append((flagnumberList[index]&flagnumberList[index-1]|flagnumberList[index+1]))
    if targetlist1!=calclist:
        return False
    #---CHECK 3
    for index in range(len(flagnumberList)-8):
        if index%2==0:
            calcindex=flagnumberList[index]+flagnumberList[index+2]-180
        elif index%2==1:
            calcvalue=flagnumberList[index]+flagnumberList[index+2]-180
            if calcindex>=0 and targetlist2[calcindex]!=calcvalue:
                return False

    #check 4
    if flagnumberList[31]!=ord("Q"):
        return False
    if flagnumberList[28]!=ord("r"):
        return False
    #check5
    total=0
    for i in range(32):
        total+=flagnumberList[i]
    if total!=3096:
        return False

    return True

if check_serial(code):
    print ("感谢注册！")
    print("flag: flag{"+code+"}")
else:
    print ("你tm买个注册码吧！")