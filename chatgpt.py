import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from chatgpt_ui import Ui_MainWindow
import openai


class ChatGPT(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.login_status = False  #登录状态默认false
        self.model_name = "gpt-3.5-turbo"  # 默认模型
        self.setupUi(self)
        self.pushButton.clicked.connect(self.submit)  # 连接按钮和槽函数
        self.pushButton_2.clicked.connect(self.login)
        self.textBrowser.setOpenExternalLinks(True)

    
    def submit(self): 
        text = self.textEdit_2.toPlainText()
        if text is None or text == "":
            return
        print(text)
        if self.login_status == False:
            self.textBrowser.append('请您先登录..')
            self.textEdit_2.clear()  # 清空 textEdit_2
            return

        self.textBrowser.update()
        owner_img = "owner.jpg"
        html = '<p> <img src="%s" alt="image" width="32" height="32"> %s</p>'%(owner_img, text)
        self.textBrowser.append(html)
        self.textBrowser.update()
        self.textBrowser.repaint()

        self.textEdit_2.clear()  # 清空 textEdit_2
        res = self.do_chatgpt(text) 
        chat_img = "chat.png"  
        html = '<p> <img src="%s" alt="image" width="32" height="32"> %s</p>'%(chat_img, res)
        self.textBrowser.append(html)   

    def login(self):
        organization = self.lineEdit.text()
        api_key = self.lineEdit_2.text()
        if organization is None or organization == "":
            return
        if api_key is None or api_key == "":
            return
        
        if  self.login_status == False:
            openai.organization = organization
            openai.api_key = api_key  
            try:       
                self.init_model_list() #初始化模型列表
                self.login_status = True
                self.textBrowser.append("登录成功")  # 在 textBrowser 中显示文本
                self.pushButton_2.setText("已登录")
            except Exception as e:       
                msg_box = QMessageBox(QMessageBox.Warning, '警告', str(e))
                msg_box.exec_()
                self.textBrowser.append("登录失败..")  # 在 textBrowser 中显示文本
                self.pushButton_2.setText("重新登录")

          
    def init_model_list(self):
        try:
            model_list =  openai.Model.list()
            model_dict = {}
            for k, model in enumerate(model_list.data):
                if ":" in model.root:
                    continue
                print(model.root)
                model_dict[k] = model.root 
            i = 0
            for k,model in model_dict.items():
                self.comboBox.addItem(model)
                if model == "gpt-3.5-turbo":
                    i = k
            self.comboBox.setCurrentIndex(i)   # 设置默认值
            self.comboBox.currentIndexChanged.connect(self.on_combobox_changed)  # 连接信号和槽函数
        except Exception as e:
            print(str(e))
            raise e

    def on_combobox_changed(self):
        self.model_name = self.comboBox.currentText()

    #发起chatgpt请求
    def do_chatgpt(self,text):
        try:
            res = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[{"role":"user","content":text}],
                temperature=0.7,
                max_tokens=1000,
                top_p=1 
            )
            return res.choices[0].message.content
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chatgpt = ChatGPT()
    chatgpt.show()
    sys.exit(app.exec_())
