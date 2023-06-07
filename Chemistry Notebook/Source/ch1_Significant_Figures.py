## Significant_Figures

class sig_Figs:
    
    def __init__(self, array):
        
        self
        self.array = str(array)
    
    def sigFigs(self, n, sigFig):
        return(intround(n, sigFig))

sigFig = 0
count = 0

n = 1.2330
m = 0.0345
o = 3400
p = 10.0030
#array method: multiple entries
arrayE = list([m, n, o, p])

for x in arrayE:
    if type(x) is int:
        x = str(x)
        x[::-1]
        for y in x:
            count += 1
            if y > 0: 
                i = x.index(y)
                
                
    if type(x) is float:
        x = str(x)
        for y in x:
            count += 1
            # if y > 0:


# method: define a single numbers length of sig figs
# method:   find lowest sig figs
#           multiple entries 

#print(len(n))



    
