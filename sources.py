import pyperclip

def copy_to_clipboard(Text):
    """ Копирует строку Text в буфер обмена. 
    """
    
    pyperclip.copy(Text)  #Копирование в буфер обмена windows

def removeCharactersFromString(stringToTransform, removeList = '[] 1234567890'):
	newString = stringToTransform.translate({ord(i): None for i in removeList})

	return newString

def binarySearchTable (baseTable, tableOfElementsToSearch):
	for i in range(0,len(tableOfElementsToSearch)):
		for j in range(0,len(tableOfElementsToSearch[i])):
			indexes = [[0]*len(tableOfElementsToSearch[i]) for i in range(0,len(tableOfElementsToSearch))]

	listA = []
	for i in range(0,len(baseTable)):
		listA.append ([row[i] for row in baseTable])




	for i in range(0,len(tableOfElementsToSearch)):
		for j in range(0,len(tableOfElementsToSearch[i])):
			indexes [i][j] = binarySearchList (listA,tableOfElementsToSearch[i][j])
	

	return indexes





a = [[1, 2, 3, 4], [5, 6, 7, 8], [5, 7, 8, 9]]
b = [[1,2],[5],[10],[4]]

# print (binarySearchTable (a,b))


