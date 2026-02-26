# Product description expansion
# As you continue your work on the electronics review website, you've come across some products that are already summarized but lack a comprehensive description. Your task now is to expand these concise product descriptions into detailed narratives, ensuring that each product has both a full description and a bulleted summary for easy comparison. The complete description should effectively capture the product's unique features, benefits, and potential applications. You will apply your first prompt on a smart home security camera's product description.

# The OpenAI package, the product_description string, and the get_response() function have been pre-loaded for you.

# Instructions
# 100 XP
# Craft a prompt that expands the product_description pre-loaded string, and writes a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f""" Expand the text below into a comprehensive one-paragraph overview. \
    The expanded description should highlight the smart home security camera’s unique features, \
    key benefits for users, and potential applications in everyday life. \
        Make the writing clear, engaging, and professional. Product description:\
        ```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)