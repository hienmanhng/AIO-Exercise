# câu 1:Cho một list các số nguyên num_list và một sliding window có kích thước size k di
# chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
# đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
# lớn hơn hoặc bằng 1
# Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k=3
# Output: [5, 5, 5, 5, 10, 12, 33,

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]


def slide_k(k):
    for j in range(len(num_list)-2):
        num_list_new = num_list[j:k+j]
        num_list_new.sort(reverse=True)
        print(num_list_new, " ==> ", num_list_new[0])


print(slide_k(3))

# Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
# và value là số lần xuất hiện
# • Input: một từ
# • Output: dictionary đếm số lần các chữ xuất hiện
# • Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]


def count_char(word):
    word = word.replace(' ', '')
    word = word.replace(',', '')
    character_counts = {}
    for char in word.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts


print(count_char('Hello, world'))
