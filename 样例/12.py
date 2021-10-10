#Vscode需要单独的生成一个main函数来进行窗体文件的调用
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_untitled          #引用生成好的文件名称

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_untitled.Ui_Form()          #调用文件里面的方法
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
