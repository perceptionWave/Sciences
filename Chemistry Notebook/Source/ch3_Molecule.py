class molecule:
    
    #def __init__(self):
    #    self

    def splitMolecule(self, molecule):
        self.molecule = molecule
        self.atomArray = []
        z = 0
        for x in molecule:
            z += 1
            if x.isupper():
                lastUpperIndex = z - 1
                self.atomArray.append(x)
            if x.islower():
                yyy = molecule[lastUpperIndex:z]
                self.atomArray.pop()
                self.atomArray.append(yyy)
            if x.isdigit():
                digit = int(x) - 1
                l = len(self.atomArray) - 1
                a = self.atomArray[l]
                for n in range(digit):
                    self.atomArray.append(a)
        return(self.atomArray)
