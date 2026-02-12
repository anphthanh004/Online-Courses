# Zero-shot prompting with reviews
# As well as answering questions, transforming text, and generating new text, OpenAI's models can also be used for classification tasks, such as categorization and sentiment analysis.

# In this exercise, you'll explore using OpenAI's chat models for sentiment classification using reviews from an online shoe store called Toe-Tally Comfortable.

# Instructions
# 100 XP
# Define a prompt to classify the sentiment of the statements provided using the numbers 1 to 5 (positive to negative).
# Create a request to the Chat Completions endpoint to send this prompt to gpt-4o-mini.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """Hãy xếp hạng cảm xúc từ 1 đến 5 (negative to postitive) cho các bình luận thu được từ bình luận trên cửa hàng online:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100
)

print(response.choices[0].message.content)
# Dưới đây là xếp hạng cảm xúc cho các bình luận theo thang điểm từ 1 đến 5 (1 là tiêu cực và 5 là tích cực):

# 1. **Unbelievably good!** - 5
# 2. **Shoes fell apart on the second use.** - 1
# 3. **The shoes look nice, but they aren't very comfortable.** - 3
# 4. **Can't wait to show them off!** - 5