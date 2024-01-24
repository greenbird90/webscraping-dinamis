#import tool webdriver via selenium
from selenium import webdriver
#memanggil fungsi waktu untuk menghitung waktu eksekusi
import time

#jika menggunakan local IDE
#from selenium.webdriver.chrome.service import Service
#membuat variabel untuk path cromedriver
#service = Service('c:\\Users\\syarifudin\\Downloads\\jupyternotebook\\chromedriver-win64\\chromedriver.exe')


#membuat fungsi untuk membuat driver
def get_drvier():
  #mengatur options agar browser mudah dijalankan

  #membuat kelas kosong
  options = webdriver.ChromeOptions()
  #menonaktifkan pop-up infobars agar tidak mengganggu script saat menjalankan browser
  options.add_argument("disable-infobars")
  #akses pada saat tampilan normal / maksimal agar kontent tidak berubah
  options.add_argument("start-maximized")
  #menghindari issue pada saat interaksi dengan browser di perangkat linux (repl)
  options.add_argument("disable-dev-shm-usage")
  #disable fungsi sandbox agar browser tidak terbatas pada mode saat menjalankan script
  options.add_argument("no-sandbox")
  #membantu selenium untuk menghindari deteksi script dari browser atau halaman web
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  #membuat variable driver dengan menggunakan chrome class dari webdriver
  driver = webdriver.Chrome(options=options)
  #membuat koneksi ke halaman web yang akan di scraping
  driver.get("https://automated.pythonanywhere.com/")
  return driver

#membuat fungsi untuk memisahkan text 
def clean_text(text):
  """Extract only the temperature from text"""
  #memformat text float dan memisahkan 
  output = float(text.split(": ")[1])
  return output

def main():
  #memanggil fungsi get_drvier untuk menjalankan driver
  driver = get_drvier()
  #stop script selama 2 detik untuk waktu jeda
  time.sleep(2)

  #membuat variabel untuk menyimpan data (xpath) dari halaman web
  element = driver.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

#cetak hasil dari fungsi main
print(main())
