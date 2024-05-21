class Bird():
    def fly(self):
        return "flies high"

class Penguin(Bird):
    def fly(self):
        return "Cannot fly"

def fly_test(bird):
    print(bird.fly())

b=Bird()
fly_test(b)

e=Penguin()
fly_test(e)