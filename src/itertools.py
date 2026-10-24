
class CountDown():
    def __init__(self,value):
        self.current = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > 0:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration

for i in CountDown(4):
    print(i)