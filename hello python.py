print('*'*10,"欢迎进入狗狗年龄对比系统",'*'*10)
while True:
    try:
        age=int(input("请输入狗的年龄:"))
        print("")
        if age<=0:
            print("豆")
            break
        elif age==1:
            print("相当于人的10岁")
            break
        elif age==2:
            print("相当于人的20岁")
            break

        else:
            human=age*10+2
            print("相当于人类的%s岁"%human)
            break
    except ValueError:
        print("输入不合法，请重新输入")
input("按enter键退出")
