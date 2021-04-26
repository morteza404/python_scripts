import sys
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("Hello World!")
label.resize(550, 400)
label.setWindowTitle('First PySide Application')
label.show()

sys.exit(app.exec_())