import sys
from PySide2.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide2.QtCore import QUrl
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PySide2.QtWidgets import QGridLayout, QLineEdit, QWidget, QHeaderView, QListView
from PySide2.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PySide2 import QtNetwork


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_frame = QWidget()
    listView = QListView()
    browser = QWebEngineView()
    grid = QGridLayout()
    ledit = QLineEdit()

    ledit.resize(50,20)
    listView.setFixedWidth(250)
    listView.setWindowTitle('Example List')
    model = QStandardItemModel(listView)

    foods = [
        'Cookie dough',  # Must be store-bought
        'Hummus',  # Must be homemade
        'Spaghetti',  # Must be saucy
        'Dal makhani',  # Must be spicy
        'Chocolate whipped cream'  # Must be plentiful
    ]

    for food in foods:
        # Create an item with a caption
        item = QStandardItem(food)

        # Add a checkbox to it
        item.setCheckable(True)

        # Add the item to the model
        #model.appendRow(item)
    item = QStandardItem(ledit)
    model.appendRow(item)
    listView.setModel(model)

    browser.load(QUrl('http://avito.ru'))

    grid.addWidget(listView, 0, 1)
    grid.addWidget(browser, 0, 2)

    main_frame.setLayout(grid)
    main_frame.show()
    sys.exit(app.exec_())
