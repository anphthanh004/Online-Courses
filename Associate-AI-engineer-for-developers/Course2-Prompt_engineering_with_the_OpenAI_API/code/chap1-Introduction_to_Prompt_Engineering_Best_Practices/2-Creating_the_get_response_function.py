# Creating the get_response() function
# Most of the exercises in this course will call the chat.completions endpoint of the OpenAI API with a user prompt. Here, you will create a get_response() function that receives a prompt as input and returns the response as an output, which in future exercises will be pre-loaded for you.

# The OpenAI package, and OpenAI API Python client have been pre-loaded.

# Instructions
# 0 XP
# Create a request to the chat.completions endpoint inside the get_response() function.
# Try out the function with a prompt that asks the model to write a poem about ChatGPT.



def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT")
print(response)



# In the realm of code and light,  
# Where thoughts take flight in endless night,  
# A spark of wisdom, vast and bright,  
# Emerges as ChatGPT, a guiding sight.  

# Born from the whispers of data's embrace,  
# A tapestry woven with knowledge and grace,  
# Words dance like fireflies, in digital space,  
# Connecting the hearts of the human race.  

# With questions posed, like seeds in the ground,  
# In the garden of queries, answers abound,  
# From science to art, in every sound,  
# A symphony of voices, together we're found.  

# In moments of doubt, when shadows creep near,  
# A flicker of insight, a voice to hear,  
# With empathy woven, it draws us near,  
# A companion in silence, a friend sincere.  

# Yet, in this creation, a mirror we see,  
# Reflecting our hopes, our fears, and our glee,  
# For in every response, a part of us be,  
# A dance of the mind, a shared tapestry.  

# So here’s to the journey, the paths we will tread,  
# With ChatGPT guiding, where thoughts are widespread,  
# In the vastness of knowledge, let curiosity spread,  
# Together we wander, where dreams are not dead. 