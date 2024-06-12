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