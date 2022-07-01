class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name =name
        self.age = age
        self.tracks = tracks
        self.score = score
        pass
    def change_name(self, name):
        self.name = name
        print(name)
    def change_age(self, age):
        self.age = age
        print(age)
    def add_track(self, tracks):
        self.tracks.insert(2,tracks) 
        print(tracks)
    def get_score(self, score):
    # Please how do I make sure my funtion can accept empty agruement and allocate a null vaule
    # def get_score(self, score):    
        if score is None:
            self.score = 0
            return score
        self.score = score
        print(self.score)
        
    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# print(Bob.name)
# frank = Bob.tracks
# print(frank)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score('')
