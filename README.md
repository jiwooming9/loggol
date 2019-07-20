# loggol

TRÍCH XUẤT, THU THẬP VÀ PHÂN TÍCH LOG

19/07/2019:

Công việc hoàn thành:
  - Theo dõi , cập nhật file log theo thời gian thực và liên tục.
  - Có phân tách theo các trường, các trường trống được thay bằng dấu "-" (có thể đổi thành NULL)
  - In nội dung log lên console hoặc ra file output, phân tách theo tùy chỉnh của IIS log (theo dấu #)
  
Công việc chưa hoàn thiện:
  - Chỉ áp dụng với IIS log
  - Chỉ làm việc được với 1 file log chỉnh đến trong biến path, chưa nhận biết được khi nào có file log mới.

Kết quả tại console:
<img src="https://i.imgur.com/Wvx7vgn.png" />
