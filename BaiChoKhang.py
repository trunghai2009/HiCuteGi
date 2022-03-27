def GiaiToan():
    S = 0
    user = input()
    listSo = user.split(",")
    # Theo cách viết của t, cái split() ấy thì giữa mỗi số phải ngăn bằng dấu phẩy, m thay bằng dấu khác cũng được 
    # nhưng mỗi số phải ngăn bằng dấu m ghi trong ngoặc đấy
    for x in listSo:
        S = S + x
    ketQua = S / len(listSo)
    print(ketQua)
    # len(listSo) là số lượng phần tử của list listSo