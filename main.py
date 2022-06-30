import requests
import time
from bs4 import BeautifulSoup as bs
from flask import Flask
#" + time.strftime("%Y-%m-%d", time.localtime()) + "

app = Flask(__name__)

@app.route('/api/1')
def DG():  #도리원-구미-api
      page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3736202&arvl_Trml_Cd=3923301&depr_Trml_Nm=%EB%8F%84%EB%A6%AC%EC%9B%90&arvl_Trml_Nm=%EA%B5%AC%EB%AF%B8&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", headers={"Content-Type": "application/x-www-form-urlencoded"})
      print(page.text)

      soup = bs(page.text, "html.parser")

      elements = soup.select('.btn_reservation > strong')

      data1 = list()

      for index, element in enumerate(elements[:4], 1):
          data1.append(element.text)
      return ','.join(data1)

                                            
@app.route('/api/2')
def DI():  #도리원-인천-api
      page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3736202&arvl_Trml_Cd=2224201&oneway_return=on&depr_Trml_Nm=%EB%8F%84%EB%A6%AC%EC%9B%90&arvl_Trml_Nm=%EC%9D%B8%EC%B2%9C&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", headers={"Content-Type": "application/x-www-form-urlencoded"})
      print(page.text)

      soup = bs(page.text, "html.parser")

      elements = soup.select('.btn_reservation > strong')

      data = list()

      for index, element in enumerate(elements[:2], 1):
          data.append(element.text)
      return ','.join(data)

@app.route('/api/3')
def DS():  #도리원-서울-api
        page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3736202&arvl_Trml_Cd=0511601&oneway_return=on&depr_Trml_Nm=%EB%8F%84%EB%A6%AC%EC%9B%90&arvl_Trml_Nm=%EB%8F%99%EC%84%9C%EC%9A%B8&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", headers={"Content-Type": "application/x-www-form-urlencoded"})
        print(page.text)

        soup = bs(page.text, "html.parser")

        elements = soup.select('.btn_reservation > strong')

        data = list()
                     
        for index, element in enumerate(elements[:4], 1):
            data.append(element.text)
        return ','.join(data)

@app.route('/api/4')
def UD():  #의성-동대구-api
        page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3733501&arvl_Trml_Cd=4124601&oneway_return=on&depr_Trml_Nm=%EC%9D%98%EC%84%B1&arvl_Trml_Nm=%EB%8F%99%EB%8C%80%EA%B5%AC&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", headers={"Content-Type": "application/x-www-form-urlencoded"})
        print(page.text)

        soup = bs(page.text, "html.parser")

        elements = soup.select('.btn_reservation > strong')

        data = list()

        for index, element in enumerate(elements[:2], 1):
            data.append(element.text)
        return ','.join(data)

@app.route('/api/5')
def UDB():  #의성-대구북부-api
        page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3733501&arvl_Trml_Cd=4171101&oneway_return=on&depr_Trml_Nm=%EC%9D%98%EC%84%B1&arvl_Trml_Nm=%EB%8C%80%EA%B5%AC%EB%B6%81%EB%B6%80&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", headers={"Content-Type": "application/x-www-form-urlencoded"})
        print(page.text)

        soup = bs(page.text, "html.parser")

        elements = soup.select('.btn_reservation > strong')

        data = list()

        for index, element in enumerate(elements[:6], 1):
            data.append(element.text)
        return ','.join(data)
app.run()
