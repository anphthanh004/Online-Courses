# Text summarization
# One really common use case for using OpenAI models is summarizing text. This has a ton of applications in business settings, including summarizing reports into concise one-pagers or a handful of bullet points, or extracting the next steps and timelines for different stakeholders.

# In this exercise, you'll summarize a passage of text on financial investment (finance_text) into two concise bullet points using a chat completion model.

# Instructions
# 100 XP
# Use an f-string to insert finance_text into prompt.
# Create a request, sending the prompt provided; use a maximum of 400 tokens.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Assign your text to a variable first
finance_text = """Trong thời đại 4.0 hiện nay, sự dịch chuyển của ngành logistic trong kỷ nguyên số
không chỉ dừng lại ở việc tối ưu lộ trình mà còn là khả năng thích ứng thời gian thực với
các biến động của thị trường. Bài toán vận tải truyền thống vốn dựa trên các tài nguyên
tĩnh đã không còn đáp ứng được tính phức tạp khi xuất hiện các nhu cầu giao hàng động
(Dynamic). Trong bối cảnh đó, mô hình phối hợp song song giữa xe tải và thiết bị bay
không người lái (Parallel Truck-Drone) nổi lên như một giải pháp tối ưu, tận dụng được
thế mạnh về tải trọng của xe tải và tính linh hoạt về tốc độ của drone.
Tuy nhiên, thách thức lớn nhất nằm ở việc điều phối các thực thể này trong môi
trường không chắc chắn, nơi các yêu cầu khách hàng xuất hiện rời rạc theo khung thời
gian mà không có thông tin báo trước. Các thuật toán tối ưu hóa cổ điển thường tập
trung tìm kiếm một lời giải duy nhất cho một kịch bản cố định, điều này dẫn đến sự thiếu
hiệu quả khi môi trường thay đổi.
Để giải quyết vấn đề này, đề tài tiếp cận theo hướng Genetic Programming
Hyper-heuristic. Trong cách tiếp cận này, thay vì tìm kiếm một lộ trình cụ thể, mục
tiêu là tiến hóa các quy tắc điều phối (dispatching policies) để cuối cùng tìm ra tập hợp
các chính quy tắc tối ưu không bị trị, đảm bảo sự cân bằng giữa khả năng phục vụ khách
hàng tối đa và việc tối thiểu hóa tổng thời gian hoàn thành nhiệm vụ."""

# Then use the variable in your f-string
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""


# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=400,
)

print(response.choices[0].message.content)