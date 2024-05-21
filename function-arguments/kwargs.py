

def Student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

Student(name="hari",age=12,email="haru@gmail.com",city="ktm")