from abc import ABC, abstractmethod
import math
# class AbstractClothes(ABC):
#     @abstractmethod
#     def for_coat(self):
#         pass
    
#     def for_suit(self):
#         pass
    
#     def total(self):
#         pass
    
# class Clothes(AbstractClothes):
#     def __init__(self, size, height):
#         self.size = size
#         self.height = height
#         self.coat = size / 6.5 + 0.5
#         self.suit = height * 2 + 0.3
   
class AbstractClothes(ABC):
    
    def __init__(self, param):
        self.param = int(param)
         
    @abstractmethod
    def consumption(self):
        pass
    
class Coat(AbstractClothes):

    @property
    def consumption(self):      
        return round(self.param / 6.5 + 0.5, 2)
    
    
class Suit(AbstractClothes):
    
    @property    
    def consumption(self):
        return round(self.param * 0.02 + 0.3, 2)
          
coat_1 = Coat(58)
print(f"Расход ткани на пальто {coat_1.consumption}")
suit_1 = Suit(186)
print(f"Расход ткани на костюм {suit_1.consumption}")
print(f"Общий расход ткани {suit_1.consumption + coat_1.consumption}")            
            