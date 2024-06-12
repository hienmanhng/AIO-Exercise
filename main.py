# Bài tập số 2 gửi Mentor PTK
# Bài toán yêu cầu tính tiền nhận được khi gửi 1$ trong 1 năm, với lãi suất 1 ngày là 1/365
# sử dụng cấu trúc for loop để thực hiện yêu cầu
def calculate_interest(money, period):
  result = money
  for i in range(period):
    result = result * (1 + 1/period)
  return result
print(calculate_interest(1, 12), calculate_interest(1, 365), calculate_interest(1, 730), sep = " | ")