class Cookie:
    def __init__(self, color) -> None:
        self.color = color 

    def get_color(self):
        return self.color 
    
    def set_color(self, color):
        self.color = color 


cookie_one = Cookie(color='Blue')
cookie_two = Cookie(color='Yellow')

print(f'The color of the cookie one is {cookie_one.get_color()}, and cookie two is {cookie_two.get_color()}')

cookie_two.set_color(color='red')

print(f'The color of the cookie one is {cookie_one.get_color()}, and cookie two is {cookie_two.get_color()}')
