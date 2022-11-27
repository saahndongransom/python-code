def register():
    db=open("database.txt","r")
    username=input("create username")
    password=input("create password")
    password=input("confirm password")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b= b.strip()
        d.append(a)
        f.append(b)
        data =dict(zip(d,f))

    if password != password:
        print("password dont match ,restart")
        register()
    else:
        if len(password)<=6:
            print("password to short,restart")
            register()
        elif username in d:
            print("username exist")
            register()
        else:
            db =open("database.txt","a")
    db.write(username+","+password+"\n")
    print("sucess")

def access():
    db =open("database.txt","r")
    username=input("enter your username")
    password=input("enter password")
    if not len(username or password)<1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("login success")
                        print("hi",username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorrect password or username")
                else:
                    print("username or password doest not exist")

        except:
            print("username or password doest not exist")
        else:
            print("please enter a valid ")
def home(option=None):
    option = input("login|signup:")
    if option== "login":
        access()
    elif option=="signup":
        register()
    else:
        print("enter an option")

home()

