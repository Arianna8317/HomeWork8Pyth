from abc import ABC, abstractmethod
import math
class AbstractClothes(ABC):
    
    @abstractmethod
    def for_coat(self):
         pass
    
    @abstractmethod
    def for_suit(self):
         pass
        
    def total(self):
         pass
    
    
class Clothes(AbstractClothes):
    
    def __init__(self, size, height):
         self.v = size
         self.h = height
    
    @property
    def for_coat(self):
        return round(self.v / 6.5 + 0.5, 2) 
    
    @property
    def for_suit(self): 
        return  round(self.h * 2 + 0.3)  
    
    @property
    def total(self):
        return self.for_suit + self.for_coat
    
    
cloth_1 = Clothes(52, 1.86)
print(f"Расход ткани на пальто {cloth_1.for_coat}")
print(f"Расход ткани на костюм {cloth_1.for_suit}")
print(f"Общий расход ткани {cloth_1.total}")            
                
