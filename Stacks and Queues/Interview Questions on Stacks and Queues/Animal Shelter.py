class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0)

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeueAny(self):
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        return self.cats.pop(0)


q = AnimalShelter()
q.enqueue('cat1', 'cat')
q.enqueue('cat2', 'cat')
q.enqueue('dog1', 'dog')
q.enqueue('cat3', 'cat')
q.enqueue('dog2', 'dog')
print(q.dequeueCat())
print(q.dequeueDog())
print(q.dequeueAny())
