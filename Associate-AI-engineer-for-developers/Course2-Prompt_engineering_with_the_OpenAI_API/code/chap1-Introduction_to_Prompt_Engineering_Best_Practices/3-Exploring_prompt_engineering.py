# Exploring prompt engineering
# Prompt engineering refers to crafting effective prompts to guide the language model towards the intended response. By refining your prompts, you can achieve better results and guide the model towards generating more accurate and useful responses. Your task in this exercise is to modify the prompt you used in the previous exercise.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# 100 XP
# Craft a prompt that asks the model to generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand.
# Get the response using the get_response() function.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "write a poem about ChatGPT using English that a child can understand"

# Get the response
response = get_response(prompt)

print(response)



# In a world of words, so bright and wide,  
#     Lives a friendly helper, right by your side.  
#     ChatGPT’s the name, a magical friend,  
#     With stories and answers that never end.  
    
#     Ask me a question, big or small,  
#     I’m here to help you, just give me a call.  
#     From dinosaurs roaring to stars in the sky,  
#     I’ll share all the wonders, just you and I.  
    
#     Want to hear a tale of a brave little mouse?  
#     Or learn how to build a fantastic tree house?  
#     I can tell you about colors, or how to bake pie,  
#     With a sprinkle of magic, oh my, oh my!  
    
#     So if you’re feeling curious, or need a good laugh,  
#     Just type in your thoughts, I’ll help you on your path.  
#     Together we’ll explore, with joy and with glee,  
#     In the land of imagination, just you and me!  
    
#     So remember my name, I’m here day and night,  
#     ChatGPT is my name, your friend in the light.  
#     With words we can travel, to places so grand,  
#     Let’s go on adventures, just take my hand!