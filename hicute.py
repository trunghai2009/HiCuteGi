import os
import playsound
import speech_recognition as sr
import sys
import ctypes
import wikipedia
import datetime

import json
import re
import webbrowser
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime, sleep, time
from time import strptime, time
#from datetime import datetime
from gtts import gTTS, tts
from youtube_search import YoutubeSearch
import webbrowser
from selenium import webdriver
import pyowm
from apikey import apikey
from random import randint
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from hicuteUi import Ui_hicuteUi

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

# List câu hỏi trắc nghiệm

# Khởi nghĩa Bà Trưng

list_question_Ba_Trung = ["", "", "", "", ""]

list_question_Ba_Trung[0] = "Mục tiêu quan trọng nhất của cuộc khởi nghĩa Hai Bà Trưng là gì?"
list_question_Ba_Trung[1] = "Lãnh đạo cuộc khởi nghĩa Hai Bà Trưng là ai?"
list_question_Ba_Trung[2] = "Cuộc khởi nghĩa Hai Bà Trưng bùng nổ vào thời gian?"
list_question_Ba_Trung[3] = "Đặc điểm nổi bật nhất về cuộc khởi nghĩa Hai Bà Trưng?"
list_question_Ba_Trung[4] = "Sau khi đánh đổ ách cai trị nhà Hán, bà Trưng Trắc đã đóng đô ở đâu?"


list_A_Ba_Trung = ["", "", "", "", ""]

list_A_Ba_Trung[0] = "Lật đổ ách cai trị của nhà Hán"
list_A_Ba_Trung[1] = "Lý Bí"
list_A_Ba_Trung[2] = "Mùa xuân năm 42"
list_A_Ba_Trung[3] = "Mở ra một thời kỳ độc lập lâu dài của dân tộc ta"
list_A_Ba_Trung[4] = "Huyện Mê Linh (Hà Nội)"


list_B_Ba_Trung = ["", "", "", "", ""]

list_B_Ba_Trung[0] = "Trả thù cho Thi Sách"
list_B_Ba_Trung[1] = "Trưng Trắc, Trưng Nhị"
list_B_Ba_Trung[2] = "Mùa đông năm 40"
list_B_Ba_Trung[3] = "Khẳng định vai trò và vị trí của người phụ nữ trong lịch sử"
list_B_Ba_Trung[4] = "Luy Lâu"


list_C_Ba_Trung = ["", "", "", "", ""]

list_C_Ba_Trung[0] = "Trả thù riêng"
list_C_Ba_Trung[1] = "Mai Thúc Loan"
list_C_Ba_Trung[2] = "Mùa xuân năm 40"
list_C_Ba_Trung[3] = "Lòng tự tôn dân tộc"
list_C_Ba_Trung[4] = "Thăng Long"

list_D_Ba_Trung = ["", "", "", "", ""]

list_D_Ba_Trung[0] = "Nhà Hán suy yếu"
list_D_Ba_Trung[1] = "Phùng Hưng"
list_D_Ba_Trung[2] = "Mùa xuân năm 43"
list_D_Ba_Trung[3] = "Cuộc khởi nghĩa đầu tiên thời Bắc thuộc do những nữ anh hùng lãnh đạo"
list_D_Ba_Trung[4] = "Hoa Lư"

list_answer_Ba_Trung = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Ba_Trung_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

# Khởi nghĩa Bà Triệu
list_question_Ba_Trieu = ["", "", "", "", ""]

list_question_Ba_Trieu[0] = "Căn cứ của cuộc khởi nghĩa Bà Triệu ở đâu?"
list_question_Ba_Trieu[1] = "Giữa thế kỉ III, ở quận Cửu Chân nổi lên cuộc khởi nghĩa lớn nào? "
list_question_Ba_Trieu[2] = "Cuộc khởi nghĩa Bà Triệu nhằm lật đổ ách cai trị của triều đại nhà nào?"
list_question_Ba_Trieu[3] = "Bà Triệu hi sinh ở địa điểm nào?"
list_question_Ba_Trieu[4] = "Trước thắng lợi của khởi nghĩa Bà Triệu, nhà Ngô cử tướng nào đem quân sang đàn áp?"


list_A_Ba_Trieu = ["", "", "", "", ""]

list_A_Ba_Trieu[0] = "Phú Điền (Hậu Lộc – Thanh Hóa)"
list_A_Ba_Trieu[1] = "Khởi nghĩa Mai Thúc Loan"
list_A_Ba_Trieu[2] = "Nhà Nam Hán"
list_A_Ba_Trieu[3] = "Phú Điền"
list_A_Ba_Trieu[4] = "Tướng Lục Dận đem 6000 quân"

list_B_Ba_Trieu = ["", "", "", "", ""]

list_B_Ba_Trieu[0] = "Cổ Loa (đông anh)"
list_B_Ba_Trieu[1] = "Khởi nghĩa Bà Triệu"
list_B_Ba_Trieu[2] = "Nhà đường"
list_B_Ba_Trieu[3] = "Hát Môn"
list_B_Ba_Trieu[4] = "Tướng Lục Dận đem 5000 quân"

list_C_Ba_Trieu = ["", "", "", "", ""]

list_C_Ba_Trieu[0] = "Mê Linh"
list_C_Ba_Trieu[1] = "Khởi nghĩa Phùng Hưng"
list_C_Ba_Trieu[2] = "Nhà Ngô (Trung Quốc)"
list_C_Ba_Trieu[3] = "Mê Linh"
list_C_Ba_Trieu[4] = "Tướng Lục Rận đem 6000 quân"

list_D_Ba_Trieu = ["", "", "", "", ""]

list_D_Ba_Trieu[0]= "Luy Lâu"
list_D_Ba_Trieu[1] = "Khởi nghĩa Hai Bà Trưng"
list_D_Ba_Trieu[2] = "Nhà Đông Hán"
list_D_Ba_Trieu[3] = "Núi Tùng (Thanh Hóa)"
list_D_Ba_Trieu[4] = "Tướng Lục Rận đem 5000 quân"

list_answer_Ba_Trieu = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Ba_Trieu_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

# Khởi nghĩa Lý Bí

list_question_Li_Bi = ["", "", "", "", ""]

list_question_Li_Bi[0] = "Nhà nước Vạn Xuân được thành lập sau thắng lợi của cuộc khởi nghĩa nào?"
list_question_Li_Bi[1] = "Cuộc khởi nghĩa Lý Bí bùng nổ ở địa điểm nào? "
list_question_Li_Bi[2] = "Nhà nước Vạn Xuân được đóng đô ở đâu?"
list_question_Li_Bi[3] = "Lý Bí phất cờ khởi nghĩa năm bao nhiêu?"
list_question_Li_Bi[4] = "Vì sao Lý Bí phất cờ khởi nghĩa chống lại ách cai trị nhà Lương?"

list_A_Li_Bi = ["", "", "", "", ""]

list_A_Li_Bi[0] = "Khởi nghĩa Lý Bí"
list_A_Li_Bi[1] = "Mê Linh (Vĩnh Phúc)"
list_A_Li_Bi[2] = "Vùng cửa sông Hồng"
list_A_Li_Bi[3] = "Năm 248"
list_A_Li_Bi[4] = "Tại vì nhà Lương thực hiện chính sách cai trị hà khắc, bóc lột tàn bạo nhân dân ta"

list_B_Li_Bi = ["", "", "", "", ""]

list_B_Li_Bi[0] = "Khởi nghĩa Mai Thúc Loan"
list_B_Li_Bi[1] = "Thái Bình (Sơn Tây – Hà Nội)"
list_B_Li_Bi[2] = "Vùng cửa sông Bạch đằng"
list_B_Li_Bi[3] = "Năm 766"
list_B_Li_Bi[4] = "Mong muốn nền độc lập lâu dài cho dân tộc"

list_C_Li_Bi = ["", "", "", "", ""]

list_C_Li_Bi[0] = "Khởi nghĩa Hai Bà Trưng"
list_C_Li_Bi[1] = "Giao Châu"
list_C_Li_Bi[2] = "Vùng cửa sông Tô Lịch"
list_C_Li_Bi[3] = "Năm 713"
list_C_Li_Bi[4] = "Trả thù nhà"

list_D_Li_Bi = ["", "", "", "", ""]

list_D_Li_Bi[0] = "Khởi nghĩa Phùng Hưng"
list_D_Li_Bi[1] = "Tống Bình"
list_D_Li_Bi[2] = "Vùng cửa sông Đuống"
list_D_Li_Bi[3] = "Năm 542"
list_D_Li_Bi[4] = "Trả nợ nước"

list_answer_Li_Bi = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Li_Bi_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

# Khởi nghĩa Mai Thúc Loan

list_question_Mai_Thuc_Loan = ["", "", "", "", ""]

