import numpy as np
from datetime import datetime
import pandas as pd

def bnh(df, column = 'Close', start = '20000101', end = '20200101'): # 매개변수가 *df면 가변의 의미, column, start, end에 디폴타값 생성
    # 인덱스 시계열로 변경
    df.index = pd.to_datetime(df.index)
    start = datetime.strptime(start, '%Y%m%d')
    end = datetime.strptime(end, '%Y%m%d')
    df = df.loc[start: end]     # iloc : 인덱스의 위치, loc : 인덱스의 값

    # 결측치, 무한대 제외
    df = df.loc[~df.isin([np.nan, np.inf, -np.inf]).any(axis='columns')]

    # 수정 종가만 있는 데이터프레임으로 변경
    df = df[[column]]  # df = df['Adj Close'] : 데이터형태가 Series

    # 일별 수익률 변수 생성
    df['daily_rtn'] = df[column].pct_change()

    # 누적 수익률 변수 생성
    df['st_rtn'] = (1 + df['daily_rtn']).cumprod()
    
    # 데이터프레임을 리턴
    return df