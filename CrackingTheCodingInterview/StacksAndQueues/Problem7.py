'''
Created on Jun 28, 2015

@author: Debanjan Mahata
'''


class Queue:
    def __init__(self):
        self.__storage = []
        
    def isEmpty(self):
        return self.__storage == []
    
    def enqueue(self, val):
        self.__storage.insert(0, val)
        
    def dequeue(self):
        return self.__storage.pop()
    
    def peek(self):
        return self.__storage[-1]

class Animal:
    
    def __init__(self):
        self.order = 0
        self.name = None
        
    def set_order(self, order):
        self.order = order
        
    def get_order(self):
        return self.order
    
    def is_older_than(self,animal):
        return self.order < animal.order


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
#        super(Dog,self).__init__()
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
#        super(Cat,self).__init__()


class AnimalQueue:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.order = 0
        
        
    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.order += 1
            animal.set_order(self.order)
            self.dog_queue.enqueue(animal)
            
            
        if isinstance(animal, Cat):
            self.order += 1
            animal.set_order(self.order)
            self.cat_queue.enqueue(animal)
            
            
    def dequeueAny(self):
        if self.dog_queue.isEmpty() and self.cat_queue.isEmpty():
            return "Both queue are empty, therefor dequeue operation not possible"
        
        if self.dog_queue.isEmpty() and self.cat_queue.isEmpty() == False:
            return self.cat_queue.dequeue()
        
        if self.cat_queue.isEmpty() and self.dog_queue.isEmpty() == False:
            return self.dog_queue.dequeue()
        
        
        dog = self.dog_queue.peek()
        cat = self.cat_queue.peek()
        
        if dog.is_older_than(cat):
            return self.dog_queue.dequeue()
        else:
            return self.cat_queue.dequeue()
        
        
if __name__ == "__main__":
    
    cat1 = Cat()
    cat1.name = "cat1"
    cat2 = Cat()
    cat2.name = "cat2"
    cat3 = Cat()
    cat3.name = "cat3"
    
    dog1 = Dog()
    dog1.name = "dog1"
    dog2 = Dog()
    dog2.name = "dog2"
    dog3 = Dog()
    dog3.name = "dog3"
    
    aq = AnimalQueue()
    
    aq.enqueue(cat1)
    aq.enqueue(dog1)
        
    aq.enqueue(cat2)
    aq.enqueue(dog2)
        
    aq.enqueue(cat3)
    aq.enqueue(dog3)
    
    print aq.dequeueAny().name
    print aq.dequeueAny().name