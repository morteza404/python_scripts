from tkinter import *
from tkinter import filedialog
import xlrd
def import_nodes(self):
        filepath = filedialog.askopenfilenames(filetypes = (('xls files','*.xls'),))
        if not filepath:
            return
        else:
            filepath ,= filepath
        book = xlrd.open_workbook(filepath)
        try:
            sheet = book.sheet_by_index(0)
        # if the sheet cannot be found, there's nothing to import
        except xlrd.biffh.XLRDError:
            warnings.warn('the excel file is empty: import failed')
        for row_index in range(1, sheet.nrows):
            x, y = self.to_canvas_coordinates(*sheet.row_values(row_index))
            self.create_object(x, y)
