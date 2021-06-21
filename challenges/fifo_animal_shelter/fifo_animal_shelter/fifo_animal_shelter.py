class  AnimalShelter:
    def __init__(self):
        self.rearcat=None
        self.frontcat=None
        self.reardog=None
        self.frontdog=None



    def enqueue(self,animal):

        if animal.type=="cat":
    
            if self.frontcat ==None:
                self.frontcat=animal
                self.rearcat=animal
            else:
                self.rearcat.next=animal
                self.rearcat=animal

        if animal.type=="dog":
            
            if self.frontdog ==None:
                self.frontdog=animal
                self.reardog=animal
            else:
                self.reardog.next=animal   
                self.reardog=animal



    def dequeue(self,pref):

        if pref == "cat" and self.frontcat != None :
            temp=self.frontcat
            self.frontcat=temp.next
            temp.next=None
            return temp.name

        elif pref == "dog" and self.frontdog != None :
            temp=self.frontdog
            self.frontdog=temp.next
            temp.next=None
            return temp.name 
        else:
            return 'null'       





class Cat():
    def __init__(self,name):
        self.name=name
        self.type='cat'
        self.next= None



class Dog():
    def __init__(self,name):
        self.name=name
        self.type='dog'
        self.next= None








