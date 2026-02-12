# Multi-step prompt to plan a trip
# You noticed that the single-step prompt was not effective, because the answer was too vague for what you had in mind. You improve your prompt by specifying the steps to follow for planning. The plan should have four potential locations for your beach vacation, and each location should have some accommodation options, some activities, and an evaluation of the pros and cons.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster. This may truncate your solution.

# Instructions
# 100 XP
# Create a multi-step prompt asking the model to make a plan for a beach vacation, which should include: four potential locations, each with some accommodation options, some activities, and an evaluation of the pros and cons.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """
     Help me plan a beach vacation.
     Step 1 - Specify four potential locations for beach vacations
     Step 2 - State some accommodation options in each
     Step 3 - State activities that could be done in each
     Step 4 - Evaluate the pros and cons for each destination
    """

response = get_response(prompt)
print(response)


# Sure! Let’s plan a beach vacation step by step.

# ### Step 1: Specify Four Potential Locations for Beach Vacations

# 1. **Maui, Hawaii**
# 2. **Cancun, Mexico**
# 3. **Gold Coast, Australia**
# 4. **Phuket, Thailand**

# ### Step 2: State Some Accommodation Options in Each

# 1. **Maui, Hawaii**
#    - **Luxury:** Four Seasons Resort Maui at Wailea
#    - **Mid-range:** Kaanapali Beach Hotel
#    - **Budget:** Hostel City Maui

# 2. **Cancun, Mexico**
#    - **Luxury:** The Ritz-Carlton Cancun
#    - **Mid-range:** Fiesta Americana Villas Cancun
#    - **Budget:** Selina Cancun Laguna Hotel Zone

# 3. **Gold Coast, Australia**
#    - **Luxury:** Palazzo Versace
#    - **Mid-range:** Mantra on View Hotel
#    - **Budget:** Surfers Paradise Backpackers Resort

# 4. **