class PersonInfo:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.atk = 10
        self.dif = 5
        self.sword = 0
        self.shield = 0
        self.hands = False
        print("Info ok")
        print(self.name)
    def a_test(self):
        print(str(self.name)+"nice")
class Person_Set:
    def __init__(self,name):
        self.personInfo = PersonInfo(name)
    def set_normal_sword(self):
        self.personInfo.sword = 5
    def set_rare_sword(self):
        self.personInfo.sword = 10
    def set_epic_sword(self):
        self.personInfo.sword = 20
    def set_legend_sword(self):
        self.personInfo.sword = 50
    def set_heavy_sword(self):
        self.personInfo.sword = 100
        self.personInfo.shield = 0
        self.personInfo.hands = True
    def set_shield(self):
        if self.personInfo.hands == False:
            self.personInfo.shield = 50
        else:
            self.personInfo.shield = 50
            self.personInfo.sword = 0
            self.personInfo.hands = False
    def show_Info(self):
        print("name："+str(self.personInfo.name))
        print("血量："+str(self.personInfo.hp))
        print("攻擊力："+str(self.personInfo.atk+self.personInfo.sword))
        print("防禦力："+str(self.personInfo.dif+self.personInfo.shield))
a = Person_Set("阿蛙")
#a.show_Info()
#a.set_legend_sword()
a.personInfo.a_test()
#a.show_Info()