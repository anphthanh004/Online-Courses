# Single-step prompt to plan a trip
# Imagine you're a developer taking a break and you want to apply your prompting skills to plan the perfect beach vacation. As an initial step, you decide to use a standard single-step prompt to seek assistance.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster.

# Instructions
# 100 XP
# Create a single-step prompt asking the model to help you plan a beach vacation.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "Help me plan a beach vacation"

response = get_response(prompt)
print(response)

# Sure! Planning a beach vacation can be exciting. Here’s a step-by-step guide to help you organize your trip:
    
#     ### Step 1: Choose Your Destination
#     - **Consider Your Preferences**: Do you prefer a tropical paradise, a rugged coastline, or a family-friendly beach?
#     - **Popular Beach Destinations**: 
#       - **USA**: Miami Beach, Maui, San Diego, Outer Banks
#       - **Caribbean**: Bahamas, Jamaica, Barbados, Cancun
#       - **Europe**: Amalfi Coast (Italy), Costa del Sol (Spain), Greek Islands
#       - **Asia**: Bali (Indonesia), Phuket (Thailand), Maldives
    
#     ### Step 2: Decide on Travel Dates
#     - **Season**: Consider the best time to visit your chosen destination. Some beaches are best in summer, while others may be ideal in spring or fall.
#     - **Duration**: How long do you want to stay? A long weekend, a week, or more?