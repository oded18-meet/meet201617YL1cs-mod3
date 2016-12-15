class Student :
'''
A class made for writing interetaction summary
'''

    def __init__(self, name, hometwon, age , height, fav_ice_cream_flavor):
    
        self.name = name
        self.hometwon = hometwon
        self.age = age
        self.height = height
        self.fav_ice_cream_flavor = fav_ice_cream_flavor

    def print_summary(self):
        print('hey, my name is'+ self.name + 'I live in'+
              self.hometwon + "and I'm" + str(self.age) + " I'm about" +
              str(self.height) + 'meters tall' + 'and my favorite ice cream flavor is' +
              self.fav_ice_cream_flavor + '.')