list_question_Mai_Thuc_Loan[0] = "Cuộc khởi nghĩa Mai Thúc Loan chống lại ách cai trị của nhà nào bên Trung Quốc?"
list_question_Mai_Thuc_Loan[1] = "Căn cứ của cuộc khởi nghĩa Mai Thúc Loan ở đâu? "
list_question_Mai_Thuc_Loan[2] = "“Vua Đen” là biệt hiệu nhân dân ta đặt cho nhân vật lịch sử nào?"
list_question_Mai_Thuc_Loan[3] = "Tên gọi nước ta thời thuộc Đường là gì?"
list_question_Mai_Thuc_Loan[4] = "Nguyên nhân trực tiếp dẫn đến sự bùng nổ của cuộc khởi nghĩa Mai Thúc Loan là gì?"

list_A_Mai_Thuc_Loan = ["", "", "", "", ""]

list_A_Mai_Thuc_Loan[0] = "Nhà Đường"
list_A_Mai_Thuc_Loan[1] = "Mê Linh (Vĩnh Phúc)"
list_A_Mai_Thuc_Loan[2] = "Dương Đình Nghệ"
list_A_Mai_Thuc_Loan[3] = "Đại Cồ Việt"
list_A_Mai_Thuc_Loan[4] = "Nhà đường bắt nhân dân ta phải cống nộp vải trong điều kiện khó khăn"

list_B_Mai_Thuc_Loan = ["", "", "", "", ""]

list_B_Mai_Thuc_Loan[0] = "Nhà Nam Hán"
list_B_Mai_Thuc_Loan[1] = "Thành Vạn An (tỉnh Nghệ An)"
list_B_Mai_Thuc_Loan[2] = "Phùng Hưng"
list_B_Mai_Thuc_Loan[3] = "Giao Chỉ"
list_B_Mai_Thuc_Loan[4] = "Mong muốn nền độc lập lâu dài cho dân tộc"

list_C_Mai_Thuc_Loan = ["", "", "", "", ""]

list_C_Mai_Thuc_Loan[0] = "Nhà Lương"
list_C_Mai_Thuc_Loan[1] = "Đường Lâm"
list_C_Mai_Thuc_Loan[2] = "Mai Thúc Loan"
list_C_Mai_Thuc_Loan[3] = "Nước Vạn Xuân"
list_C_Mai_Thuc_Loan[4] = "Trả thù riêng"

list_D_Mai_Thuc_Loan = ["", "", "", "", ""]

list_D_Mai_Thuc_Loan[0] = "Nhà Ngô"
list_D_Mai_Thuc_Loan[1] = "Giao Châu"
list_D_Mai_Thuc_Loan[2] = "Lý Bí"
list_D_Mai_Thuc_Loan[3] = "An Nam đô hộ phủ"
list_D_Mai_Thuc_Loan[4] = "Nhà đường suy yếu"

list_answer_Mai_Thuc_Loan = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Mai_Thuc_Loan_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

# Khởi nghĩa Phùng Hưng

list_question_Phung_Hung = ["", "", "", "", ""]

list_question_Phung_Hung[0] = "“Bố Cái Đại Vương” là biệt hiệu nhân dân ta đặt cho nhân vật lịch sử nào?"
list_question_Phung_Hung[1] = "Phùng Hưng phất cờ khởi nghĩa ở đâu? "
list_question_Phung_Hung[2] = "Vì sao cuộc khởi nghĩa Phùng Hưng được mọi người hưởng ứng?"
list_question_Phung_Hung[3] = "Dưới ách cai trị của nhà Đường, những cuộc khởi nghĩa lớn nào đã diễn ra?"
list_question_Phung_Hung[4] = "Khi Phùng Hưng khởi nghĩa, viên đô hộ người Hán tên là gì?"

list_A_Phung_Hung = ["", "", "", "", ""]

list_A_Phung_Hung[0] = "Phùng Hưng"
list_A_Phung_Hung[1] = "Mê Linh (Vĩnh Phúc)"
list_A_Phung_Hung[2] = "Vì nhân dân căm thù bọn cướp nước"
list_A_Phung_Hung[3] = "Khởi nghĩa của Dương Đình Nghệ"
list_A_Phung_Hung[4] = "Cao Chính Bình"

list_B_Phung_Hung = ["", "", "", "", ""]

list_B_Phung_Hung[0] = "Mai Thúc Loan"
list_B_Phung_Hung[1] = "Đường Lâm"
list_B_Phung_Hung[2] = "Vì cuộc sống nhân dân rất cùng quẫn"
list_B_Phung_Hung[3] = "Khởi nghĩa Mai Thúc Loan"
list_B_Phung_Hung[4] = "Tống Chính Bình"

list_C_Phung_Hung = ["", "", "", "", ""]

list_C_Phung_Hung[0] = "Lý Bí"
list_C_Phung_Hung[1] = "Thành Vạn An (Nghệ An)"
list_C_Phung_Hung[2] = "Vì Phùng Hưng là người có uy tín và nhân dân rất căm phẫn chính sách cai trị của nhà Đường, sẵn sàng nổi dậy đấu tranh"
list_C_Phung_Hung[3] = "Khởi nghĩa Lý Bí"
list_C_Phung_Hung[4] = "Tống Cao Bình"

list_D_Phung_Hung = ["", "", "", "", ""]

list_D_Phung_Hung[0] = "Triệu Quang Phục"
list_D_Phung_Hung[1] = "Cửu Châu"
list_D_Phung_Hung[2] = "Vì Phùng Hưng đã thu phục được lòng dân"
list_D_Phung_Hung[3] = "Khởi nghĩa Phùng Hưng và khởi nghĩa Mai Thúc Loan"
list_D_Phung_Hung[4] = "Cao Tống Bình"

list_answer_Phung_Hung = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Phung_Hung_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']
# Ngô Quyền và chiến thắng Bạch đằng

list_question_Ngo_Quyen = ["", "", "", "", ""]

list_question_Ngo_Quyen[0] = "Trận đánh trên sông Bạch Đằng (năm 938) diễn ra trong thời gian bao lâu?"
list_question_Ngo_Quyen[1] = "Ngô Quyền chuẩn bị đánh quân xâm lược Nam Hán lần 2 như thế nào? "
list_question_Ngo_Quyen[2] = "Ngô Quyền sử dụng chiến thuật nào để đối phó với quân xâm lược Nam Hán trên sông Bạch Đằng năm 938?"
list_question_Ngo_Quyen[3] = "Chỉ ra điểm độc đáo trong kế hoạch đánh giặc của Ngô Quyền?"
list_question_Ngo_Quyen[4] = "Tên gọi khác của sông Bạch Đằng là gì?"

list_A_Ngo_Quyen = ["", "", "", "", ""]

list_A_Ngo_Quyen[0] = "Một ngày"
list_A_Ngo_Quyen[1] = "Tiêu hao quân địch"
list_A_Ngo_Quyen[2] = "Phóng hỏa tiễn đốt thuyền địch"
list_A_Ngo_Quyen[3] = "Vũ khí hiện đại"
list_A_Ngo_Quyen[4] = "Sông Rừng"

list_B_Ngo_Quyen = ["", "", "", "", ""]

list_B_Ngo_Quyen[0] = "Hai ngày"
list_B_Ngo_Quyen[1] = "Xây dựng trận địa cọc ngầm dưới đáy sông Bạch Đằng"
list_B_Ngo_Quyen[2] = "Mai phục"
list_B_Ngo_Quyen[3] = "Dồn toàn lực tổng tiến công"
list_B_Ngo_Quyen[4] = "Sông Đáy"

list_C_Ngo_Quyen = ["", "", "", "", ""]

list_C_Ngo_Quyen[0] = "Ba ngày"
list_C_Ngo_Quyen[1] = "Hạn chế sức mạnh quân thù"
list_C_Ngo_Quyen[2] = "Kết hợp mai phục và đánh nhử"
list_C_Ngo_Quyen[3] = "Kết hợp mai phục và tiêu hao quân địch"
list_C_Ngo_Quyen[4] = "Sông Mã"

list_D_Ngo_Quyen = ["", "", "", "", ""]

list_D_Ngo_Quyen[0] = "Một tuần"
list_D_Ngo_Quyen[1] = "Mai phục, tấn công bất ngờ"
list_D_Ngo_Quyen[2] = "Lợi dụng địa thế hiểm trở trong rừng để tiêu diệt địch"
list_D_Ngo_Quyen[3] = "Lợi dụng thủy triều lên xuống làm trận địa cọc ngầm"
list_D_Ngo_Quyen[4] = "Sông Lâu"

list_answer_Ngo_Quyen = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Ngo_Quyen_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']
# Nhà nước Chăm pa

list_question_Cham_pa = ["", "", "", "", ""]

list_question_Cham_pa[0] = "Vua Lâm ẤP sau khi hợp nhất các bộ lạc đã đổi tên nước là?"
list_question_Cham_pa[1] = "Kinh đô nước Chăm pa ở đâu? "
list_question_Cham_pa[2] = "Người Chăm pa sống chủ yếu dựa vào?"
list_question_Cham_pa[3] = "Chữ viết của người Chăm bắt nguồn từ đâu?"
list_question_Cham_pa[4] = "Di sản của người Chăm pa còn tồn tại đến ngày nay?"

list_A_Cham_pa = ["", "", "", "", ""]

