from PySide2 import QtWidgets


from ui import Basic


class MYQTAPP(Basic.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MYQTAPP,self).__init__()
        self.setupUi(self)
        self.showMaximized() #for full screen
        self.setWindowTitle("Trial")
        self.list_widget()
        self.tree_widget()
        self.push.clicked.connect(self.fill_form)

    def tree_widget(self):
        self.treeWidget.clear()
        values = ['apple', 'banana', 'mango']
        for each in values:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0,each)

    def list_widget(self):
        self.listWidget.clear()
        item = ['apple', 'banana', 'mango']
        self.listWidget.addItems(item)

    def fill_form(self):
        name = self.name_bar.text()
        if not name:
            QtWidgets.QMessageBox.about(self,"name required")
        print(name)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MYQTAPP()
    qt_app.show()
    app.exec_()






