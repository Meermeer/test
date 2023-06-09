## flask 로드 
from flask import Flask, render_template
import pandas as pd

## Class 생성
app = Flask(__name__)

## localhost:3000/ 요청시 index.html 리턴 api 생성
@app.route("/")
def index():
    # inex.html 그래프를 그리기 위해서 필요한 변수 값 
    # x_pos, y_pos 
    # 코로나 데이터를 로드
    # 일일 확진자 파생변수
    # x축에는 등록일시
    # y축에는 일일확진자
    df = pd.read_csv("../csv/corona.csv")
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", 
                    "기준일", "기준시간", "수정일시", "누적의심자", 
                    "누적확진률"]
    df.sort_values("등록일시", inplace=True)
    df["일일확진자"] = df["확진자"].diff().fillna(0)
    df_2 = df.tail(50)
    # x축   ##
    _x = df_2["등록일시"].tolist()    ##
    # y축   ##
    _y = df_2["일일확진자"].tolist()   ##
    # 표로 표시할 데이터    ##
    data = df_2.to_dict()
    cnt = len(df_2)
    columns = df_2.columns  # 데이터형 list
    c_cnt = len(columns)
    # print(data)
    # _x = [1,2,3,4,5]
    # _y = [40, 20, 10, 40, 100]
    return render_template("index.html", 
                            x_pos=_x, 
                            y_pos=_y, 
                            cnt = cnt, 
                            data = data, 
                            c_cnt = c_cnt, 
                            columns = columns)

@app.route("/index2")
def index2():
    df = pd.read_csv("../csv/corona.csv")
    df.columns = ["인덱스", "등록일시", "사망자", "확진자", "게시글번호", 
                    "기준일", "기준시간", "수정일시", "누적의심자", 
                    "누적확진률"]
    df.sort_values("등록일시", inplace=True)
    df["일일확진자"] = df["확진자"].diff().fillna(0)
    df["일일사망자"] = df["사망자"].diff().fillna(0)
    df_2 = df.tail(50)
    _x = df_2["등록일시"].tolist()
    _y = df_2["일일사망자"].tolist()
    data = df_2.to_dict()
    cnt = len(df_2)
    columns = df_2.columns  # 데이터형 list
    c_cnt = len(columns)
    # print(data)
    # _x = [1,2,3,4,5]
    # _y = [40, 20, 10, 40, 100]
    return render_template("index2.html", 
                            x_pos=_x, 
                            y_pos=_y, 
                            cnt = cnt, 
                            data = data, 
                            c_cnt = c_cnt, 
                            columns = columns)

app.run(port=3000)