import datetime
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout, \
    QLabel, QTextEdit, QPushButton, QInputDialog, QFileDialog


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.show()


def process_data(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    contents = lines[0]
    coordinates = [float(x) for x in lines[1].split(',')]
    return {'contents': contents, 'coordinates': coordinates}


class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.text = QTextEdit(self)
        self.btn_save = QPushButton(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        self.tabs.addTab(self.tab1, "Save a file")
        self.tabs.addTab(self.tab2, "Read a file")
        self.tabs.addTab(self.tab3, "Show the map")

        # TAB 1
        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.text)
        self.tab1.layout.addWidget(self.btn_save)
        self.btn_save.setText('Save a file!')
        self.btn_save.clicked.connect(self.save_text)
        self.lab1 = QLabel()
        self.tab1.layout.addWidget(self.lab1)
        self.tab1.setLayout(self.tab1.layout)

        # TAB 2
        self.tab2.layout = QVBoxLayout(self)
        self.btn_read = QPushButton(self)
        self.btn_read.setText('Read a file!')
        self.btn_read.clicked.connect(self.read_text)
        self.tab2.layout.addWidget(self.btn_read)
        self.lab2 = QLabel()
        self.tab2.layout.addWidget(self.lab2)
        self.tab2.setLayout(self.tab2.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def save_text(self):
        my_text = self.text.toPlainText()
        lines = my_text.split("\n")
        for i, line in enumerate(lines):
            file_name, ok = QInputDialog.getText(self, "Save File", "Enter a name for the file:")
            if ok and file_name:
                with open(file_name + ".txt", "w") as f:
                    f.write(line)

    def read_text(self):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            with open(file_name, "r") as f:
                text = f.read()
            self.lab2.setText(f"{timestamp}\n{text}")

    # mam skończoną wersję na komputerze szkolnym, nie przesłała mi się najnowsza wersja
    """def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            data = process_data(file_name)
            m.save('map.html')
    """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
