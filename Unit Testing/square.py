class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be a number!')
            
        if length <= 0:
            raise ValueError('Length must be greater than 0!')
        
        self.length = length

    def area(self):
        return self.length * self.length