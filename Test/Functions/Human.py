class Human:
    def __init__(self, sex, age, name):
        self.Sex = sex
        self.Age = age
        self.Name = name
    def GetSex(self):
        return self.Sex

    def GetAge(self):
        return self.Age

    def GetName(self):
        return self.Name

    def SetSex(self, sex):
        self.Sex = sex

    def SetAge(self, age):
        self.Age = age
        
    def SetName(self, name):
        self.Name = name
