import sys
from PySide2 import QtCore, QtWidgets
from PySide2.QtWebEngineWidgets import QWebEngineView


class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadFinished.connect(self._auth)

        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self._check_captcha)

    def _auth(self):
        print("1")
        page = self.page()
        page.runJavaScript(
            'document.querySelector("#index_email").value = "{}"'.format(
                '12345'
            )
        )
        page.runJavaScript(
            'document.querySelector("#index_pass").value = {}'.format('12345')
        )
        page.runJavaScript(
            'document.querySelector("#index_login_button").click()'
        )

        self._timer.start(1000)

    def _check_captcha(self):
        print("2")
        self._timer.stop()
        text = ''
        self.page().runJavaScript(
            ('document.querySelector("#box_layer > div.popup_box_container > '
             'div > div.box_title_wrap > div.box_title").innerHTML')
        )
        print(text)



app = QtWidgets.QApplication(sys.argv)
b = Browser()
b.load(QtCore.QUrl('https://vk.com'))
b.show()
app.exec_()