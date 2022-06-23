import requests
import time
from bs4 import BeautifulSoup as bs
from flask import Flask

app = Flask(__name__)


@app.route('/api/1')
def index():
    page = requests.post("https://txbus.t-money.co.kr/otck/readAlcnList.do", data="depr_Trml_Cd=3736202&arvl_Trml_Cd=3923301&depr_Trml_Nm=%EBEB%AF%B8&depr_Dt=" + time.strftime("%Y-%m-%d", time.localtime()) + "&bef_Aft_Dvs=D&req_Rec_Num=10&depr_Time=00%3A00&ig=1&im=0&ic=0&iv=0", healencoded"})
    print(page.text)

    soup = bs(page.text, "html.parser")

    elements = soup.select('.btn_reservation > strong')

    data = list()

    for index, element in enumerate(elements[:4], 1):
        data.append(element.text)
    return ','.join(data)

app.run()
