# One-shot chain-of-thought prompts
# When you need to sum the even numbers within a given set, you first have to identify these even numbers and then sum them. You can teach this to a language model via one or more examples, and it will follow this strategy to operate on new sets.

# Your goal in this exercise is to teach the model how to apply this procedure on the following set: {9, 10, 13, 4, 2}, and then ask the model to perform it on a new set: {15, 13, 82, 7, 14}. This is how you perform chain-of-thought prompting through one-shot prompting.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# 100 XP
# Define an example that teaches the model how to sum the even numbers on the set {9, 10, 13, 4, 2}.
# Define a question, similar to the one in the example, that asks the model to reason on a new set {15, 13, 82, 7, 14}.
# Create the final prompt.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: {10, 4, 2}. Adding them: 10 + 4 + 2 = 16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}.
              A: Let's think step by step"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

# To sum the even numbers in the set {15, 13, 82, 7, 14}, we can follow these steps:

# 1. **Identify the even numbers**: 
#    - 15 is odd.
#    - 13 is odd.
#    - 82 is even.
#    - 7 is odd.
#    - 14 is even.

#    So, the even numbers in the set are {82, 14}.

# 2. **Add the even numbers**:
#    - 82 + 14 = 96.

# Therefore, the sum of the even numbers in the set {15, 13, 82, 7, 14} is **96**.

# <script.py> output:
#     To sum the even numbers in the set {15, 13, 82, 7, 14}, we can follow these steps:
    
#     1. Identify the even numbers in the set:
#        - 15 is odd.
#        - 13 is odd.
#        - 82 is even.
#        - 7 is odd.
#        - 14 is even.
    
#        So, the even numbers are {82, 14}.
    
#     2. Now, we add the even numbers together:
#        - 82 + 14 = 96.
#     Therefore, the sum of the even numbers in the set {15, 13, 82, 7, 14} is **96**.