list_A_Cham_pa[0] = "Chăm pa"
list_A_Cham_pa[1] = "Hội An - Quảng Nam"
list_A_Cham_pa[2] = "Khai thác lâm thổ sản, làm đồ gốm"
list_A_Cham_pa[3] = "Chữ La tinh"
list_A_Cham_pa[4] = "Thánh địa Mỹ Sơn"

list_B_Cham_pa = ["", "", "", "", ""]

list_B_Cham_pa[0] = "Văn Lang"
list_B_Cham_pa[1] = "Trà Kiệu - Quảng Nam"
list_B_Cham_pa[2] = "Đánh bắt cá"
list_B_Cham_pa[3] = "Chữ Hán"
list_B_Cham_pa[4] = "Cầu Trường Tiền"

list_C_Cham_pa = ["", "", "", "", ""]

list_C_Cham_pa[0] = "Phù Nam"
list_C_Cham_pa[1] = "Sa Huỳnh - Quảng Ngãi"
list_C_Cham_pa[2] = "Nghề nông trồng lúa nước, 1 năm hai vụ"
list_C_Cham_pa[3] = "Chữ Nôm"
list_C_Cham_pa[4] = "Chùa Tây Phương"

list_D_Cham_pa = ["", "", "", "", ""]

list_D_Cham_pa[0] = "Âu Lạc"
list_D_Cham_pa[1] = "Tượng Lâm - Quảng Nam"
list_D_Cham_pa[2] = "Trồng trọt và chăn nuôi (trâu, bò, lợn, gà...)"
list_D_Cham_pa[3] = "Chữ Phạn"
list_D_Cham_pa[4] = "Chùa Một Cột"

list_answer_Cham_pa = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Cham_pa_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

# Cai trị phương bắc

list_question_Cai_tri = ["", "", "", "", ""]

list_question_Cai_tri[0] = "Nhà Hán cho người Hán ở lẫn với người Việt, bắt dân ta theo phong tục tập quán của họ nhằm âm mưu gì?"
list_question_Cai_tri[1] = "Loại thuế bị các triều đại phương Bắc đánh nặng nhất là gì? "
list_question_Cai_tri[2] = "Các triều đại phương Bắc cho người Hán nắm quyền cai trị nước ta đến cấp Huyện nhằm mục đích gì?"
list_question_Cai_tri[3] = "Trong sách Nam phương thảo mộc trạng có nói đến kĩ thuật trồng cam đặc biệt của người Việt. Đó là kĩ thuật gì?"
list_question_Cai_tri[4] = "Từ thế kỉ III khi làm gốm, người Việt đã áp dụng thêm kĩ thuật gì?"

list_A_Cai_tri = ["", "", "", "", ""]

list_A_Cai_tri[0] = "Đồng hóa dân tộc ta"
list_A_Cai_tri[1] = "Thuế muối"
list_A_Cai_tri[2] = "Để dễ thống trị, sai khiến"
list_A_Cai_tri[3] = "Dùng côn trùng thụ phấn"
list_A_Cai_tri[4] = "Tráng men và trang trí hoa văn"

list_B_Cai_tri = ["", "", "", "", ""]

list_B_Cai_tri[0] = "Sát nhập nước ta vào Trung Quốc"
list_B_Cai_tri[1] = "Thuế muối và thuế sắt"
list_B_Cai_tri[2] = "Đồng hóa dân tộc ta"
list_B_Cai_tri[3] = "Ươm cây"
list_B_Cai_tri[4] = "Trang trí hoa văn"

list_C_Cai_tri = ["", "", "", "", ""]

list_C_Cai_tri[0] = "Nô dịch dân tộc ta"
list_C_Cai_tri[1] = "Thuế sắt"
list_C_Cai_tri[2] = "Thắt chặt bộ máy cai trị và hạn chế các cuộc nổi dậy của nhân dân ta"
list_C_Cai_tri[3] = "Chiết cành"
list_C_Cai_tri[4] = "Nung luyện"

list_D_Cai_tri = ["", "", "", "", ""]

list_D_Cai_tri[0] = "Hạn chế chống đối của dân tộc ta"
list_D_Cai_tri[1] = "Thuế nông nghiệp"
list_D_Cai_tri[2] = "Vơ vét của cải"
list_D_Cai_tri[3] = "Dùng côn trùng diệt côn trùng"
list_D_Cai_tri[4] = "Men rạn"

list_answer_Cai_tri = ['đáp án a', 'đáp án b', 'đáp án c', 'đáp án d', 'đáp án a']
list_answer_Cai_tri_2 = ['phương án a', 'phương án b', 'phương án c', 'phương án d', 'phương án a']

can_on_tap = []

def speakers(word):
        
    print("HiCute: {}".format(word))
    tts = gTTS(text=word, lang='vi', slow=False)
    sound = "sound.mp3"
    tts.save(sound)
    playsound.playsound(sound, False)
    os.remove(sound)
    # Lập trình cho nó nói được

def ear():
        
    hear = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: ", end=' ')
        audio = hear.listen (source, phrase_time_limit=6)
        # Nhận dạng để nghe người nói
        try:
            text = hear.recognize_google(audio, language="vi")
            print(text)
            return text
        except Exception:
            print("...")
            return 0
            # Thử âm thanh, nếu lỗi thì return 0

def stop():
        
    speakers("Hẹn gặp lại bạn sau nhé!")
    sleep(3)
    raise SystemExit
    # Để khi nó nghe không được lần N, nó sẽ tắt
    
