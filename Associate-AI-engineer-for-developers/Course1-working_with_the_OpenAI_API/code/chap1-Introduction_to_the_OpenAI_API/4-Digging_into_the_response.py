# Digging into the response
# One key skill in working with APIs is extracting the right data from a structured response. Now, you'll practice retrieving the necessary text from an OpenAI API response.

# The OpenAI class has already been imported for you from the openai library.

# Instructions
# 100 XP
# Extract the content from the response, which is nested inside the message attribute.



client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Quick productivity tip."}]
)

# Extract the content from the response
print(response.choices[0].message.content)


# # Extract the content from the response
# print(response.choices[0].message.content)
# Set a timer for 25 minutes and work on a single task without distractions. This technique, known as the Pomodoro Technique, helps maintain focus and encourages regular breaks, boosting overall productivity. After the timer goes off, take a 5-minute break before starting another session!
# In [1]:
