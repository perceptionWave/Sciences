# Look up terms in glossary
def define(term):
    for x in glossary:
        if term == glossary[x]:
            print(glossary[x])
        else:
            print("Term could not be found")

# Add glossary of terms. 
glossary = {
    "atom": "atom is the definition"
}

define("atom")
# Does not work