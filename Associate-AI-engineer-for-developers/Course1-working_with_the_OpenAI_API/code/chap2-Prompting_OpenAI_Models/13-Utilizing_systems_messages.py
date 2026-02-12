# Utilizing systems messages
# The Chat Completions endpoint supports three different roles to shape the messages sent to the model:

# System: controls assistant's behavior
# User: instruct the assistant
# Assistant: response to user instruction
# In this exercise, you'll begin to design an AI system for helping people learn new skills, using a system message to set an appropriate model behavior.

# Instructions
# 100 XP
# Create a request using both system and user messages to create a study plan to learn to speak Dutch.
# Extract and print the assistant's text response.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_completion_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)

# Great choice! Learning Dutch can be a rewarding experience, especially if you're planning to travel to the Netherlands or Belgium, or if you want to connect with Dutch-speaking communities. Here’s a structured plan to help you get started:

# ### **12-Week Dutch Language Learning Plan**

# #### **Week 1-2: Foundation**
# - **Goal:** Learn basic vocabulary and common phrases.
# - **Activities:**
#   - Spend 15-30 minutes daily on a language app (like Duolingo, Babbel, or Memrise).
#   - Focus on basic greetings, numbers, and common expressions (e.g., "Hallo" - Hello, "Dank u" - Thank you).
#   - Start a vocabulary notebook to write down new words.