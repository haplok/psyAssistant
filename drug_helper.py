
from PyQt5 import QtCore, QtGui, QtWidgets

import databaseQueriesFunctions as dbFunc
import sources



"""
                -   -   -   -   --  -   --  -   -   -   -
"""

class Ui_MainWindow(object):
    groupNamesButton = []
    dosageFormButton = []
    dosageButton = []
    latinNameButton = []
    brandNameButton = []
    doseButton = []
    regularityButton = []
    courseDurationButton = []

    global doseRegularityCourseDurtion
    doseRegularityCourseDurtion = ['']*3

    groupNames = dbFunc.databaseFullColumnImport('groupName')
    dosageForm = dbFunc.databaseFullColumnImport('dosageForm')
    dosage = dbFunc.databaseFullColumnImport('dosage')
    latinName = dbFunc.databaseFullColumnImport('latinName')
    brandName = dbFunc.databaseFullColumnImport('brandName')
    dose = dbFunc.databaseFullColumnImport('dose')
    regularity = dbFunc.databaseFullColumnImport('regularity')
    courseDuration = dbFunc.databaseFullColumnImport('courseDuration')

    rgbBGC_GroupNames = 'rgb(114, 147, 203);'
    rgbBGC_DosageForm = 'rgb(225, 151, 76);'
    rgbBGC_Dosage = 'rgb(132, 186, 91);'
    rgbBGC_Mask = 'rgb(211, 94, 96);'
    rgbBGC_LatinName = 'rgb(220, 220, 220);'
    rgbBGC_BrandName = 'rgb(210, 210, 210);'
    rgbBGC_Dose = 'rgb(128, 133, 133);'
    rgbBGC_Regularity = 'rgb(144, 103, 167);'
    rgbBGC_CourseDuration = 'rgb(171, 104, 87);'



    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        font = QtGui.QFont()
        font.setFamily("Microsoft New Tai Lue")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("medical_icon.icns"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.drugGroupScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.drugGroupScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_GroupNames) 
        self.drugGroupScAr.setWidgetResizable(True)
        self.drugGroupScAr.setObjectName("drugGroupScAr")
        self.drugGroupWidgetContents = QtWidgets.QWidget()
        self.drugGroupWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 176))
        self.drugGroupWidgetContents.setObjectName("drugGroupWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.drugGroupWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        for i in range (len(Ui_MainWindow.groupNames)):
            self.groupNamesButton.append(QtWidgets.QPushButton(self.drugGroupWidgetContents))
            self.groupNamesButton[i].setObjectName('groupName ' + str(i))
            self.groupNamesButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_5.addWidget(self.groupNamesButton[i])      
        self.drugGroupScAr.setWidget(self.drugGroupWidgetContents)
        self.verticalLayout_3.addWidget(self.drugGroupScAr)
        self.dosageFormScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.dosageFormScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_DosageForm) 
        self.dosageFormScAr.setWidgetResizable(True)
        self.dosageFormScAr.setObjectName("dosageFormScAr")
        self.dosageFormWidgetContents = QtWidgets.QWidget()
        self.dosageFormWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 176))
        self.dosageFormWidgetContents.setObjectName("dosageFormWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dosageFormWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        for i in range (len(Ui_MainWindow.dosageForm)):
            self.dosageFormButton.append(QtWidgets.QPushButton(self.dosageFormWidgetContents))
            self.dosageFormButton[i].setObjectName('dosageForm ' + str(i))
            self.dosageFormButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_6.addWidget(self.dosageFormButton[i])
        self.dosageFormScAr.setWidget(self.dosageFormWidgetContents)
        self.verticalLayout_3.addWidget(self.dosageFormScAr)
        self.dosageScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.dosageScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_Dosage) 
        self.dosageScAr.setWidgetResizable(True)
        self.dosageScAr.setObjectName("dosageScAr")
        self.dosageWidgetContents = QtWidgets.QWidget()
        self.dosageWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 175))
        self.dosageWidgetContents.setObjectName("dosageWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dosageWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        for i in range (len(Ui_MainWindow.dosage)):
            self.dosageButton.append(QtWidgets.QPushButton(self.dosageWidgetContents))
            self.dosageButton[i].setObjectName('dosage ' + str(i))
            self.dosageButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_7.addWidget(self.dosageButton[i])       
        self.dosageScAr.setWidget(self.dosageWidgetContents)
        self.verticalLayout_3.addWidget(self.dosageScAr)
        self.maskScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.maskScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_Mask) 
        self.maskScAr.setWidgetResizable(True)
        self.maskScAr.setObjectName("maskScAr")
        self.maskWidgetContents = QtWidgets.QWidget()
        self.maskWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 176))
        self.maskWidgetContents.setObjectName("maskWidgetContents")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.maskWidgetContents)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_2 = QtWidgets.QPushButton(self.maskWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.buttonClicked)
        self.verticalLayout_16.addWidget(self.pushButton_2)
        self.maskScAr.setWidget(self.maskWidgetContents)
        self.verticalLayout_3.addWidget(self.maskScAr)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.latinDrugsScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.latinDrugsScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_LatinName) 
        self.latinDrugsScAr.setWidgetResizable(True)
        self.latinDrugsScAr.setObjectName("latinDrugsScAr")
        self.latinDrugsWidgetContents = QtWidgets.QWidget()
        self.latinDrugsWidgetContents.setGeometry(QtCore.QRect(0, 0, 234, 729))
        self.latinDrugsWidgetContents.setObjectName("latinDrugsWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.latinDrugsWidgetContents)

        self.verticalLayout_4.setObjectName("verticalLayout_4")

        for i in range (len(Ui_MainWindow.latinName)):
            self.latinNameButton.append(QtWidgets.QPushButton(self.latinDrugsWidgetContents))
            self.latinNameButton[i].setObjectName('latinName ' + str(i))
            self.latinNameButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_4.addWidget(self.latinNameButton[i])

        self.latinDrugsScAr.setWidget(self.latinDrugsWidgetContents)
        self.horizontalLayout.addWidget(self.latinDrugsScAr)
        self.brandNameScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.brandNameScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_BrandName) 
        self.brandNameScAr.setWidgetResizable(True)
        self.brandNameScAr.setObjectName("brandNameScAr")
        self.brandNameWidgetContents = QtWidgets.QWidget()
        self.brandNameWidgetContents.setGeometry(QtCore.QRect(0, 0, 234, 729))
        self.brandNameWidgetContents.setObjectName("brandNameWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.brandNameWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        for i in range (len(Ui_MainWindow.brandName)):
            self.brandNameButton.append(QtWidgets.QPushButton(self.brandNameWidgetContents))
            self.brandNameButton[i].setObjectName('brandName ' + str(i))
            self.brandNameButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_8.addWidget(self.brandNameButton[i])
        self.brandNameScAr.setWidget(self.brandNameWidgetContents)
        self.horizontalLayout.addWidget(self.brandNameScAr)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doseScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.doseScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_Dose) 
        self.doseScAr.setWidgetResizable(True)
        self.doseScAr.setObjectName("doseScAr")
        self.doseWidgetContents = QtWidgets.QWidget()
        self.doseWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 237))
        self.doseWidgetContents.setObjectName("doseWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.doseWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        for i in range (len(Ui_MainWindow.dose)):
            self.doseButton.append(QtWidgets.QPushButton(self.doseWidgetContents))
            self.doseButton[i].setObjectName('dose ' + str(i))
            self.doseButton[i].setCheckable(True)
            self.doseButton[i].clicked.connect(self.checkableOneActive)
            self.doseButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_9.addWidget(self.doseButton[i])



        self.doseScAr.setWidget(self.doseWidgetContents)
        self.verticalLayout_2.addWidget(self.doseScAr)
        self.regularityScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.regularityScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_Regularity) 
        self.regularityScAr.setWidgetResizable(True)
        self.regularityScAr.setObjectName("regularityScAr")
        self.regularityWidgetContents = QtWidgets.QWidget()
        self.regularityWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 237))
        self.regularityWidgetContents.setObjectName("regularityWidgetContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.regularityWidgetContents)
        self.verticalLayout_10.setObjectName("verticalLayout_10")


        for i in range (len(Ui_MainWindow.regularity)):
            self.regularityButton.append(QtWidgets.QPushButton(self.regularityWidgetContents))
            self.regularityButton[i].setObjectName('regularity ' + str(i))
            self.regularityButton[i].setCheckable(True)
            self.regularityButton[i].clicked.connect(self.checkableOneActive)
            self.regularityButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_10.addWidget(self.regularityButton[i])

        self.regularityScAr.setWidget(self.regularityWidgetContents)
        self.verticalLayout_2.addWidget(self.regularityScAr)
        self.courseDurationScAr = QtWidgets.QScrollArea(self.centralwidget)
        self.courseDurationScAr.setStyleSheet("background-color: " + Ui_MainWindow.rgbBGC_CourseDuration) 
        self.courseDurationScAr.setWidgetResizable(True)
        self.courseDurationScAr.setObjectName("courseDurationScAr")
        self.courseDurationWidgetContents = QtWidgets.QWidget()
        self.courseDurationWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 237))
        self.courseDurationWidgetContents.setObjectName("courseDurationWidgetContents")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.courseDurationWidgetContents)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        for i in range (len(Ui_MainWindow.courseDuration)):
            self.courseDurationButton.append(QtWidgets.QPushButton(self.courseDurationWidgetContents))
            self.courseDurationButton[i].setObjectName('courseDuration ' + str(i))
            self.courseDurationButton[i].setCheckable(True)
            self.courseDurationButton[i].clicked.connect(self.checkableOneActive)
            self.courseDurationButton[i].clicked.connect(self.buttonClicked)
            self.verticalLayout_11.addWidget(self.courseDurationButton[i])


        self.courseDurationScAr.setWidget(self.courseDurationWidgetContents)
        self.verticalLayout_2.addWidget(self.courseDurationScAr)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.textLine = QtWidgets.QLineEdit(self.centralwidget)
        self.textLine.setReadOnly(True)
        self.textLine.setObjectName("textLine")
        self.gridLayout.addWidget(self.textLine, 1, 0, 1, 1)
        self.buttonCopyToClipboard = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopyToClipboard.setObjectName("buttonCopyToClipboard")
        self.buttonCopyToClipboard.clicked.connect(self.textLineCopyToClipboard)
        self.gridLayout.addWidget(self.buttonCopyToClipboard, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Помощник психиатра Ver 0.9.1"))
        for i in range (len(Ui_MainWindow.groupNames)):
            self.groupNamesButton[i].setText(_translate("MainWindow", Ui_MainWindow.groupNames[i]))
        for i in range (len(Ui_MainWindow.dosageForm)):
            self.dosageFormButton[i].setText(_translate("MainWindow", Ui_MainWindow.dosageForm[i]))
        for i in range (len(Ui_MainWindow.dosage)):
            self.dosageButton[i].setText(_translate("MainWindow", str(Ui_MainWindow.dosage[i])))

        self.pushButton_2.setText(_translate("MainWindow", "FullList"))

        for i in range (len(Ui_MainWindow.latinName)):
            if (len(self.latinName[i]) >=45):
                self.latinNameButton[i].setStyleSheet(" \
                        font-family: Microsoft New Tai Lue; \
                        font-size: 7pt; \
                        font-weight: bold, 75; \
                        background-color: " + Ui_MainWindow.rgbBGC_LatinName)


            self.latinNameButton[i].setText(_translate("MainWindow", Ui_MainWindow.latinName[i]))

        for i in range (len(Ui_MainWindow.brandName)):
            self.brandNameButton[i].setText(_translate("MainWindow", Ui_MainWindow.brandName[i]))

        for i in range (len(Ui_MainWindow.dose)):
            self.doseButton[i].setText(_translate("MainWindow", str(Ui_MainWindow.dose[i])))

        for i in range (len(Ui_MainWindow.regularity)):
            self.regularityButton[i].setText(_translate("MainWindow", Ui_MainWindow.regularity[i]))

        for i in range (len(Ui_MainWindow.courseDuration)):
            self.courseDurationButton[i].setText(_translate("MainWindow", Ui_MainWindow.courseDuration[i]))

    
        self.buttonCopyToClipboard.setText(_translate("MainWindow", "Копировать"))

    def checkableOneActive (self):
        send = self.MainWindow.sender()
        nameOfSenderGroup = sources.removeCharactersFromString(send.objectName())

        if nameOfSenderGroup == 'dose':
            for i in range (len(Ui_MainWindow.dose)):
                if self.doseButton[i].isChecked():
                    self.doseButton[i].toggle()
        if nameOfSenderGroup == 'regularity':
            for i in range (len(Ui_MainWindow.regularity)):
                if self.regularityButton[i].isChecked():
                    self.regularityButton[i].toggle()
        if nameOfSenderGroup == 'courseDuration':
            for i in range (len(Ui_MainWindow.courseDuration)):
                if self.courseDurationButton[i].isChecked():
                    self.courseDurationButton[i].toggle()

        send.toggle()
            


        
       
    def buttonClicked(self):

        global resultList
        
        send = self.MainWindow.sender()
        
        if send.objectName() == 'pushButton_2':
            self.paintAllInactiveTable ('grey',True)
            dbFunc.setSqlVariablesToEmpty()
            self.textLine.setText('')
            return

        

        nameOfSenderGroup = sources.removeCharactersFromString(send.objectName())


                   
        if (nameOfSenderGroup != 'dosageForm') and (nameOfSenderGroup != 'dosage') and (
            nameOfSenderGroup != 'latinName') and (nameOfSenderGroup !='brandName') and (nameOfSenderGroup != 'groupName'):
            if nameOfSenderGroup == 'dose':
                doseRegularityCourseDurtion [0] = float(send.text())
            elif nameOfSenderGroup == 'regularity':
                doseRegularityCourseDurtion [1] = send.text()
            elif nameOfSenderGroup == 'courseDuration':
                doseRegularityCourseDurtion [2] = send.text()

            if 'resultList' in globals(): 
                if (doseRegularityCourseDurtion[0] == '') or (doseRegularityCourseDurtion[1] == '') or (doseRegularityCourseDurtion[2] == ''):
                    pass
                else:
                    self.checkForOneRowInTable ()
                     





            print (doseRegularityCourseDurtion, sep = '\t')

            return 


        resultList = dbFunc.databaseCompositeSelection(nameOfSenderGroup, str(send.text()))
        if len(resultList) == 0:
            dbFunc.setSqlVariablesToEmpty()
            return
        print ('\t',resultList)
        if (doseRegularityCourseDurtion[0] == '') or (doseRegularityCourseDurtion[1] == '') or (doseRegularityCourseDurtion[2] == ''):
            pass
        else:
            self.checkForOneRowInTable ()

        
           
        
        
        self.paintAllInactiveTable('grey', False)
        self.paintTable (resultList)

    def checkForOneRowInTable (self):
        if (len(resultList) == 1) or (
                            (resultList[0][2]==resultList[1][2]) 
                        and (resultList[0][3]==resultList[1][3])
                        and (resultList[0][6]==resultList[1][6])):
            self.setMyTextLine (resultList) 
        else:
            self.textLine.setText('')


    def paintDefaultTable (self):
        self.drugGroupWidgetContents.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + Ui_MainWindow.rgbBGC_GroupNames)
        self.dosageFormWidgetContents.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + Ui_MainWindow.rgbBGC_DosageForm)
        self.dosageWidgetContents.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + Ui_MainWindow.rgbBGC_Dosage)
        self.latinDrugsWidgetContents.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + Ui_MainWindow.rgbBGC_LatinName)
        self.brandNameWidgetContents.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + Ui_MainWindow.rgbBGC_BrandName)


    def paintTable (self, elementsToPaint):
               
        for i in range (0,len(elementsToPaint)):
            for j in range (0,len(self.brandNameButton)):
                if elementsToPaint[i][1] == self.brandNameButton[j].text():
                    self.colorise (self.brandNameButton[j], 'grey')
                    self.brandNameButton[j].setVisible(True)
                
            for j in range (0,len(self.dosageFormButton)):
                if elementsToPaint[i][2] == self.dosageFormButton[j].text():
                    self.colorise (self.dosageFormButton[j], 'grey')
                    self.dosageFormButton[j].setVisible(True)
                

            for j in range (0,len(self.dosageButton)):
                if str(elementsToPaint[i][3]) == str(self.dosageButton[j].text()):
                    self.colorise (self.dosageButton[j], 'grey')
                    self.dosageButton[j].setVisible(True)
            

            for j in range (0,len(self.latinNameButton)):
                if elementsToPaint[i][7] == self.latinNameButton[j].text():
                    self.colorise (self.latinNameButton[j], 'grey')
                    self.latinNameButton[j].setVisible(True)
                

            for j in range (0,len(self.groupNamesButton)):
                if elementsToPaint[i][8] == self.groupNamesButton[j].text():
                    self.colorise (self.groupNamesButton[j], 'grey')
                    self.groupNamesButton[j].setVisible(True)
                
              
    def paintAllInactiveTable(self, colour:list, flag):
        for i in range (0,len(self.brandNameButton)):
            self.colorise (self.brandNameButton[i], colour)
            self.brandNameButton[i].setVisible(flag)         
        for i in range (0,len(self.dosageFormButton)):
            self.colorise (self.dosageFormButton[i], colour)
            self.dosageFormButton[i].setVisible(flag)
        for i in range (0,len(self.dosageButton)):
            self.colorise (self.dosageButton[i], colour)
            self.dosageButton[i].setVisible(flag)
        for i in range (0,len(self.latinNameButton)):
            self.colorise (self.latinNameButton[i], colour)
            self.latinNameButton[i].setVisible(flag)
        for i in range (0,len(self.groupNamesButton)):
            self.colorise (self.groupNamesButton[i], colour)
            self.groupNamesButton[i].setVisible(flag)
 
    def colorise (self, buttonToColorise, colour:list):
        buttonToColorise.setStyleSheet(" \
            font-family: Microsoft New Tai Lue; \
            font-size: 9pt; \
            font-weight: bold, 75; \
            background-color: " + colour)

 
    def textLineCopyToClipboard(self):
      
        sources.copy_to_clipboard(self.textLine.displayText())

    def setMyTextLine(self, myTable):






        partOfLine_1 = myTable [0][7]
        if myTable [0][3] == None:
            partOfLine_2 = ''
            partOfLine_4 = 1 * (doseRegularityCourseDurtion[0])
            partOfLine_5 = 'таб'
        else:
            partOfLine_2 = str(float(myTable [0][3])/1000)
            partOfLine_4 = str((myTable [0][3])*(doseRegularityCourseDurtion[0]))
            partOfLine_5 = myTable [0][4]
        partOfLine_3 = myTable [0][2]

       
        
        partOfLine_6 = doseRegularityCourseDurtion [1]
        partOfLine_7 = doseRegularityCourseDurtion [2]
        partOfLine_8 = myTable [0][5]




        textLineComposition = f'{partOfLine_1} {partOfLine_2} in {partOfLine_3} По {partOfLine_4} {partOfLine_5} {partOfLine_6} ({partOfLine_7}, №{partOfLine_8})' 

        self.textLine.setText(str(textLineComposition))


    







