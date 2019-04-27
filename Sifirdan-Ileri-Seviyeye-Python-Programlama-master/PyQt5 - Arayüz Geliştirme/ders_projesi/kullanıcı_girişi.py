import sys
import sqlite3
# self klass içindeki metodların (fonksiyonların
# birbirleriyle haberleşmesini sağlar.
# birbirlerine bu şekilde ulaışlar.)
'''
Mesela:

class matematik(object):

    def __init__(self):
        self.pi=3.14
        
    def toplam(self,birinci,ikinci)
        return birinci + ikinci
        
    def çarp(self,birinci, ikinci):
        return birinci * ikinci
        
    def karesi(self,rakam)
        return self.çarp(rakam,rakam)
        
    def pinin_karesi(self):
        return self.karesi(self.pi)
        
mat=matematik()
print(mat.karesi(5))

işte burada karesi metodunun içine self ile
çarp metodunu çağırdık ve rakam değişkenini kendisiyle
çarptık. böylece tekrar çarpma fonkisyonu yazmamıza gerek 
kalmadı. klass içinde metodlarda geçerlidir bu self


__init__ ise ilk başta çağırılır. mesela program başladığında bir 
veritabınına bağlanması gerekiyorsa bunu init ile yaparsın.
yukarıdaki örnekte pi sayısı ilka başta çalışavağı için
self ile hem pi sayısına, hem de karesi metoduna ulaşuyoruz.
mat=matematik()
print(mat.pinin_karesi()) içeriye değişken atamamıza gerek yok.

def __init__(self):
    bağlantı=mongdb.connect("veritbanı")
'''


from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() #miras aldığımız fonksiyonun init clasını çağırdık.
        self.baglanti_olustur()
        self.init_ui() #fazladan özellik eklemek için bu fonksiyonu çağıracağız progmra çalıştığında.

    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")

        self.cursor=baglanti.cursor()

        self.cursor.execute("Create Table If not exists üyeler ("
                            "kullanıcı_adı TEXT,parola TEXT)")

        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giriş yap")
        self.yazi_alani= QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box=QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı firişi")
        self.giris.clicked.connect(self.login)

        self.show()

    def login(self):

        adi=self.kullanici_adi.text()
        par=self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı"
                            "== ? and parola == ?",(adi,par))

        data=self.cursor.fetchall()

        if len(data)== 0:
            self.yazi_alani.setText("Böyle bir kullanıcı yok"
                                    "\nLütfen tekrar deneyin.")

        else:
            self.yazi_alani.setText("Hoşgeldiniz " + adi)



app=QtWidgets.QApplication(sys.argv)

pencere=Pencere()

sys.exit(app.exec_()) # Programının kapanmaması için loopa sokuyor.