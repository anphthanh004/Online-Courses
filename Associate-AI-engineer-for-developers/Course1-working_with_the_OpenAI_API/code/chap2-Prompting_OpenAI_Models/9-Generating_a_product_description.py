# Generating a product description
# Imagine you're writing marketing copy for SonicPro headphones. Your goal is to generate a persuasive product description using the OpenAI API.

# Test how different prompting techniques, response lengths, and temperature settings influence the output!

# Instructions
# 100 XP
# Create a detailed prompt to generate a product description for SonicPro headphones, including:
# Active noise cancellation (ANC)
# 40-hour battery life
# Foldable design
# Experiment with max_completion_tokens and temperature settings to see how they affect the output.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """Hãy viết mô tả chi tiết sản phẩm cho SonicPro headphones, bao gồm:
    Active noise cancellation (ANC)
    40-hour battery life
    Foldable design
"""

# configs = [(100, 0), (200, 0.5), (300, 1), (400, 2)]
# n = 4
# res = []

# for i in range(n) :
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    # max_completion_tokens=configs[i][0],
    # temperature=configs[i][1],
    max_completion_tokens=400,
    temperature=1,
)
# res.append(response.choices[0].message.content)

# for r in res:
#     print(r)
print(response.choices[0].message.content)

# **Mô Tả Sản Phẩm: Tai Nghe SonicPro**

# Chiếc tai nghe SonicPro không chỉ đơn thuần là một phụ kiện âm thanh, mà còn là một trải nghiệm tuyệt vời cho những ai yêu thích âm nhạc và muốn tận hưởng sự tách biệt khỏi thế giới ồn ào bên ngoài. Dưới đây là những đặc điểm nổi bật của sản phẩm:

# ### 1. **Chức Năng Khử Tiếng Ồn Chủ Động (Active Noise Cancellation - ANC)**
# Tai nghe SonicPro được trang bị công nghệ khử tiếng ồn chủ động tiên tiến, giúp bạn lọc bỏ những âm thanh ồn ào xung quanh, cho phép bạn đắm chìm hoàn toàn trong âm nhạc yêu thích mà không bị làm phiền. Dù bạn đang ở trong một quán cà phê đông đúc hay trên chuyến bay dài, SonicPro sẽ giúp bạn tận hưởng những giai điệu một cách trọn vẹn nhất.

# ### 2. **Thời Gian Sử Dụng Lên Đến 40 Giờ**
# Với pin có dung lượng lớn, tai nghe SonicPro mang lại thời gian sử dụng lên đến 40 giờ chỉ với một lần sạc. Bạn có thể thoải mái nghe nhạc, xem phim hay tham gia các cuộc gọi mà không cần lo lắng về việc hết pin. Đặc biệt, chế độ tiết kiệm năng lượng thông minh giúp tối ưu hóa thời gian sử dụng, cho phép bạn đồng hành cùng SonicPro trong những chuyến đi dài mà không cần phải thường xuyên sạc lại.

# ### 3. **Thiết Kế Gấp Gọn và Tiện Lợi**
# Tai nghe SonicPro được thiết kế thông minh với khả năng gấp gọn, giúp bạn dễ dàng mang theo bất cứ đâu. Với trọng lượng nhẹ và kích thước nhỏ gọn khi gập lại, SonicPro

