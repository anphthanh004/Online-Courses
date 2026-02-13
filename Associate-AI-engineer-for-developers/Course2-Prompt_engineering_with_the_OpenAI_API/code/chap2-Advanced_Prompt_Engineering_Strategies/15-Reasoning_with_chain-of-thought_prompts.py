# Reasoning with chain-of-thought prompts
# Chain-of-thought prompting is helpful to explain the reasoning behind the answer that the model is giving, especially in complex tasks such as generating the solution for a mathematical problem or a riddle. In this exercise, you will craft a chain-of-thought prompt to let the language model guess the age of your friend's father based on some information you will provide.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# 100 XP
# Create a chain-of-thought prompt to determine your friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = "My friend's father was twice my friend's age. Now my friend is 20 years old. How old is my friend's father in 10 years? Let's think step by step"

response = get_response(prompt)
print(response)


# Let's break down the problem step by step.
    
#     1. **Current Age of Your Friend**: Your friend is currently 20 years old.
    
#     2. **Father's Age When Your Friend Was Born**: When your friend was born, your friend's father was twice your friend's age. Since your friend is now 20, we can determine the father's age at that time:
#        - When your friend was born, your friend's age was 0 years.
#        - Therefore, the father's age at that time was \(2 \times 0 = 0\) (which doesn't make sense). 
    
#        Let's clarify: If your friend is currently 20, we need to find out how old the father was when your friend was born. 
    
#     3. **Father's Current Age**: Let's denote your friend's father's current age as \(F\). Since your friend's father was twice your friend's age when your friend was born, we can express this as:
#        - \(F - 20 = 2 \times 0\) (which is not useful).
    
#        Instead, let's think about the relationship:
#        - If your friend is currently 20, and the father was twice the age of your friend when your friend was born, we can say:
#        - When your friend was born, the father was \(F - 20\) years old.
    
#     4. **Setting Up the Equation**: When your friend was born (20 years ago), the father was twice the age of your friend:
#        - \(F - 20 = 2 \times 0\) (which is not useful).
#        - Instead, we can say that when your friend was born, the father was \(F - 20\) years old, and at that time, your friend was 0 years old.
    
#     5. **Finding Father's Current Age**: Since your friend's father was twice the age of your friend when your friend was born, we can say:
#        - \(F - 20 = 2 \times 0\) (which is not useful).
#        - Instead, we can say that when your friend was born, the father was \(F - 20\) years old, and at that time, your friend was 0 years old.
    
#     6. **Conclusion**: Since your friend is currently 20 years old, and the father was twice the age of your friend when your friend was born, we can conclude that the father's current age is:
#        - \(F = 20 + 20 = 40\).
    
#     7. **Father's Age in 10 Years**: Now, to find out how old your friend's father will be in 10 years:
#        - \(F + 10 = 40 + 10 = 50\).
    
#     So, your friend's father will be **50 years old in 10 years**.