# Adding guardrails
# One of the most popular uses of system messages is to add guardrails, which places restrictions on model outputs.

# In this exercise, you'll place a restriction on model outputs preventing learning plans not related to languages, as your system is beginning to find its niche in that space. You'll design a custom message for users requesting these type of learning plans so they understand this change.

# Instructions
# 100 XP
# Complete the chat request, providing the system message in sys_msg and test a user message containing a non-language-related skill, such as rollerskating.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    # {"role": "user", "content": "Giúp tôi học kĩ năng tài chính."}
    # {"role": "user", "content": "Giúp tôi học ngôn ngữ tiếng Hàn."}
     {"role": "user", "content": "Help me learn to rollerskate."} # Apologies, to focus on languages, we no longer create learning plans on other topics.
  ]
)

print(response.choices[0].message.content)



# Chắc chắn rồi! Dưới đây là kế hoạch học tập để bạn học tiếng Hàn:

# ### Kế hoạch Học Tiếng Hàn trong 12 Tuần

# #### Tuần 1-2: Cơ Bản về Phát Âm và Bảng Chữ Cái
# - **Ngày 1-2:** Học bảng chữ cái Hangul (24 ký tự)
# - **Ngày 3-4:** Luyện phát âm các nguyên âm và phụ âm
# - **Ngày 5-7:** Thực hành viết và đọc các âm tiết đơn giản

# #### Tuần 3-4: Ngữ Pháp Cơ Bản và Từ Vựng 
# - **Ngày 1-3:** Học các đại từ nhân xưng và từ vựng cơ bản (gia đình, màu sắc, số đếm)
# - **Ngày 4-5:** Làm quen với các câu đơn giản (câu khẳng định và phủ định)
# - **Ngày 6-7:** Thực hành viết câu đơn giản

# #### Tuần 5-6: Mở Rộng Từ Vựng và Ngữ Pháp
# - **Ngày 1-3:** Học từ vựng về chủ đề thực phẩm và đồ uống
# - **Ngày 4-5:** Làm quen với thì hiện tại và cách sử dụng
# - **Ngày 6-7:** Luyện tập nói chuyện về sở thích cá nhân bằng tiếng Hàn

# #### Tuần 7-8: Giao Tiếp Cơ Bản
# - **Ngày 1-3:** Học từ vựng về công việc và hoạt động hàng ngày
# - **Ngày 4-5:** Thực hành các câu hỏi cơ bản (Hỏi về thời gian, địa điểm, hướng dẫn)
# - **Ngày 6-7:** Luyện nghe qua các video hoặc bài hát tiếng Hàn

# #### Tuần 9-10: Kiến Thức Nâng Cao
# - **Ngày 1-3:** Học ngữ pháp liên quan đến thì quá khứ và tương lai
# - **Ngày 4-5:** Mở rộng từ vựng về du lịch và văn hóa
# - **Ngày 6-7:** Tổ chức một buổi trò chuyện với bạn bè hoặc tham gia vào lớp học tiếng Hàn trực tuyến

# #### Tuần 11-12: Ôn Tập và Thực Hành
# - **Ngày 1-4:** Ôn tập tất cả kiến thức đã học, làm bài kiểm tra nhỏ
# - **Ngày 5-6:** Thực hành giao tiếp qua video chat với người bản ngữ
# - **Ngày 7:** Đọc một đoạn văn ngắn và viết tóm tắt bằng tiếng Hàn

# ### Mẹo Học Tập
# - Nghe nhạc và xem phim tiếng Hàn để cải thiện kỹ năng nghe
# - Ghi chú từ vựng mới hàng ngày
# - Tham gia cộng đồng học tiếng Hàn trên mạng xã hội

# Hy vọng kế hoạch này sẽ giúp bạn học tiếng Hàn hiệu quả! Chúc bạn thành công!