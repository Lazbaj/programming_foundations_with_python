class Parent():
    """docstring for Parent"""

    def __init__(self, last_name, eye_color):
        print ('Parent Constructor Called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ('Last name: ' + self.last_name)
        print ('Eye color: ' + self.eye_color)

class Child(Parent):
    """docstring for Child"""

    def __init__(self, last_name, eye_color, number_of_toys):
        print ('Child Constructor Called')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        Parent.show_info(self)
        print ('Number of toys: ' + self.number_of_toys)



# mad_max = Parent('Mad', 'blue')
# print mad_max.show_info()

mad_tom = Child('Mad', 'blue', '5')
mad_tom.show_info()