def get_text():
    
    for count in range(3):
        text = ear()
        if text:
            return text.lower()
        elif count < 5:
            speakers("Tôi không nghe rõ, bạn nói lại đi")
        # Ko nghe rõ 3 lần = Tự tắt 
    sleep(4)
    stop()
    return 0
 
       # chrome_driver_manager()

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        speakers("Chào bạn, bạn cần giúp gì?")
        sleep(0.25)
        self.TaskExecution()
    
    def test(self):    
        speakers("Hãy kiểm tra lại một chút xem bạn ôn tập tốt chưa nhé")
        sleep(3)
        diem = 100
        for chon_chu_de in range(1, 9):
            
            cau_so = randint(0, 4)
            if chon_chu_de == 1:
                
                speakers((str(list_question_Ba_Trung[cau_so] + "\n" + "A " + list_A_Ba_Trung[cau_so] + "\n" + "B " + list_B_Ba_Trung[cau_so] + "\n" + "C " + list_C_Ba_Trung[cau_so] + "\n" + "D " + list_D_Ba_Trung[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(25)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Ba_Trung[cau_so]) in answer) or (str(list_answer_Ba_Trung_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn đã ôn tập tốt")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Hai Bà Trưng nhé!")
                    diem = diem - 12.5
                    sleep(4)
                #raise SystemExit
            
            elif chon_chu_de == 2:
            
                speakers((str(list_question_Ba_Trieu[cau_so] + "\n" + "A " + list_A_Ba_Trieu[cau_so] + "\n" + "B " + list_B_Ba_Trieu[cau_so] + "\n" + "C " + list_C_Ba_Trieu[cau_so] + "\n" + "D " + list_D_Ba_Trieu[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(25)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Ba_Trieu[cau_so]) in answer) or (str(list_answer_Ba_Trieu_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn đã ôn tập tốt")
                    sleep(2)
                
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Bà Triệu nhé!")
                    diem = diem - 12.5
                    sleep(4)
                    
                                
            elif chon_chu_de == 3:
                speakers((str(list_question_Li_Bi[cau_so] + "\n" + "A " + list_A_Li_Bi[cau_so] + "\n" + "B " + list_B_Li_Bi[cau_so] + "\n" + "C " + list_C_Li_Bi[cau_so] + "\n" + "D " + list_D_Li_Bi[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(25)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Li_Bi[cau_so]) in answer) or (str(list_answer_Li_Bi_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn đã ôn tập tốt")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Lí Bí nhé!")
                    diem = diem - 12.5
                    sleep(4)
                    
            elif chon_chu_de == 4:
                speakers((str(list_question_Mai_Thuc_Loan[cau_so] + "\n" + "A " + list_A_Mai_Thuc_Loan[cau_so] + "\n" + "B " + list_B_Mai_Thuc_Loan[cau_so] + "\n" + "C " + list_C_Mai_Thuc_Loan[cau_so] + "\n" + "D " + list_D_Mai_Thuc_Loan[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(30)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Mai_Thuc_Loan[cau_so]) in answer) or (str(list_answer_Mai_Thuc_Loan_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn đã ôn tập tốt")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Mai Thúc Loan nhé!")
                    diem = diem - 12.5
                    sleep(4)
            elif chon_chu_de == 5:
                speakers((str(list_question_Phung_Hung[cau_so] + "\n" + "A " + list_A_Phung_Hung[cau_so] + "\n" + "B " + list_B_Phung_Hung[cau_so] + "\n" + "C " + list_C_Phung_Hung[cau_so] + "\n" + "D " + list_D_Phung_Hung[cau_so]+ "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(35)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Phung_Hung[cau_so]) in answer) or (str(list_answer_Phung_Hung_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn giỏi quá")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Phùng Hưng nhé!")
                    sleep(4)
                    diem = diem - 12.5     
            
            elif chon_chu_de == 6:
                speakers((str(list_question_Ngo_Quyen[cau_so] + "\n" + "A " + list_A_Ngo_Quyen[cau_so] + "\n" + "B " + list_B_Ngo_Quyen[cau_so] + "\n" + "C " + list_C_Ngo_Quyen[cau_so] + "\n" + "D " + list_D_Ngo_Quyen[cau_so]+ "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(30)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Ngo_Quyen[cau_so]) in answer) or (str(list_answer_Ngo_Quyen_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn giỏi quá")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề Ngô Quyền nhé!")
                    sleep(4)
                    diem = diem - 12.5

            elif chon_chu_de == 7:
                speakers((str(list_question_Cai_tri[cau_so] + "\n" + "A " + list_A_Cai_tri[cau_so] + "\n" + "B " + list_B_Cai_tri[cau_so] + "\n" + "C " + list_C_Cai_tri[cau_so] + "\n" + "D " + list_D_Cai_tri[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(35)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Cai_tri[cau_so]) in answer) or (str(list_answer_Cai_tri_2[cau_so]) in answer):
                    speakers("Đúng rồi, bạn đã làm rất tốt")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề chính sách cai trị thời kỳ bắc thuộc nhé!")
                    sleep(6)
                    diem = diem - 12.5        
            
            elif chon_chu_de == 8:
                speakers((str(list_question_Cham_pa[cau_so] + "\n" + "A " + list_A_Cham_pa[cau_so] + "\n" + "B " + list_B_Cham_pa[cau_so] + "\n" + "C " + list_C_Cham_pa[cau_so] + "\n" + "D " + list_D_Cham_pa[cau_so] + "\n" + "Thời gian suy nghĩ là 20 giây.")))
                sleep(30)
                speakers("Mời bạn trả lời")
                sleep(1)
                answer = str(get_text())
                if ('đề' in answer) or ('đê' in answer):
                    answer = 'phương án d'
                if (str(list_answer_Cham_pa[cau_so]) in answer) or (str(list_answer_Cham_pa_2[cau_so]) in answer):
                    speakers("Đúng rồi đó, chúc mừng bạn")
                    sleep(2)
                else:
                    speakers("Bạn cần ôn tập lại về chủ đề nhà nước Chăm pa nhé!")
                    sleep(5)
                    diem = diem - 12.5

        speakers("Tổng điểm bạn đạt được là: " + str(diem))
        sleep(5)
        if diem > 80:
            speakers("Chúc mừng bạn, bạn đã được trên 8 điểm.")
            sleep(4)
        elif (diem >= 50) and (diem <= 80):
            speakers("Bạn làm khá tốt.")
            sleep(2.5)
        else:
            speakers("Bạn cần cố gắng ôn tập hơn nhé. Bạn có số điểm dưới trung bình.")
            sleep(6)
    
    def TaskExecution(self):
        file = 'Ngay.txt'
        now = datetime.datetime.now()
        today = datetime.datetime.today()
        # d0 = datetime.strftime(now, '%d/%m/%Y')
        d0_obj = datetime.datetime.strftime(today, '%Y/%m/%d') #không có giờ phút giây
        
        f = open(file, 'r')
        a = f.read()
        f.close()

        f = open(file, 'w+')
        f.write(d0_obj)
        f.close()

        a = datetime.datetime.strptime(a, "%Y/%m/%d")
        d0 = datetime.datetime.strptime(d0_obj,'%Y/%m/%d') #có định dạng giờ phút giây
        different = (d0 - a).days
        if different >= 3:
            print("Sao bạn đã ", different, "ngày không học vậy?")
            print("Bạn cầm chăm học hơn nhé!")
        text = get_text()
        sleep(2)
        while True:
                
            def cham_pa():
                speakers("Bạn muốn học theo cách nào: flashcards, sơ đồ tư duy hay chơi trò chơi củng cố kiến thức")
                sleep(5)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    speakers("OK, tôi mở đây")
                    sleep(2)
                    webbrowser.open('https://drive.google.com/file/d/1onw4-HsOEFaUVcct0-5Wq0AE6p1Y3W4K/view?usp=sharing')
                    speakers("""Nước Chăm - Pa từ thế kỉ 2 đến thế kỉ 10:
                                Sự thành lập: Thế kỉ 2, Khu Liên thành lập nước Lâm Ấp.
                                Các vua Lâm Ấp mở rộng lãnh thổ, đổi tên nước thành Chăm - pa.
                                Kinh đô là Trà Kiệu (Quảng Nam). Tình hình kinh tế: Nông nghiệp trồng lúa nước, ruộng bậc thang.
                                Ngư nghiệp: Nghề đánh cá phát triển. Thương nghiệp: Buôn bán với các quận Giao Châu, Trung Quốc, Ấn Độ.
                                Tình hình văn hóa: Tôn giáo đạo Phật, đạo bà La Môn phát triển. Chữ viết bắt nguồn từ chữ Phạn
                                Kiến trúc: tháp Chăm, đền, tượng, các bức chạm nổi...""")
                    sleep(50)
                    speakers ("Có một số video liên quan, bạn có muốn xem không?")
                    sleep(3)
                    while True:
                        answer = get_text()
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            speakers("OK")
                            sleep(1)
                            thu_tu_video = randint(1, 2)
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=X8bTB1Cszx4'
                            elif thu_tu_video == 2:
                                videourl = 'https://www.youtube.com/watch?v=cQoIrEOicq0'
                            webbrowser.open(videourl)
                            
                        else:
                            speakers("Tốt thôi, tôi sẽ mở wikipedia, bạn tự tra cứu tham khảo nhé")    
                            sleep(6)
                            webbrowser.open('https://vi.wikipedia.org/wiki/Ch%C4%83m_Pa')
                            raise SystemExit
                elif ("chơi" in answer):
                    speakers("Chúc bạn chơi thật vui vẻ. Chơi xong nhớ ôn lại kiến thức nha bạn yêu.")
                    sleep(7)
                    webbrowser.open('https://quizizz.com/join/quiz/60be39f023aa83001b9cee2a/start?studentShare=true')
                    raise SystemExit
                else:
                    speakers("Được rồi nhé, HiCute chúc bạn ôn luyện hiệu quả")
                    sleep(5)
                    webbrowser.open('https://quizlet.com/_9xc4aq?x=1qqt&i=3n2y41')
                    raise SystemExit
            
            def cai_tri_bac_thuoc():
                speakers("Bạn muốn học theo cách nào: flashcards, sơ đồ tư duy hay chơi trò chơi củng cố kiến thức")
                sleep(5)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    speakers("OK, tôi mở đây")
                    sleep(3)
                    webbrowser.open('https://drive.google.com/file/d/1ZGUW_QbeE8eYF3d_LEKerhE1TmJVDMNv/view?usp=sharing')
                    speakers("""Chính sách cai trị của các triều đại phương Bắc thể hiện ở các điểm sau:
                    Về văn hóa: Tăng cường đưa người Hán sang ở cùng với người Việt; buộc dân ta phải học chữ Hán và tiếng Hán;
                    bắt dân ta phải tuân theo luật pháp và phong tục của người Hán.
                    Về kinh tế: Đánh nhiều thứ thuế, đặc biệt là thuế muối và thuế sắt; bắt dân ta phải cống nạp các sản vật quý (sừng tê giác, ngà voi, vàng bạc... .)
                    Về chính trị: Chia nước ta thành các Quận, sáp nhập vào lãnh thổ Trung Quốc; đưa người Hán sang cai trị tới cấp Huyện để siết chặt ách cai trị.""")
                    sleep(41)
                    speakers ("Có một số video liên quan, bạn có muốn xem không?")
                    sleep(3)
                    while True:
                        answer = get_text()
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            speakers("OK")
                            sleep(1)
                            thu_tu_video = randint(1, 2)
                            if thu_tu_video == 1:
                                videourl = 'https://drive.google.com/file/d/1UOoTff5UAW581lbQF57KnKvDs5Yo4wxi/view?usp=sharing'
                            elif thu_tu_video == 2:
                                videourl = 'https://drive.google.com/file/d/1wVusiqoVQ0b6kAnuIICUtwwmFIRyweg5/view?usp=sharing'
                            webbrowser.open(videourl)
                            
                        else:
                            speakers("Tốt thôi, tôi sẽ mở wikipedia, bạn tự tra tham khảo cứu nhé")    
                            sleep(6)
                            webbrowser.open('https://vi.wikipedia.org/wiki/B%E1%BA%AFc_thu%E1%BB%99c#:~:text=B%E1%BA%AFc%20thu%E1%BB%99c%20ch%E1%BB%89%20th%E1%BB%9Di%20k%E1%BB%B3,thu%E1%BB%99c%20%C4%91%E1%BB%8Ba%20c%E1%BB%A7a%20Trung%20Qu%E1%BB%91c.&text=Theo%20t%C3%A1c%20gi%E1%BA%A3%20Tr%E1%BA%A7n%20Tr%E1%BB%8Dng,%3A%20905%2C%20938%2C%20931.')
                        raise SystemExit
                elif ("chơi" in answer):
                    speakers("Chúc bạn chơi thật vui vẻ. Chơi xong nhớ ôn lại kiến thức nha bạn yêu.")
                    sleep(8)
                    webbrowser.open('https://quizizz.com/join/quiz/60bcb685e9113f001b1b9af3/start?studentShare=true')
                    raise SystemExit
                else:
                    speakers("Được rồi nhé, HiCute chúc bạn ôn luyện hiệu quả")
                    sleep(5)
                    webbrowser.open('https://quizlet.com/vn/599917724/chinh-sach-cai-tri-cua-cac-trieu-dai-phuong-bac-flash-cards/?x=1jqt')
                    raise SystemExit

            def maithucloan():
                speakers("Bạn muốn học theo cách nào: flashcards, sơ đồ tư duy hay chơi trò chơi củng cố kiến thức")
                sleep(6)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    speakers("OK, tôi mở đây")
                    sleep(3)
                    webbrowser.open('https://drive.google.com/file/d/17go5PHTfHK4YP388YATqG7Q7gBdaecDH/view?usp=sharing')
                    speakers("Khởi nghĩa Mai Thúc Loan đầu thế kỉ 8: Nguyên nhân sâu xa là do sự cai trị hà khắc của nhà Đường, nguyên nhân trực tiếp là nạn cống nộp sản vật cho nhà Đường. Lãnh đạo cuộc khởi nghĩa là Mai Thúc Loan. Diễn biến cuộc khởi nghĩa như sau: Đầu thế kỉ 8 (năm 713), cuộc khởi nghĩa bùng nổ, làm chủ Hoan Châu, nghĩa quân tiến đánh thành Tống Bình, quan đô hộ bỏ chạy về Trung Quốc. Năm 722, nhà Đường đem quân sang đàn áp. Kết quả: cuộc hởi nghĩa thất bại. Ý nghĩa: thể hiện tinh thần đấu tranh kiên cường của nhân dân ta.")
                    sleep(42)
                    speakers ("Có một số video liên quan, bạn có muốn xem không?")
                    sleep(3)
                    while True:
                        answer = get_text()
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer) or ('được' in answer):
                            speakers("OK")
                            sleep(1)
                            thu_tu_video = randint(1, 4)
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=NLgrtzVwRg4'
                            elif thu_tu_video == 2:
                                videourl = 'https://youtu.be/BLq8JVkSsEI'
                            elif thu_tu_video == 3:
                                videourl = 'https://youtu.be/BF9RPtDkrcs'
                            webbrowser.open(videourl)
                            
                        else:
                            speakers("Tốt thôi, tôi sẽ mở wikipedia, bạn tự tra cứu tham khảo nhé")    
                            sleep(6)
                            webbrowser.open('https://vi.wikipedia.org/wiki/Mai_H%E1%BA%AFc_%C4%90%E1%BA%BF')
                            raise SystemExit
                elif ("chơi" in answer):
                    speakers("Mời bạn. Chơi xong nhớ ôn lại kiến thức nhé.")
                    sleep(3)
                    webbrowser.open('https://quizizz.com/join/quiz/60bdbff8709528001b5c7ae5/start?studentShare=true')
                    raise SystemExit
                else:
                    speakers("Được rồi nhé, HiCute chúc bạn ôn luyện hiệu quả")
                    sleep(3)
                    webbrowser.open('https://quizlet.com/vn/599891525/khoi-nghia-mai-thuc-loan-flash-cards/?x=1jqt')
                    raise SystemExit
            
            def wikipedia_searching_info(texting):
                while True:
                    try:
                        content = wikipedia.page(texting)
                        webbrowser.open(content.url)
                        raise SystemExit
                    except Exception:
                        speakers("Không tìm thấy dữ liệu mà bạn yêu cầu trên wikipedia, bạn hãy nói lại")
                        sleep(4.75)
                                
            def li_bi():
                speakers("Bạn muốn học theo cách nào: Flashcards, trò chơi hay sơ đồ tư duy?")
                sleep(3)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    speakers("OK, tôi mở đây")
                    sleep(2)
                    webbrowser.open('https://drive.google.com/file/d/1waecLRhAsSX9sc_ccfYas5oldNEfipRd/view?usp=sharing')
                    speakers("""Khởi nghĩa Lí Bí: Nguyên nhân: Chính sách cai trị tàn bạo của nhà Lương
                                    Lãnh đạo: Lí Bí. Diễn biến: Năm 542, Lí Bí dựng cờ khởi nghĩa tại Thái Bình (Sơn Tây)
                                    Nghĩa quân giải phóng được thành Long Biên, Hoàng Châu. Kết quả: thắng lợi
                                    Nhà nước Vạn Xuân được thành lập. Ý nghĩa: Thể hiện tinh thần yêu nước, quyết tâm giành độc lập """)
                    sleep(30)
                
                    speakers("Có một số video bạn có muốn xem không?")
                    sleep(3)
                    while True:
                        answer = str(get_text())
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer) or ('được' in answer):
                            videourl = ''
                            def playvideo():
                                webbrowser.open(videourl)
                            speakers("OK, bạn xem nhé.")
                            sleep(3)
                            thu_tu_video = randint(1, 2)
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=ASY1zlmuVRs'
                                playvideo()
                                
                            else:
                                videourl = 'https://www.youtube.com/watch?v=dXDgkVejqZY'
                                playvideo()
                            raise SystemExit
                        else:  
                            speakers("Bạn có muốn biết thêm thông tin chi tiết hơn không?")
                            sleep(3)
                            boolean = get_text()
                            if ("có" in boolean) or ("ok" in boolean) or ("ờ" in boolean) or ("đồng ý" in boolean) or ('mở đi' in boolean) or ("muốn" in boolean):
                                speakers("OK, tôi mở đây")     
                                sleep(3)                   
                                webbrowser.open('https://vi.wikipedia.org/wiki/L%C3%BD_Nam_%C4%90%E1%BA%BF')

                            else:
                                speakers("OK, tạm biệt bạn")
                        
                        raise SystemExit
                        
                elif ("chơi" in answer):
                    speakers("Được bạn, gì chứ việc đấy HiCute luôn sẵn sàng")
                    sleep(5)
                    webbrowser.open('https://quizizz.com/join/quiz/60bdc82f056828001cdabc56/start?studentShare=true')
                else:
                    speakers("OK, tôi mở đây bạn.")
                    sleep(3)
                    webbrowser.open('https://quizlet.com/vn/599891338/khoi-nghia-li-bi-flash-cards/')
            
            def change_wallpaper():
                api_key = 'KOr5qDqDVfhGqefpfnZpRVbBhyOXSv1KkiIP_Me9RbM'
                url_unsplash = 'https://api.unsplash.com/photos/random?client_id=' + \
                    api_key # pic from unsplash.com
                f = urllib2.urlopen(url_unsplash)
                json_string = f.read()
                f.close()
                parsed_json = json.loads(json_string)
                photos = parsed_json['urls']['full']
                # Đặt nơi down ảnh về
                urllib2.urlretrieve(photos, 'C:/Users//MTH/OneDrive - VICEM/Pictures/WallpaperUnsplash.png')
                images=os.path.join('C:/Users/MTH/OneDrive - VICEM/Pictures/WallpaperUnsplash.png')
                ctypes.windll.user32.SystemParametersInfoW(20, 0, images,3)
                speakers('Hình nền máy tính vừa được thay đổi')
                self.TaskExecution()
            
            def time():
                speakers("Bây giờ là %d giờ %d phút" % (now.hour, now.minute))
                sleep(3)
            
            def day():
                speakers("Hôm nay là ngày %d tháng %d năm %d" %(now.day, now.month, now.year))
                sleep(4.5)
            
            def open_chrome():
                speakers("OK")
                sleep(0.25)
                os.startfile('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
                raise SystemExit
                                         
            def weather():
                speakers("Bạn muốn nghe thời tiết ở đâu")
                url = "http://api.openweathermap.org/data/2.5/weather?"
                city = get_text()
                apikey = "be046d33195a73eac4be3f676ccde08a"
                call_url = url + "appid=" + apikey + "&q=" + city + "&units=metric"
                response = requests.get(call_url)
                data = response.json()
                if data["cod"] != "404":
                    city_response = data["main"]
                    current_temp = city_response["temp"]
                    current_pressure = city_response["pressure"]
                    current_humidity = city_response["humidity"]
                    suntime = data["sys"]
                    sunrise = datetime.datetime.fromtimestamp(suntime['sunrise'])
                    sunset = datetime.datetime.fromtimestamp(suntime['sunset'])
                    now = datetime.datetime.now()
                    content = """ Hôm nay là ngày {day} tháng {month} năm {year}
                    Mặt trời mọc vào {hourrise} giờ {minrise} phút
                    Mặt trời lặn vào {hourset} giờ {minset} phút
                    Nhiệt độ trung bình là {temp} độ C
                    Áp suất không khí là {pressure} Hecto Pascal
                    Độ ẩm là {humidity}%""".format(day = now.day, month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                        hourset = sunset.hour, minset = sunset.minute, temp = current_temp, pressure = current_pressure, 
                                                        humidity = current_humidity)
                    speakers(content)
                    sleep(23.5)
                else:
                    speakers("Tôi không tìm thấy địa chỉ của bạn")
                                
            def play_sound_on_youtube():
                speakers("Bạn thích nghe bài nào?")
                song = get_text()
                while True:
                    result = YoutubeSearch(song, max_results=10).to_dict()
                    if result:
                        break
                urlsong = 'https://www.youtube.com' + result[0]['url_suffix']
                webbrowser.open(urlsong)
                speakers("Bài hát bạn yêu cầu đã được mở")
                raise SystemExit
                
            def googling(texting):
                search_for = texting.split('kiếm', 1)[0]
                driver = webdriver.Chrome(path)
                driver.get('https://www.google.com')
                query = driver.find_element_by_xpath("//input[@name='q']")
                query.send_keys(str(search_for))
                query.send_keys(Keys.RETURN)
                sleep(3600)
                raise SystemExit
            
            def read_news():
                speakers("Bạn muốn đọc báo về gì")
                    
                queue = get_text()
                params = {
                    'apiKey': 'cec0814031bf4868ae05579227d3b834',
                    "q": queue,
                }
                api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
                api_response = api_result.json()
                print("Tin tức")

                for number, result in enumerate(api_response['articles'], start=1):
                    print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
                """)
                    if number <= 3:
                        webbrowser.open(result['url'])
                raise SystemExit
                
            def phung_hung():
                speakers("Bạn thích Flashcards, sơ đồ tư duy hay chơi trò chơi nhỉ bạn học đáng yêu?")
                sleep(5)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    webbrowser.open('https://drive.google.com/file/d/1OMnaJyJb35mNiJvCTzygBuCoX14YZAcb/view?usp=sharing')
                    speakers("""Khởi nghĩa Phùng Hưng diễn ra từ năm 776 đến 791. Nguyên nhân cuộc khởi nghĩa là do Chính sách cai trị tàn bạo của nhà Đường, nhân dân bất bình đứng lên đấu tranh.
                                Người lãnh đạo là Phùng Hưng, quê quán tại Đường Lâm, Ba Vì, Sơn tây (nay là Hà Nội)
                                Phùng Hưng là người tài năng, trí dũng song toàn (đứng đầu vùng Đường Lâm, sức khỏe phi thường, đã từng đánh hổ...), có xuất thân: Hào trưởng vùng Đường Lâm
                                Diễn biến cuộc khởi nghĩa như sau: Năm 776, Phùng Hưng họp quân khởi nghĩa ở Đường Lâm
                                Sau đó, Phùng Hưng kéo quân về bao vây phủ thành Tống Bình Chiếm được thành, sắp đặt việc cai trị
                                Năm 791, nhà Đường lại đem quân sang đàn áp, Phùng An ra hàng.
                                Kết quả cuộc khởi nghĩa: Giành lại được quyền làm chủ đất nước, sắp đặt việc cai trị trong 25 năm
                                Ý nghĩa cuộc khởi nghĩa: Phản ánh nỗi bất bình của nhân dân ta trước những chính sách tàn bạo của quân xâm lược
                                Thể hiện ý chí quật cường, mong muốn dân tộc được hòa bình, tự do của nhân dân ta""")
                    sleep(82)
                    speakers("Có một vài video hay quá xá cà xa, bạn có muốn xem không")
                    sleep(4)
                    while True:
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            videourl = 'https://'
                            def playvideo():
                                webbrowser.open(videourl)
                            speakers("OK, bạn xem thử đi nhé.")
                            sleep(3)
                            thu_tu_video = randint(1, 2)
                                
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=rb3JveXI-vU'
                                playvideo()
                                
                            else:
                                speakers("Cảnh báo! Video dài nhưng rất thú vị.")
                                sleep(4)
                                videourl = 'https://www.youtube.com/watch?v=JWjgHYbpXAo'
                                playvideo()
                            raise SystemExit
                        else:
                            speakers("Bạn có muốn biết thêm thông tin chi tiết hơn không?")
                            sleep(4)
                            boolean = get_text()
                            if ("có" in boolean) or ("ok" in boolean) or ("ờ" in boolean) or ("đồng ý" in boolean) or ('mở đi' in boolean) or ("muốn" in boolean):
                                speakers("OK")
                                sleep(3)                        
                                webbrowser.open('https://vi.wikipedia.org/wiki/Ph%C3%B9ng_H%C6%B0ng')
                            else:
                                speakers("OK")
                                raise SystemExit
                        
                elif ("chơi" in answer):        
                    speakers("OK")
                    webbrowser.open('https://quizizz.com/join/quiz/60bdd3c81aae7a001ca57179/start')
                
                else:
                    speakers("Được")
                    webbrowser.open('https://quizlet.com/vn/599891667/khoi-nghia-phung-hung-flash-cards/?x=1qqt')

            def haibatrung():
                speakers("Được rồi, bạn thích flashcards, sơ đồ tư duy hay là chơi trò chơi ngắn")
                sleep(4.5)
                answer = str(get_text())
                if ("xơ đồ" in answer) or ("tư duy" in answer) or ("sơ đồ" in answer):
                    speakers("OK, tôi sẽ mở thông tin cho bạn!")
                    sleep(3)
                    webbrowser.open('https://drive.google.com/file/d/1KQvRK4q9v9JFaPNRpr7K-XiuPiws_7R5/view?usp=sharing')
                    speakers("""Khởi nghĩa Hai Bà trưng. 
                    Lãnh đạo cuộc khởi nghĩa là 2 Bà: Trưng Trắc và Trưng Nhị. Thời gian diễn ra: Mùa xuân năm 40. 
                    Nguyên nhân: Do chế độ cai trị hà khắc của nhà Hán và Thi Sách bị quân Hán giết hại. 
                    Mục tiêu cuộc khởi nghĩa là đánh đuổi nhà Hán và giành lại độc lập. 
                    Diễn biến cuộc khởi nghĩa như sau: Lúc đầu, Hai Bà Trưng phất cờ khởi nghĩa làm lễ tế cờ tại Hát Môn. 
                    Nghĩa quân đã làm chủ Mê Linh, nhanh chóng tiến xuống Cổ Loa và Luy Lâu. 
                    Kết quả: Cuộc khởi nghĩa giành thắng lợi. 
                    Ý nghĩa cuộc khởi nghĩa: Khẳng định vai trò của người phụ nữ Việt Nam, mạnh mẽ - kiên cường. 
                    Đây cũng là cuộc khởi nghĩa đầu tiên diễn ra trong thời kì Bắc thuộc""")
                    sleep(52)
                    speakers("Có một vài video liên quan, bạn có muốn xem không")
                    sleep(4)
                    while True:
                        answer = str(get_text())
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            videourl = 'https://'
                            def playvideo():
                                webbrowser.open(videourl)
                            speakers("OK, bạn xem thử đi nhé.")
                            sleep(3)
                            thu_tu_video = randint(1, 2)
                                
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=WlsJL5k0xgQ'
                                playvideo()
                                raise SystemExit
                            else:
                                speakers("Cảnh báo! Video khá dài, nhưng rất hay bạn nhé, lại còn 3D nữa, mê li luôn...")
                                sleep(7)
                                videourl = 'https://www.youtube.com/watch?v=doP4TtAv81w'
                                playvideo()
                                raise SystemExit
                        elif  ("không" in answer) or ("thôi" in answer) or ("khỏi" in answer) or ("nghỉ" in answer):
                            speakers("Bạn có muốn biết thêm thông tin chi tiết hơn không?")
                            sleep(5)
                            boolean = get_text()
                            if ("có" in boolean) or ("ok" in boolean) or ("ờ" in boolean) or ("đồng ý" in boolean) or ('mở đi' in boolean) or ("muốn" in boolean):
                                                        
                                speakers("OK")
                                sleep(1)
                                webbrowser.open('https://vi.wikipedia.org/wiki/Kh%E1%BB%9Fi_ngh%C4%A9a_Hai_B%C3%A0_Tr%C6%B0ng')
                                raise SystemExit
                            else:
                                speakers("OK")
                            
                                raise SystemExit
                        else:
                            speakers("Tôi không nghe rõ bạn đang nói gì, hãy nói lại.")
                elif "chơi" in answer:
                    speakers("OK, tôi sẽ mở thông tin cho bạn! Khi link mở ra, bạn hãy bấm nút start để chơi nhé. Chúc bạn vừa chơi vừa học thật vui nhé.")
                    sleep(15)
                    webbrowser.open('https://quizizz.com/join/quiz/60bdc6a1b3267a001c6a7b1d/start?studentShare=true')
                    raise SystemExit
                else:
                    speakers("HiCute sẽ mở flashcards cho bạn, bạn hãy ôn tập và làm bài kiểm tra thật tốt qua quizlet nhé, chúc bạn thành công.")
                    sleep(10)
                    webbrowser.open('https://quizlet.com/vn/599396611/khoi-nghia-hai-ba-trung-flash-cards/?x=1jqt')
                    raise SystemExit

            def ba_trieu():
                speakers("Bạn muốn cái nào nhỉ? Flashcards, sơ đồ tư duy hay chơi trò chơi ngắn?")
                sleep(4.5)
                answer = str(get_text())
                if ('sơ đồ' in answer) or ("xơ đồ" in answer):
                    webbrowser.open('https://drive.google.com/file/d/1fKDeJr2wmksNbvtcK6Wi6tWnsHckPgSY/view?usp=sharing')
                    speakers("""Cuộc khởi nghĩa Bà Triệu diễn ra năm 248
                                Nguyên nhân cuộc khởi nghĩa là do chính sách đô hộ, đồng hóa tàn bạo nhà Ngô
                                Lãnh đạo cuộc khởi nghĩa là Bà Triệu và Triệu Quốc đạt.
                                Sau khi Triệu Quốc Đạt tử trận, bà Triệu lên làm chỉ huy.
                                Bà Triệu là người có tính cách mạnh mẽ và kiên cường. Hình ảnh của bà khi ra mặt trận: Mặc giáp, cài trâm vàng, đi guốc, cưỡi voi
                                Diễn biến cuộc khởi nghĩa: Lúc đầu, khởi nghĩa bùng nổ ở Phú Điền.
                                Sau đó, nghĩa quân đã làm chủ Cửu Châu và đã lan rộng khắp Giao Châu.
                                Kết quả: Cuộc khởi nghĩa bà triệu bị đàn áp dã man.
                                Bà Triệu hi sinh trên núi Tùng (Phú Điền - Hậu Lộc - Thanh Hóa)
                                Lăng Bà Triệu: nằm trên đỉnh núi Tùng, hình tứ giác nhỏ dần về phía đỉnh, gồm 2 tầng mái,
                                có chiều cao là 5,8 mét.""")     
                    sleep(62)
                    speakers("Có một vài video thú vị lắm nè, bạn có muốn xem không")
                    sleep(4)
                    while True:
                        answer = str(get_text())
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            videourl = 'https://'
                            def playvideo():
                                webbrowser.open(videourl)
                            speakers("OK, bạn xem thử đi nhé.")
                            sleep(3)
                            thu_tu_video = randint(1, 3)
                                
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=XXB4rvTzjXU'
                                playvideo()
                                
                            elif thu_tu_video == 2:
                                videourl = 'https://www.youtube.com/watch?v=Cty0MNg_cDg'
                                playvideo()
                            else:
                                videourl = 'https://drive.google.com/file/d/1dr02o3aoe1zSx-a9r8JaSlL9e_HKkmIZ/view?usp=sharing'
                                playvideo()
                            raise SystemExit
                        
                        elif ("không" in answer) or ("thôi" in answer) or ("khỏi" in answer) or ("nghỉ" in answer):    
                            speakers("Bạn có muốn biết thêm thông tin chi tiết hơn không?")
                            sleep(5)
                            boolean = get_text()
                            if ("có" in boolean) or ("ok" in boolean) or ("ờ" in boolean) or ("đồng ý" in boolean) or ('mở đi' in boolean) or ("muốn" in boolean):
                                speakers("OK")
                                sleep(2)                        
                                webbrowser.open('https://vi.wikipedia.org/wiki/B%C3%A0_Tri%E1%BB%87u')
                                
                            else:
                                speakers("OK, tạm biệt bạn")
                        else:
                            speakers("Tôi chưa nghe rõ bạn đang nói gì, hãy nói lại.")
                elif ("chơi" in answer):
                    speakers("Chúc bạn chơi vui vẻ và nhân tiện cũng học được nhiều kiến thức thú vị nhé")
                    sleep(6)
                    webbrowser.open('https://quizizz.com/join/quiz/60bc9bdf867e19001bdbd5a5/start?studentShare=true')
                else:
                    speakers("OK, tôi đã tạo cho bạn flashcards từ trước rùi nè, học xong bạn có thể làm bài kiểm tra luôn trên trang nhé")
                    sleep(10)
                    webbrowser.open('https://quizlet.com/vn/599891277/khoi-nghia-ba-trieu-flash-cards/?x=1jqt')
                raise SystemExit 
            
            def ngo_quyen():
                speakers("Được rồi, bạn thích flashcards, sơ đồ tư duy hay là chơi trò chơi vui vẻ")
                sleep(5)
                answer = str(get_text())
                if ("sơ đồ" in answer) or ("xơ đồ" in answer):
                    speakers("OK, tôi sẽ mở thông tin cho bạn!")
                    sleep(3)
                    webbrowser.open('https://drive.google.com/file/d/1fAnnY7wHvxBt1keMGrTgSb8Z-Ga1EEa1/view?usp=sharing')
                    speakers("""Ngô Quyền và chiến thắng Bạch Đằng năm 938:
                    Khởi nghĩa diễn ra vào năm 938. Lãnh đạo là Ngô Quyền
                    Địa điểm cuộc khởi nghĩa là cửa sông Bạch Đằng. Đó là nơi có địa hình đặc biệt: Hai bên bờ sông là cánh rừng rậm, thuận lợi mai phục, lấy gỗ đóng cọc nhọn.
                    Sông Bạch Đằng chịu nhiều ảnh hưởng của hiện tượng thủy triều lên xuống trong ngày, phù hợp với chiến thuật đánh giặc.
                    Kế hoạch đánh giặc của Ngô Quyền và nghĩa quân là xây dựng trận địa cọc ngầm dưới đáy sông Bạch Đằng.
                    Điểm đặc sắc của chiến thuật: Kết hợp giữa tiến công và mai phục, đánh thần tốc, đạt hiệu quả cao, là sự kết hợp của các yêu tố: Thiên thời, địa lợi, nhân hòa.
                    Ý nghĩa của chiến thắng Bạch Đằng năm 938: Là chiến thắng vĩ đại trong lịch sử dân tộc, chấm dứt hơn 1000 năm Bắc thuộc, mở ra một thời kì độc lập lâu dài cho đất nước.""")
                    sleep(52)
                    speakers("Có một vài video liên quan, bạn có muốn xem không")
                    sleep(4)
                    while True:
                        answer = str(get_text())
                        if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                            videourl = 'https://'
                            def playvideo():
                                webbrowser.open(videourl)
                            speakers("OK, bạn xem thử đi nhé.")
                            sleep(3)
                            thu_tu_video = randint(1, 3)
                                
                            if thu_tu_video == 1:
                                videourl = 'https://www.youtube.com/watch?v=wt_MiXJr8pE'
                                playvideo()
                                raise SystemExit
                            elif thu_tu_video == 2:
                                sleep(5)
                                videourl = 'https://www.youtube.com/watch?v=0pL7hNV41lI'
                                playvideo()
                                raise SystemExit
                            else:
                                videourl = 'https://www.youtube.com/watch?v=oPknMTsA69M'
                                playvideo()
                                raise SystemExit
                        else:
                            speakers("Bạn có muốn biết thêm thông tin chi tiết hơn không?")
                            sleep(4)
                            boolean = get_text()
                            if ("có" in boolean) or ("ok" in boolean) or ("ờ" in boolean) or ("đồng ý" in boolean) or ('mở đi' in boolean) or ("muốn" in boolean):
                                speakers("OK")
                                sleep(3)
                                webbrowser.open('https://vi.wikipedia.org/wiki/Tr%E1%BA%ADn_B%E1%BA%A1ch_%C4%90%E1%BA%B1ng_(938)')
                                raise SystemExit
                            else:
                                speakers("OK")
                            
                                raise SystemExit
                        
                elif ("chơi" in answer):
                    speakers("OK, tôi sẽ mở thông tin cho bạn. Hãy chọn start để chơi nhé, và chọn flashcards để ghi nhớ kiến thức. Chúc bạn vừa chơi vừa học thật vui nhé.")
                    sleep(13)
                    webbrowser.open('https://quizizz.com/join/quiz/60bcecdddeabef001dedfe5b/start')
                    raise SystemExit
                else:
                    speakers("HiCute sẽ mở flashcards cho bạn, bạn hãy ôn tập thật tốt qua quizlet nhé, chúc bạn thành công.")
                    sleep(8)
                    webbrowser.open('https://quizlet.com/vn/599918106/chien-thang-bach-dang-cua-ngo-quyen-flash-cards/?x=1qqt')
                    raise SystemExit

            def tong_hop():
                speakers("Tôi đã tổng hợp nội dung chủ đề thời kỳ bắc thuộc, bạn xem nhé")
                webbrowser.open('https://drive.google.com/file/d/18qdka00R8UPYkG5SsgNWX83rGuwG6jZn/view?usp=sharing')
                sleep(15)
                speakers("Tôi có video tóm tắt: 1000 năm bắc thuộc và các cuộc khởi nghĩa của nhân dân ta. Bạn xem nhé?")
                sleep(6)
                answer = str(get_text())
                if ("có" in answer) or ("ok" in answer) or ("ờ" in answer) or ("đồng ý" in answer) or ('mở đi' in answer):
                    webbrowser.open('https://www.youtube.com/watch?v=5LRD-luJd6k&t=4s')
                    raise SystemExit
                else:
                    speakers("Bạn muốn biết về sự kiện lịch sử nào, hãy nói với tôi. Hicute sẽ giúp bạn")
                    sleep(5.75)
                    self.TaskExecution()
                
            def lich_su():
                speakers("Tôi đã tổng hợp nội dung các sự kiện lịch sử theo thời gian, bạn cần ôn tập phần nào, hãy nói với tôi")
                sleep(5.75)
                webbrowser.open('https://drive.google.com/file/d/18qdka00R8UPYkG5SsgNWX83rGuwG6jZn/view?usp=sharing')
                sleep(15)
                speakers("Bạn hãy chọn chủ đề. Hicute sẽ giúp bạn")
                sleep(2)
                self.TaskExecution()            

            def on_thi():
                speakers("OK, tôi đã tạo cho bạn flashcards để ôn tập, bạn hãy xem nhé. Ngoài cách học bằng flashcards, bạn có thể làm bài trắc nghiệm, luyện đề, chơi một số trò chơi củng cố kiến thức trên trang quizlett nữa đó.")
                sleep(15)
                webbrowser.open('https://quizlet.com/vn/599395824/thoi-ki-bacthuoc-va-dau-tranh-gianh-doc-lap-flash-cards/?x=1jqt')
                raise SystemExit
                
            def kha_nang():
                speakers("""Tôi có thể trợ giúp bạn ôn tập môn lịch sử qua sơ đồ tư duy, video, ôn tập bằng flashcard và một số trò chơi qua quizizz và quizlet. 
                Ngoài ra tôi có thể làm một số chức năng khác như tra google, mở nhạc, xem thời tiết, xem giờ... Bạn muốn làm gì?""")
                sleep(17)
                self.TaskExecution()
            
            if not text:
                break
                 
            elif ('xin chào' in text) or ('chào' in text) or ("hello" in text) or ("good morning" in text) or ("good afternoon" in text) or ("good evening" in text):
                speakers("Xin chào. Tôi có thể giúp gì?")
                self.TaskExecution()

            elif ("thoát" in text) or ("tắt" in text) or ("bye" in text) or ("tạm biệt" in text) or ("thôi" in text) or ("nghỉ" in text):
                stop()

            elif ('có thể làm gì' in text) or ('làm được gì' in text) or ('khả năng' in text) or ('biết làm gì' in text) or ('giúp' in text) or ("giúp được gì" in text):
                kha_nang()

            elif ('giờ' in text):
                time()

            elif ('ngày' in text):
                day()
               
            elif ('thời tiết' in text) or ('trời' in text):
                weather()

            elif ("google" in text) or ("cho tôi biết" in text) or ("tìm cho tôi" in text) or ("tìm kiếm" in text):
                speakers ("Bạn cần tìm kiếm thông tin gì?")
                sleep(1.2)
                answer = str(get_text())
                googling(answer)
            
            elif ("chrome" in text) or ("mở web" in text):
                open_chrome()

            elif ("tổng hợp" in text) or ("thời kỳ bắc thuộc" in text) or ("1000 năm bắc thuộc" in text) or ("một nghìn năm bắc thuộc" in text):
                tong_hop()

            elif ('mai thúc loan' in text) or ('mai hắc đế' in text) or ('vua đen họ mai' in text) or ('năm 713' in text) or ('núi vệ sơn' in text) or ('thung lũng hùng sơn' in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về cuộc khởi nghĩa Mai Thúc Loan, bạn có muốn nghe không?")
                sleep(7)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    maithucloan()
                else:
                    speakers ('Tôi sẽ mở wikipedia cho bạn tham khảo nhé')
                    sleep (4)
                    wikipedia_searching_info("Mai Hắc Đế")
                
            elif ('bà trưng' in text) or ('trưng trắc' in text) or ('trưng nhị' in text) or ('năm 40' in text) or ('mê linh' in text) or ('bà chưng' in text) or ('chưng chắc' in text) or ('chưng nhị' in text) or ('trưng nữ vương' in text) or ('chưng nữ vương' in text) or ("chưng vương" in text) or ("trưng vương" in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về cuộc khởi nghĩa Hai Bà Trưng, bạn có muốn xem không?")
                sleep(8)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    haibatrung()
                else:
                    speakers ('Tôi sẽ mở wikipedia cho bạn tham khảo nhé')
                    sleep(2)
                    wikipedia_searching_info('Hai Bà Trưng')
            
            elif ("lí bí" in text) or ("lý bí" in text) or ("lí bý" in text) or ("lý bý" in text) or ("lý nam đế" in text) or ("năm 542" in text) or ('nhà nước vạn xuân' in text) or ("hoàng đế đầu tiên" in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về cuộc khởi nghĩa lí bí, bạn có muốn nghe không?")
                sleep(7)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    li_bi()
                else:
                    speakers ('Tôi sẽ mở wikipedia cho bạn nhé')
                    sleep(4)
                    wikipedia_searching_info('Lý Nam Đế')
            
            elif ("bà triệu" in text) or ("bà chiệu" in text) or ('cùng với triệu quốc đạt' in text) or ("triệu thị trinh" in text) or ('năm 248' in text) or ('cưỡi voi ra trận' in text) or ('cửu châu' in text) or ('giao châu' in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về cuộc khởi nghĩa bà triệu, bạn có muốn nghe không?")
                sleep(7)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    ba_trieu()
                else:       
                    speakers ('Tôi sẽ mở wikipedia cho bạn tham khảo nhé')
                    sleep (4)
                    wikipedia_searching_info('Bà Triệu')  

            elif ("phùng hưng" in text) or ("năm 776" in text) or ("bố cái đại vương" in text) or ("công phấn" in text) or ("giết hổ" in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về cuộc khởi nghĩa phùng hưng, bạn có muốn nghe không?")
                sleep(7)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    phung_hung()
                else:       
                    speakers ('Tôi sẽ mở wikipedia cho bạn nhé')
                    sleep (3)
                    wikipedia_searching_info("Phùng Hưng")  

            elif ("ngô quyền" in text) or ('chiến thắng bạch đằng' in text) or ('năm 938' in text) or ('đánh tan quân nam hán' in text) or ('mở đầu thời kỳ độc lập' in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về ngô quyền và chiến thắng bạch đằng năm 938, bạn có muốn nghe không?")
                sleep(10)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    ngo_quyen()
                else:
                    speakers ('Tôi sẽ mở wikipedia cho bạn tham khảo nhé')
                    sleep (4)
                    wikipedia_searching_info('Trận Bạch Đằng (938)')  
            
            elif ("chăm pa" in text) or ('cham pa' in text) or ('khu liên' in text) or ('lâm ấp' in text):
                speakers("Liên quan đến thông tin bạn yêu cầu, tôi có tư liệu về nước Chăm pa, bạn có muốn nghe không?")
                sleep(6)
                taking_info = str(get_text())
                if ("có" in taking_info) or ("ok" in taking_info) or ("ờ" in taking_info) or ("đồng ý" in taking_info) or ('mở' in taking_info):
                    cham_pa()
                else:       
                    speakers ('Tôi sẽ mở wikipedia cho bạn tham khảo nhé')
                    sleep (4)
                    wikipedia_searching_info("Chăm Pa")  
            
            elif ("nhạc" in text) or ("bài hát" in text) or ("youtube" in text):
                play_sound_on_youtube()

            elif ("hình nền") in text:
                change_wallpaper()
                             
            elif ("báo" in text) or ("tin" in text):
                read_news()
                                      
            elif ("ôn thi" in text) or ("ôn tập" in text) or ("luyện đề" in text) or ("luyện thi" in text) or ("đề bài" in text):
                on_thi()
            
            elif ("cai trị bắc thuộc" in text) or ('chính sách cai trị' in text) or ('cai trị phương bắc' in text) or ("cai trị" in text):
                cai_tri_bac_thuoc()
            
            elif ('kiểm tra' in text) or ('test' in text) or ('trắc nghiệm' in text):
                self.test()
        
            elif ('lịch sử' in text) or ('môn sử' in text) or ('học sử' in text) or ('ôn sử' in text) or ('mục lục' in text):
                lich_su()

            elif ('wiki' in text) or ('wikipedia' in text):
                speakers("Bạn muốn tìm chủ đề gì")
                sleep(1.25)
                answer = str(get_text())
                wikipedia_searching_info(answer)
            
            else:
                speakers("Tôi chưa có dữ liệu bạn yêu cầu 😭, tôi sẽ Google cho bạn")
                sleep(2)
                googling(text)
            raise SystemExit

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_hicuteUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Images\\Wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie) 
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Images\\unnamed.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
    def showTime(self):
        current_time = QTime.currentTime()
        currrent_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = currrent_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)
    # def showSpeaker(self):   
        # current_speaker = QSpeaker.Speaker()
        # self.ui.textBrowser_3.setText(currrent_date)
        # self.ui.textBrowser_3.setText(label_time)
        
app = QApplication(sys.argv)
jarvis=Main()
jarvis.show()
sys.exit(app.exec_())