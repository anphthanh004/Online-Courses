# Self-consistency prompts
# Imagine you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day? This problem is defined in the problem_to_solve string, and you will use a self-consistency prompt to solve it.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster.

# Instructions
# 100 XP
# Create the self_consistency_instruction that allows the model to solve the problem with three experts and combine the results with a majority vote.
# Create the final prompt by combining the self_consistency_instruction and the problem_to_solve.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction = "Imagine three completely independent expert who reason differently are answering this question. The final answer is obtained by majority vote. The question is: "

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)



    # Let's break down the problem step by step.
    
    # 1. **Initial Inventory:**
    #    - Total devices: 50
    #    - Mobile phones: 60% of 50 = 0.6 * 50 = 30 mobile phones
    #    - Laptops: 50 - 30 = 20 laptops
    
    # 2. **Sales:**
    #    - Three clients bought one mobile phone each: 3 mobile phones sold.
    #    - One of the clients also bought a laptop: 1 laptop sold.
    #    - Total sold: 3 mobile phones and 1 laptop.
    
    # 3. **Inventory after Sales:**
    #    - Mobile phones: 30 - 3 = 27 mobile phones remaining
    #    - Laptops: 20 - 1 = 19 laptops remaining
    
    # 4. **New Inventory Added:**
    #    - Added 10 laptops and 5 mobile phones.
    #    - New mobile phones: 27 + 5 = 32 mobile phones
    #    - New laptops: 19 + 10 = 29 laptops
    
    # 5. **Final Count:**
    #    - Laptops: 29
    #    - Mobile phones: 32
    
    # So, by the end of the day, you have **29 laptops and 32 mobile phones**.