# Customizing output format
# You work as a developer at a startup that offers a text analysis platform for content creators. Your platform helps users automatically categorize and format their content, and you're now working on a new feature that detects the language of a given piece of text and generates a suitable title for that text in a custom format. You decide to craft a prompt that guides the language model through this.

# The OpenAI package, the get_response() function, and the text variable have been pre-loaded for you.

# Instructions
# 100 XP
# Create the instructions for the prompt, asking the model to determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters.
# Create the output_format with directions to include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line.
# Create the final_prompt by combining all parts and the delimited text to use.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language, then generate a suitable title for it. "

# Create the output format
output_format = """Use the following format for the output:
         - Text: <the text>
         - Language: <the text language>
         - Title: <the generated title>"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

# - Text: Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]
# - Language: English
# - Title: The Adventures of Curious David in a Quaint Village