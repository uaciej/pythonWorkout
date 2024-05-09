'''
In this exercise, we’re going to see a small-scale version of that. In the previous
exercise, we created a Scoop class that represents one scoop of ice cream. If we’re
really going to model the real world, though, we should have another object into
which we can put the scoops. I thus want you to create a Bowl class, representing a
bowl into which we can put our ice cream
The result of running print(b) should be to display the three ice cream flavors in our
bowl
'''
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self) -> None:
        self.scoops = []

    def add_scoop(self, *flavors):
        for flavor in flavors:
            self.scoops.append(Scoop(flavor))
        
    def __str__(self) -> str:
        return('\n'.join(s.flavor for s in self.scoops))
    

if __name__ == "__main__":
    b = Bowl()
    b.add_scoop('mayonnaise', 'bleach', 'mud')
    b.add_scoop('poop')
    print(b)
