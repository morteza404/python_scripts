import sys
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

label = QtWidgets.QLabel("<center><font color=red size=40>Hello World!</font></center>")
label.resize(550, 400)
label.setWindowTitle('First PySide Application')
label.show()

sys.exit(app.exec_())