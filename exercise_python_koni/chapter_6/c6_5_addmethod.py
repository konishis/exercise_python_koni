class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_Yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_Yugo.exclaim()

#give_me_a_car.need_a_push() #無いのでエラーとなる
give_me_a_Yugo.need_a_push()
