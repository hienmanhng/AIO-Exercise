import math
import random
# tính can chi, bài tập số 1 gửi mentor


def calculate_can_chi(year):
    # tính can
    if year % 10 == 0:
        can = "Canh"
    elif year % 10 == 1:
        can = "Tân"
    elif year % 10 == 2:
        can = "Nhâm"
    elif year % 10 == 3:
        can = "Quý"
    elif year % 10 == 4:
        can = "Giáp"
    elif year % 10 == 5:
        can = "Ất"
    elif year % 10 == 6:
        can = "Bính"
    elif year % 10 == 7:
        can = "Đinh"
    elif year % 10 == 8:
        can = "Mậu"
    elif year % 10 == 9:
        can = "Kỷ"
    # tính chi
    if year % 12 == 0:
        chi = "Thân"
    elif year % 12 == 1:
        return "Dậu"
    elif year % 12 == 2:
        chi = "Tuất"
    elif year % 12 == 3:
        chi = "Hợi"
    elif year % 12 == 4:
        chi = "Tý"
    elif year % 12 == 5:
        chi = "Sửu"
    elif year % 12 == 6:
        chi = "Dần"
    elif year % 12 == 7:
        chi = "Mão"
    elif year % 12 == 8:
        chi = "Thìn"
    elif year % 12 == 9:
        chi = "Tỵ"
    elif year % 12 == 10:
        chi = "Ngọ"
    elif year % 12 == 11:
        chi = "Mùi"

    print(can, chi)


calculate_can_chi(1990)

# Bài tập số 2 gửi Mentor PTK
# Bài toán yêu cầu tính tiền nhận được khi gửi 1$ trong 1 năm, với lãi suất 1 ngày là 1/365
# sử dụng cấu trúc for loop để thực hiện yêu cầu


def calculate_interest(money, period):
    result = money
    for i in range(period):
        result = result * (1 + 1/period)
    return result


print(calculate_interest(1, 12), calculate_interest(
    1, 365), calculate_interest(1, 730), sep=" | ")


# Bài tập 3 gửi mentor
# dùng phương pháp newton để tính căn bậc 2 cho 1 số dương a, với n là số lần cải thiện xấp xỉ, epsilon = 0.001

def newton_sqrt(a, n, epsilon):
    x = a
    for i in range(n):
        x = x - (x * x - a) / (2 * x)
        if abs(x * x - a) < epsilon:
            return x
    return None


print(newton_sqrt(a=10, n=100, epsilon=0.001))