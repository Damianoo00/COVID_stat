""" The following order is crucial to avoid circular import and for the proper functioning of the program """


""" Global Instances of classes """


from Vars import Variables

var = Variables()

from Labels import SectionLabel

label = SectionLabel(1, 0, 1, 1)

from Graph import SectionGraph

graph = SectionGraph(0, 0, 1, 3)

from Button import SectionGraphDisplayOption

button = SectionGraphDisplayOption(6, 0, 1, 2)

from Checkbox import SectionCheckbox

checkbox = SectionCheckbox(3, 2, 1, 1)

from List import SectionListOfCountries

list_of = SectionListOfCountries(3, 0, 3, 1)

from File import SectionAddFile

file = SectionAddFile(1, 2, 1, 1)
