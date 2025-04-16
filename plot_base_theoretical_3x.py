import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import mplcursors

# 예시 데이터 (날짜, 가격)
data = [
#     This repository does not include any real price data.
]

# 날짜 및 가격 분리
dates = [datetime.strptime(date, "%Y-%m-%d") for date, _ in data]
raw_prices = [price for _, price in data]

# 정규화
normalized_prices = [p / raw_prices[0] * 100 for p in raw_prices]

# 이론적 3X 레버리지
prices_3x = [100]
for i in range(1, len(raw_prices)):
    daily_return = (raw_prices[i] / raw_prices[i - 1]) - 1
    prices_3x.append(prices_3x[-1] * (1 + daily_return * 3))

fig, ax = plt.subplots(figsize=(10, 6))
line1, = ax.plot(dates, normalized_prices, label="Normalized QQQ (1X)", color='blue')
line2, = ax.plot(dates, prices_3x, label="Theoretical 3X", color='red', linestyle='--')


ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
fig.autofmt_xdate()

plt.title("Normalized QQQ vs Theoretical 3X Leverage")
plt.xlabel("Date")
plt.ylabel("Performance (Start = 100)")
plt.legend()
plt.grid(True)

# 커서 활성화
cursor = mplcursors.cursor([line1, line2], hover=True)
@cursor.connect("add")
def on_add(sel):
    index = int(sel.index)  # float → int로 명시적 변환
    sel.annotation.set_text(
        f"Date: {dates[index].strftime('%Y-%m-%d')}\n"
        f"1X: {normalized_prices[index]:.2f}\n"
        f"3X: {prices_3x[index]:.2f}"
    )

plt.show()