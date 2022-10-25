class Matrix:
    def __init__(self, *args):
        self.matrix = list(args)
        
    def __str__(self):
        res = '\n'.join(map(str,self.matrix))
        res = res.replace(",","").replace("[","").replace("]","")        
        return res
    def __add__(self, other):
        sum_1 = []
        sum_2 = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_2.append(self.matrix[i][j] + other.matrix[i][j])
            sum_1.append(sum_2)
            print(sum_2)
            sum_2 = []
        return Matrix('\n'.join(map(str, sum_2)))
 
 
mat_1 = Matrix([2,3,4],[3,5,8],[1,0,2])  
print(mat_1)
print()
mat_2 = Matrix([12,-3,5],[23,-5,-1],[3,2,2])  
print(mat_2)
print()
print("Сумма матриц")
print(f"{mat_1 + mat_2}")           
#mat_3 = mat_1 + mat_2
#print(mat_3)