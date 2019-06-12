import sys
from PySide2.QtWidgets import QApplication, QStyle, QStyledItemDelegate, QGridLayout, QListView, QWidget
from PySide2.QtCore import QUrl, QAbstractListModel, Qt, QModelIndex, QRectF, QSize, QTimer
from PySide2.QtGui import QColor, QBrush, QPen, QPainter, QRadialGradient
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile
from PySide2.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from PySide2.QtNetwork import QNetworkProxy
from fake_useragent import UserAgent, FakeUserAgentError
import pyautogui
import threading


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


class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.imit_peop = threading.Thread(target=imitation_people, args=())
        self._timer = QTimer()
        self.loadFinished.connect(self.startTimer)
        self._timer.timeout.connect(self.start_thread_imitation)

    def startTimer(self):
        print("Start Timer")
        self._timer.start(5000)

    def start_thread_imitation(self):
        print("Thread Started")
        self._timer.stop()
        self.imit_peop.start()
        # self.page().runJavaScript("document.querySelector( '.button-button-2Fo5k' ).click()")


def imitation_people():
    print("Stop Timer")
    print('Start Imitation')
    duration = 1
    interval = 0.1
    imgXY = pyautogui.locateCenterOnScreen('imgs/start.png')
    pyautogui.moveTo(imgXY[0], imgXY[1] + 85, duration=duration)
    pyautogui.click()
    pyautogui.typewrite(list("kronsirius@gmail.com"), interval=interval)

    pyautogui.moveTo(imgXY[0], imgXY[1] + 125, duration=duration)
    pyautogui.click()
    pyautogui.typewrite(list("Muradika")+['enter'], interval=interval)

    pyautogui.moveTo(imgXY[0], imgXY[1] + 175, duration=duration)
    pyautogui.click()
    pyautogui.typewrite(list("Murad4023")+['enter'], interval=interval)

    pyautogui.moveTo(imgXY[0], imgXY[1] + 220, duration=duration)
    pyautogui.click()
    pyautogui.typewrite(list("3244dmk")+['enter'], interval=interval)


    pyautogui.moveTo(imgXY[0], imgXY[1] + 265, duration=duration)
    pyautogui.click()


def handleProxyAuthReq(url, auth, proxyhost):
    auth.setUser("80LgxYnqOE")
    auth.setPassword("gEkKsvssAK")


if __name__ == "__main__":

    try:
        print("1")
        ua = UserAgent()
        ua.update()
        userAgent = ua.random
    except FakeUserAgentError:
        print("2")
        userAgent = "Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit / 537.36 (KHTML, как Gecko) Chrome / " \
                    "72.0.3626.121 Safari / 537.36"
    app = QApplication(sys.argv)
    proxy = QNetworkProxy()
    proxy.setType(QNetworkProxy.HttpProxy)
    proxy.setHostName("109.173.124.250")
    proxy.setPort(7793)
    QNetworkProxy.setApplicationProxy(proxy)
    grid = QGridLayout()
    # browser = QWebEngineView()
    browser = Browser()
    # url_input = UrlInput(browser)
    list_view = QListView()
    list_view.setFixedWidth(300)
    #  interceptor = WebEngineUrlRequestInterceptor()
    profile = QWebEngineProfile()
    profile.setHttpUserAgent(userAgent)
    page = MyWebEnginePage(profile, browser)
    page.setUrl(QUrl("https://www.instagram.com/"))
    # page.setUrl(QUrl("https://2ip.ru"))
    browser.setPage(page)
    page_proxy = browser.page()
    page_proxy.proxyAuthenticationRequired.connect(handleProxyAuthReq)
    grid.addWidget(list_view, 0, 1)
    grid.addWidget(browser, 0, 2)
    main_frame = QWidget()
    main_frame.setMinimumSize(800, 600)
    main_frame.setLayout(grid)
    main_frame.show()
    sys.exit(app.exec_())