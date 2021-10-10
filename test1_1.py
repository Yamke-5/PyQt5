import sys
# 导入系统模块
from PyQt5.QtWidgets import QApplication, QWidget
# 引入pyqt5模块
if __name__ == '__main__':
    # 创建一个qApplication类的实例
    app = QApplication(sys.argv)
    # 画一个窗口
    widow = QWidget()
    # 设置窗口的尺寸
    widow.resize(800, 600)
    # 移动窗口位置
    widow.move(100, 50)
    # 设置窗口的标题
    widow.setWindowTitle('第一个窗口')
    # 做完上面的操作一定要显示这个窗口
    # 所以一定要加上show()方法
    widow.show()
    # 进入程序的主循环，并通过exit函数退出
    sys.exit(app.exec_())
    # 这里退出了app这个实例
