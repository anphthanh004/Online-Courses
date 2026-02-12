# OpenAI API message roles
# You are developing a chatbot for an event management agency that will be used to facilitate networking during events.

# Using the OpenAI API, you prepare a dictionary to pass as the message to the chat.completions endpoint. The message needs to have 3 roles defined to ensure the model has enough guidance to provide helpful responses.

# Throughout the course, you'll write Python code to interact with the OpenAI API. Entering your own API key is not necessary to create requests and complete the exercises in this course. You can leave the placeholder "<OPENAI_API_TOKEN>" as the key in api_key.

# The OpenAI package has been pre-loaded for you.


# Create the OpenAI client: you can leave "<OPENAI_API_TOKEN>" as is
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""}
]

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)


# Here are some effective conversation starters for networking events:
    
#     1. **Background Inquiry**: "What brings you to this event today? Are you looking for anything specific?"
    
#     2. **Industry Trends**: "Have you noticed any interesting trends in our industry lately?"
    
#     3. **Recent Projects**: "What project are you currently working on that excites you the most?"
    
#     4. **Common Interests**: "I heard you mention [topic or interest]. Can you tell me more about that?"
    
#     5. **Event Experience**: "What do you think of the event so far? Have you attended any other events like this?"
    
#     6. **Networking Goals**: "What are your goals for networking here? Are you looking to meet specific people or find certain opportunities?"
    
#     7. **Professional Development**: "Have you taken any workshops or courses recently that you found valuable?"
    
#     8. **Book/Resource Recommendations**: "Have you read any good books or articles related to our field lately?"
    
#     9. **Career Path**: "What inspired you to pursue your current career path?"
    
#     10. **Future Opportunities**: "What are some of your upcoming goals for your career or business?"
    
#     These starters can help foster engaging discussions and establish connections with other attendees.

