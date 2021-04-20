from PyQt5.QtWidgets import *

# menubar
def createMenuBar(self):
    menubar = QMenuBar()
    menubar.setObjectName("menubar")
#########file menu################
    filemenu = QMenu("File", self)
    # new file
    # open file
    newFileAction = QAction("New", self)
    newFileAction.triggered.connect(self.newFile)
    newFileAction.setShortcut("Ctrl+N")
    filemenu.addAction(newFileAction)
    #save file
    saveAction = QAction("Save as", self)
    saveAction.setShortcut("Ctrl+S")
    saveAction.triggered.connect(self.saveFile)
    filemenu.addAction(saveAction)

    # open file
    openFileAction = QAction("Open", self)
    openFileAction.triggered.connect(self.openFile)
    openFileAction.setShortcut("Ctrl+O")
    filemenu.addAction(openFileAction)



    menubar.addMenu(filemenu)

###############################



#########edit menu############

    editmenu = QMenu("Edit", self)

    # copy 
    copyAction = QAction("Copy", self)
    copyAction.triggered.connect(self.editor.copy)
    editmenu.addAction(copyAction)

    # cut 
    cutAction = QAction("Cut", self)
    cutAction.triggered.connect(self.editor.cut)
    editmenu.addAction(cutAction)

    # paste 
    pasteAction = QAction("Paste", self)
    pasteAction.triggered.connect(self.editor.paste)
    editmenu.addAction(pasteAction)

    # selectAll 
    selectAllAction = QAction("Select All", self)
    selectAllAction.triggered.connect(self.editor.selectAll)
    editmenu.addAction(selectAllAction)

    # clearAll 
    clearAction = QAction("Clear", self)
    clearAction.triggered.connect(self.editor.clear)
    editmenu.addAction(clearAction)

  
    menubar.addMenu(editmenu)
##############################


#########edit menu############
    
    veiwmenu = QMenu("View",self)
    # normalscreen
    normalscreenAction = QAction("Normal",self)
    normalscreenAction.triggered.connect(self.showNormal)
    normalscreenAction.setShortcut("Ctrl+Shift+N")
    veiwmenu.addAction(normalscreenAction)
    # fullscreen
    fullscreenAction = QAction("Fullscreen",self)
    fullscreenAction.triggered.connect(self.showFullScreen)
    fullscreenAction.setShortcut("Ctrl+F")
    veiwmenu.addAction(fullscreenAction)

    menubar.addMenu(veiwmenu)

##############################



    self.setMenuBar(menubar)