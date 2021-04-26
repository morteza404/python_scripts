import sys
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

wid = QtWidgets.QWidget()
wid.show()

sys.exit(app.exec_())