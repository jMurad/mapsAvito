import sys
from PySide2.QtWidgets import QApplication, QStyle, QStyledItemDelegate, QGridLayout, QListView, QWidget
from PySide2.QtCore import QUrl, QAbstractListModel, Qt, QModelIndex, QRectF, QSize
from PySide2.QtGui import QColor, QBrush, QPen, QPainter, QRadialGradient
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PySide2.QtWebEngineCore import QWebEngineUrlRequestInterceptor
# from PySide2 import QtNetwork


'''
class UrlInput(QLineEdit):
    def __init__(self, browser):
        super(UrlInput, self).__init__()
        self.browser = browser
        self.returnPressed.connect(self._return_pressed)

    def _return_pressed(self):
        url = QUrl(self.text())
        browser.load(url)
'''


# Перехват запросов
class WebEngineUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        # info.setHttpHeader("X-Frame-Options", "ALLOWALL")
        # print("interceptRequest")
        # print(info.requestUrl())
        pass


# Просмотр урлов
class MyWebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        # print("acceptNavigationRequest")
        # print(url)
        return QWebEnginePage.acceptNavigationRequest(self, url, _type, isMainFrame)


# Модель для ListView
class Model(QAbstractListModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.items = list()

    def data(self, index, role):
        item = self.items[index.row()]

        return {
            Qt.DisplayRole: [item["label"], item["countMsg"]],
            Qt.DecorationRole: item["section"]
        }.get(role)

    def append(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def rowCount(self, parent=None):
        return len(self.items)


# Класс для отрисовки элементов ListView
class Item(object):
    @classmethod
    def paint(cls, painter, option, index):
        rect = QRectF(option.rect)
        w, h = option.rect.width(), option.rect.height()

        painter.save()

        if index.row() % 2 == 0:
            painter.fillRect(rect, QColor("#FFFFFF"))
        else:
            painter.fillRect(rect, QColor("#EFF5F5"))

        if option.state & QStyle.State_MouseOver:
            painter.fillRect(rect, QColor("#8CCDDE"))

        if option.state & QStyle.State_Selected:
            painter.fillRect(rect, QColor("#5FA4DD"))

        painter.drawText(rect.adjusted(0, 0, 0, 0), Qt.AlignVCenter, index.data(Qt.DisplayRole)[0])

        if index.data(Qt.DecorationRole) == "true":
            pbrush = QPen(QBrush(QColor("#F2A6A6"), Qt.SolidPattern), 1)
            painter.setPen(pbrush)
            circlerect = QRectF(w-h-1, h * index.row()+1, h - 2, h - 2)
            gradient = QRadialGradient(circlerect.center(), h, circlerect.center())
            gradient.setColorAt(0.0, QColor("#F2A6A6"))
            gradient.setColorAt(0.5, QColor("#EE8181"))
            gradient.setColorAt(1.0, QColor("#E55252"))
            brush = QBrush(gradient)
            painter.setBrush(brush)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.drawEllipse(circlerect)

            pbrush = QPen(QBrush(QColor("#313131")), 20)
            painter.setPen(pbrush)
            painter.drawText(circlerect, Qt.AlignCenter, str(index.data(Qt.DisplayRole)[1]))

        painter.restore()

    @classmethod
    def sizeHint(cls, option, index):
        return QSize(option.rect.width(), 20)


# Делегат отрисовки элементов ListView
class Delegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.data(Qt.DisplayRole):
            return Item.paint(painter, option, index)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # proxy = QtNetwork.QNetworkProxy()
    # proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
    # proxy.setHostName("172.19.96.51")
    # proxy.setPort(9090)
    # QtNetwork.QNetworkProxy.setApplicationProxy(proxy)

    grid = QGridLayout()
    browser = QWebEngineView()
    # url_input = UrlInput(browser)
    list_view = QListView()
    list_view.setFixedWidth(300)
    interceptor = WebEngineUrlRequestInterceptor()
    profile = QWebEngineProfile()
    profile.setRequestInterceptor(interceptor)

    page = MyWebEnginePage(profile, browser)
    # page.setUrl(QUrl("https://stackoverflow.com/questions/50786186/qwebengineurlrequestinterceptor-not-working"))
    page.setUrl(QUrl("https://www.avito.ru/dagestan#login?s=h"))
    browser.setPage(page)
    # action_box = ActionInputBox(page)
    grid.addWidget(list_view, 0, 1)
    grid.addWidget(browser, 0, 2)
    print('nuu4')
    model = Model()

    for item in ({"label": "Ben", "section": "true", "countMsg": 13},
                 {"label": "Steve", "section": "false", "countMsg": 0},
                 {"label": "Alpha", "section": "true", "countMsg": 0},
                 {"label": "Mike", "section": "true", "countMsg": 1},
                 {"label": "Steve", "section": "true", "countMsg": 2},
                 ):
        model.append(item)

    list_view.setModel(model)
    delegate = Delegate()
    list_view.setItemDelegate(delegate)

    main_frame = QWidget()
    main_frame.setMinimumSize(800, 600)
    main_frame.setLayout(grid)
    main_frame.show()
    sys.exit(app.exec_())
