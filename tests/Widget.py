import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QStyledItemDelegate


Label = QtCore.Qt.DisplayRole
Section = QtCore.Qt.UserRole + 1
IsSection = QtCore.Qt.UserRole + 2


class Item(object):
    @classmethod
    def paint(cls, painter, option, index):
        rect = QtCore.QRectF(option.rect)

        painter.save()

        if option.state & QtWidgets.QStyle.State_MouseOver:
            painter.fillRect(rect, QtGui.QColor("#0EE"))
            print('oops')

        if option.state & QtWidgets.QStyle.State_Selected:
            painter.fillRect(rect, QtGui.QColor("#FDD"))


        painter.drawText(rect.adjusted(20, 0, 0, 0),
                         index.data(Label))

        painter.restore()

    @classmethod
    def sizeHint(cls, option, index):
        return QtCore.QSize(option.rect.width(), 20)


class Section(object):
    @classmethod
    def paint(self, painter, option, index):
        painter.save()
        painter.setPen(QtGui.QPen(QtGui.QColor("#F66")))
        painter.drawText(QtCore.QRectF(option.rect), index.data(Label))
        painter.restore()

    @classmethod
    def sizeHint(self, option, index):
        return QtCore.QSize(option.rect.width(), 20)


class Delegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.data(IsSection):
            return Section.paint(painter, option, index)
        else:
            return Item.paint(painter, option, index)

    def sizeHint(self, option, index):
        if index.data(IsSection):
            return Section.sizeHint(option, index)
        else:
            return Item.sizeHint(option, index)


class Model(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.items = list()

    def data(self, index, role):
        item = self.items[index.row()]

        return {
            Label: item["label"],
            Section: item["section"],
            IsSection: False
        }.get(role)

    def append(self, item):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def rowCount(self, parent=None):
        return len(self.items)


class Proxy(QtCore.QSortFilterProxyModel):
    def data(self, index, role):
        if index.row() >= self.sourceModel().rowCount():

            return {
                Label: "Virtual Label",
                Section: "Virtual Section",
                IsSection: True
            }.get(role)

        return self.sourceModel().data(index, role)

    def rowCount(self, parent):
        sections = 0

        prev = None
        for item in self.sourceModel().items:
            cur = item["section"]

            if cur != prev:
                sections += 1

            prev = cur

        # Note: This includes 1 additional, duplicate, section
        # for the bottom item. Ordering of items in model is important.
        return self.sourceModel().rowCount() + sections

    def index(self, row, column, parent):
        return self.createIndex(row, column, parent)

    def mapToSource(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        return self.sourceModel().createIndex(index.row(),
                                              index.column(),
                                              QtCore.QModelIndex())

    def parent(self, index):
        return QtCore.QModelIndex()


app = QtWidgets.QApplication(sys.argv)
model = Model()

for item in ({"label": "Ben", "section": "Human"},
             {"label": "Steve", "section": "Human"},
             {"label": "Alpha12", "section": "Robot"},
             {"label": "Mike", "section": "Toaster"},
             {"label": "Steve", "section": "Human"},
             ):
    model.append(item)

proxy = Proxy()
proxy.setSourceModel(model)

delegate = Delegate()

view = QtWidgets.QListView()
view.setWindowTitle("My View")
view.setModel(proxy)
view.setItemDelegate(delegate)
view.show()

app.exec_()