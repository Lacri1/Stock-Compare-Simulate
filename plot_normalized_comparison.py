import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors
from datetime import datetime

# 데이터1
data = [
# This repository does not include any real price data.
]
# 데이터2
data3x = [
# This repository does not include any real price data.
]


# 날짜와 가격 분리
dates = [datetime.strptime(d, "%Y-%m-%d") for d, _ in data]
prices_1x = [p for _, p in data]
prices_3x = [p for _, p in data3x]

# 시작 값을 기준으로 정규화 (100으로 시작)
base_1x = prices_1x[0]
base_3x = prices_3x[0]
normalized_1x = [p / base_1x * 100 for p in prices_1x]
normalized_3x = [p / base_3x * 100 for p in prices_3x]

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))

line1, = ax.plot(dates, normalized_1x, label="1X (A)", marker='o', color='blue')
line2, = ax.plot(dates, normalized_3x, label="3X (B)", linestyle='-', marker='o', color='red')

# x축 날짜 포맷 설정
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()

plt.title("A vs B Performance (Normalized)")
plt.xlabel("Date")
plt.ylabel("Normalized Price (Base = 100)")
plt.legend()
plt.grid(True)

# 호버 기능 추가
cursor = mplcursors.cursor([line1, line2], hover=True)

@cursor.connect("add")
def on_add(sel):
    index = int(sel.index)
    sel.annotation.set_text(
        f"Date: {dates[index].strftime('%Y-%m-%d')}\n"
        f"1X: {normalized_1x[index]:.2f}\n"
        f"3X: {normalized_3x[index]:.2f}"
    )

plt.show()
