import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Create menu actions
        menu_actions = [
            ("Option 1", "This is option 1", self.on_option1),
            ("Option 2", "This is option 2", self.on_option2),
            ("Option 3", "This is option 3", self.on_option3),
            ("Option 4", "This is option 4", self.on_option4),
            ("Option 5", "This is option 5", self.on_option5),
        ]

        for label, description, handler in menu_actions:
            action = QAction(label, self)
            action.setStatusTip(description)
            action.triggered.connect(handler)
            file_menu.addAction(action)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Simple Menu Example')
        self.show()

    def on_option1(self):
        self.show_message("You selected Option 1")

    def on_option2(self):
        self.show_message("You selected Option 2")

    def on_option3(self):
        self.show_message("You selected Option 3")

    def on_option4(self):
        self.show_message("You selected Option 4")

    def on_option5(self):
        self.show_message("You selected Option 5")

    def show_message(self, message):
        from PyQt5.QtWidgets import QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec_()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()