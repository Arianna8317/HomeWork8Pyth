class Cell:
    
    def __init__(self, quantity):
         self.quantity = int(quantity)
         
    def __add__(self, other):
        return f"Сумма клеток равна {str(self.quantity + other.quantity)}"    
     
    def __sub__(self, other):
        delta = self.quantity - other.quantity
        if delta > 0:
            return f"Разность клеток равна {delta}" 
        else:
            return f"Невозможно совершить операцию вычитания"  
        
    def __mul__(self, other):
        return f"Произведение клеток равнo {str(self.quantity * other.quantity)}"
      
    def __truediv__(self, other):
        return f"Деление клеток равно {str(self.quantity // other.quantity)}" 
    
    def make_order(self, cells_in_row):
        row = ""
        for i in range(int(self.quantity // cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * int(self.quantity % cells_in_row)}\\n'    
        return row      
 
 
print("Создаем клетки")    
cell_1 = Cell(34)
cell_2 = Cell(64)
cell_3 = Cell(126) 
print(cell_2 + cell_3) 
print(cell_3 - cell_2)
print(cell_3 * cell_2) 
print(cell_3 / cell_1)         
print("Организуем клетки в ряды")
print(cell_2.make_order(20)) 
print(cell_1.make_order(12))      
        
         
         
              