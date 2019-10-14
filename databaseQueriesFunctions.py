
import sqlite3

my_database = 'drugs_list.db'

#SQL Queries:

groupNameColumnSQL = "SELECT DISTINCT groupName FROM drug_group ORDER BY groupName"
dosageFormColumnSQL = "SELECT DISTINCT dosageForm FROM drugs_full_list ORDER BY dosageForm"
dosageColumnSQL = "SELECT DISTINCT dosage FROM drugs_full_list WHERE dosage IS NOT NULL ORDER BY dosage"
latinNameColumnSQL = "SELECT DISTINCT latinName FROM drugs_full_list WHERE latinName IS NOT NULL ORDER BY latinName"
brandNameColumnSQL = "SELECT DISTINCT brandName FROM drugs_full_list WHERE brandName IS NOT NULL ORDER BY brandName"
doseColumnSQL = "SELECT DISTINCT doseVar FROM dose_table WHERE doseVar IS NOT NULL ORDER BY doseVar"
regularityColumnSQL = "SELECT DISTINCT regularity FROM regularity_table WHERE regularity IS NOT NULL ORDER BY id"
courseDuratinColumnSQL = "SELECT DISTINCT courseDuration FROM course_duration_table WHERE courseDuration IS NOT NULL ORDER BY id"








def databaseFullColumnImport(columnName:list):
    ''' Берет из таблицы "tableName" весь столбец "columnName" базы данных databaseName
        сортирует по алфавиту
        переводит его в массив элементов
    '''
    if columnName == 'groupName':
        querSQL = groupNameColumnSQL
    elif columnName == 'dosageForm':
        querSQL = dosageFormColumnSQL
    elif columnName == 'dosage':
        querSQL = dosageColumnSQL
    elif columnName == 'latinName':
        querSQL = latinNameColumnSQL
    elif columnName == 'brandName':
        querSQL = brandNameColumnSQL
    elif columnName == 'dose':
        querSQL = doseColumnSQL
    elif columnName == 'regularity':
        querSQL = regularityColumnSQL
    elif columnName == 'courseDuration':
        querSQL = courseDuratinColumnSQL


    currentColumn = []
  
    conn = sqlite3.connect(my_database)

    with conn:
        cur = conn.cursor()

        cur.execute(querSQL)    
        column = cur.fetchall()

        for i in column:
            currentColumn.append (i[0])
    conn.close()

    return currentColumn    
"""
                -   -   --  -   -   --  -   -   --  -   

"""

def databaseSelection (nameOfColumn, nameToSelection):


    if nameOfColumn == 'dosageForm':
        querSQL = "SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                AND drugs_full_list.dosageForm = '" + str(nameToSelection + "'")
    elif nameOfColumn == 'dosage':
        querSQL = "SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                AND drugs_full_list.dosage = '" + str(nameToSelection + "'")
    elif nameOfColumn == 'latinName':
        querSQL = "SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                AND drugs_full_list.latinName = '" + str(nameToSelection + "'")
    elif nameOfColumn == 'brandName':
        querSQL = "SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                AND drugs_full_list.brandName = '" + str(nameToSelection + "'")
    elif nameOfColumn == 'groupName':
        querSQL = "SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                AND drug_group.groupName = '" + str(nameToSelection + "'")

    conn = sqlite3.connect(my_database)

    with conn:
        cur = conn.cursor()

        cur.execute(querSQL)   
        myTable = cur.fetchall()

       
    return myTable    

"""
                -   -   --  -   -   --  -   -   --  -   

"""


sqlVariablesDosageForm, sqlVariablesDosage, sqlVariablesLatinName, sqlVariablesBrandName, sqlVariablesGroupName = '','','','',''


def setSqlVariablesToEmpty ():
    
    global sqlVariablesDosageForm, sqlVariablesDosage, sqlVariablesLatinName, sqlVariablesBrandName, sqlVariablesGroupName
    sqlVariablesDosageForm, sqlVariablesDosage, sqlVariablesLatinName, sqlVariablesBrandName, sqlVariablesGroupName = '','','','','' 



def databaseCompositeSelection (nameOfColumn, nameToSelection):

    global sqlVariablesDosageForm, sqlVariablesDosage, sqlVariablesLatinName, sqlVariablesBrandName, sqlVariablesGroupName

    if (nameOfColumn == 'dosageForm') and (sqlVariablesDosageForm == ''):
        sqlVariablesDosageForm = f"AND drugs_full_list.dosageForm = '{str(nameToSelection)}'"
    elif (nameOfColumn == 'dosage') and (sqlVariablesDosage == ''):
        sqlVariablesDosage = f"AND drugs_full_list.dosage = '{str(nameToSelection)}'"
    elif (nameOfColumn == 'latinName') and (sqlVariablesLatinName == ''):
        sqlVariablesLatinName = f"AND drugs_full_list.latinName = '{str(nameToSelection)}'"
    elif (nameOfColumn == 'brandName') and (sqlVariablesBrandName == ''):
        sqlVariablesBrandName =f"AND drugs_full_list.brandName = '{str(nameToSelection)}'"
    elif (nameOfColumn == 'groupName') and (sqlVariablesGroupName == ''):
        sqlVariablesGroupName = f"AND drug_group.groupName = '{str(nameToSelection)}'"

    querSQL = f"SELECT drugs_full_list.*, drug_group.groupName \
            FROM group_latin, drugs_full_list, drug_group \
            WHERE drugs_full_list.latinName = group_latin.latinName \
                AND drug_group.groupName = group_latin.groupName \
                {sqlVariablesDosageForm} {sqlVariablesDosage} {sqlVariablesLatinName} {sqlVariablesBrandName} {sqlVariablesGroupName}"

    # print (sqlVariablesDosageForm, sqlVariablesDosage, sqlVariablesLatinName, sqlVariablesBrandName, sqlVariablesGroupName, sep = ' *** ')

    conn = sqlite3.connect(my_database)

    with conn:
        cur = conn.cursor()

        cur.execute(querSQL)   
        myTable = cur.fetchall()

       
    return myTable

# print (databaseCompositeSelection('dosage', '5'))
