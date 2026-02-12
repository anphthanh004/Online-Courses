# Content generation
# AI is playing a much greater role in content generation, from creating marketing content such as blog post titles to creating outreach email templates for sales teams.

# In this exercise, you'll harness AI to generate a catchy slogan for a new restaurant. Feel free to test out different prompts, such as varying the type of cuisine (Italian, Chinese, etc.) or the type of restaurant (fine-dining, fast-food, etc.), to see how the response changes.

# Instructions
# 100 XP
# Create a request to create a slogan for a new restaurant; set the maximum number of tokens to 100.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Công ty tôi cung cấp các mặt hàng sản phẩm đồ điện tử, hãy làm nổi bật các tính năng hiệu năng, độ bền, chất lượng

Hướng đến những người dùng ưu thích sự đơn giản, thanh lịch. Hãy tạo cho tôi slogan 
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": f"{prompt}"}],
  max_completion_tokens=100,
)

print(response.choices[0].message.content)

# Dưới đây là một số gợi ý slogan dành cho công ty cung cấp đồ điện tử, hướng đến những người dùng ưu thích sự đơn giản và thanh lịch:

# 1. **"Sự tinh tế trong từng sản phẩm."**
# 2. **"Đồ điện tử, đơn giản nhưng không đơn điệu."**
# 3. **"Chất lượng bền bỉ, phong cách thanh lịch."**
# 4. **"Hiệu suất tối ưu, thiết kế hoàn hảo