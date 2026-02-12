# Using delimited prompts with f-strings
# You are a junior developer at a dynamic startup that generates content with the help of AI. The company believes this technology can revolutionize storytelling, and you are excited to be a part of it. Today, your task is to generate a continuation of a story with a delimited prompt using an f-string.

# The OpenAI package, the get_response() function, and the story variable have been pre-loaded for you.

# Instructions
# 100 XP
# Create a prompt asking to complete the variable story (provided to you as a string): use f-string, and delimit the story with triple backticks (```) to pass its content to the prompt.
# Get the generated response.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


#  Original story: 
     
#     In a distant galaxy, there was a brave space explorer named Alex. Alex had spent years traveling through the cosmos, discovering new planets and meeting alien species. One fateful day, while exploring an uncharted asteroid belt, Alex stumbled upon a peculiar object that would change the course of their interstellar journey forever...
    
    
#      Generated story: 
#      ```
#     The object was a shimmering, crystalline sphere, pulsating with a soft, ethereal light. Intrigued, Alex carefully maneuvered their ship closer, the asteroid belt swirling around them like a cosmic dance. As the ship's sensors scanned the sphere, a series of ancient symbols illuminated on the screen, revealing a language long forgotten by the galaxy.
    
#     With a mix of excitement and trepidation, Alex decided to retrieve the sphere. Using a specialized robotic arm, they carefully grasped it and brought it aboard the ship. The moment the sphere crossed the threshold of the airlock, a surge of energy coursed through the ship, causing the lights to flicker and the engines to hum with newfound power.
    
#     Curiosity piqued, Alex activated the ship's holographic interface to analyze the sphere further. The symbols began to rearrange themselves, forming a map of the galaxy with a glowing
# In [1]:
