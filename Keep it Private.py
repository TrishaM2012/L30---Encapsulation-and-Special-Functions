class myclass:
    
    __privateVar = 27;
    
    
    def __priveMeth(self):
        print("I'm inside myclass")
        
    def hello(self):
        print("Private Variable Value:",myclass.__privateVar)
        
foo = myclass()
foo.hello()
foo.__priveMeth
        