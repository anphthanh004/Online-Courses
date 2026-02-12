# Building specific and precise prompts
# In the previous exercise, you generated text that completes a given story. Your team was happy with your achievement, however, they want you to follow specific guidelines when it comes to length and style. Your task now is to craft a more specific prompt that controls these aspects of the generated story.

# The OpenAI package, the get_response() function, and the same story variable have been pre-loaded for you.

# Instructions
# 100 XP
# Craft a prompt that completes the given story with only two paragraphs in the style of Shakespeare; use f-string, and delimit the story with triple backticks (```).


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
prompt = f"""Complete the story delimited by triple backticks with only two paragraphs in the style of Shakespeare
```{story}```
"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)


#  Generated story: 
#  Upon that fateful find, a crystal orb did gleam,  
# Its surface shone with hues of azure bright,  
# As if the very stars had trapped their beam,  
# And whispered secrets of the cosmic night.  
# With trembling hands, brave Alex did approach,  
# For in that sphere, a power strange did dwell,  
# A voice, ethereal, like a silken broach,  
# Did beckon forth, with tales of heaven and hell.  

# “Thou seeker bold, dost thou wish to behold,  
# The fates entwined in threads of time and space?  
# For every choice, a story yet untold,  
# And in thy heart, the courage to embrace.”  
# Thus, Alex stood, with heart both fierce and true,  
# To grasp the orb, and with it, fate’s decree,  
# A journey vast, where dreams and fears anew,  
# Would weave the tapestry of destiny.  