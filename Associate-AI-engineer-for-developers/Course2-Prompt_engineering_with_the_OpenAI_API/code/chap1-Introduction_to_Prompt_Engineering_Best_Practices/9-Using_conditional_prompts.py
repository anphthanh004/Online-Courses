# Using conditional prompts
# Building upon the previous task, your next challenge is to enhance the responses you received. When processing a given text, you need to determine its language, count the number of sentences, and generate a suitable title if the text contains more than one sentence. However, here's the new twist: if the text consists of only one sentence, no title should be generated, and instead, the model should display "N/A". This modification ensures that the title is generated only for texts with multiple sentences, providing a more refined and practical output for your platform's users.

# The OpenAI package, the get_response() function, and the sample text have been pre-loaded for you.

# Instructions
# 100 XP
# Create the instructions, with the directions to infer the language and the number of sentences of the given delimited text; then if the text contains more than one sentence, generate a suitable title for it, otherwise, write 'N/A' for the title.
# Create the output_format, with directions to include the text, language, number of sentences, and title, each on a separate line,and ensure to use 'Text:', 'Language:', and 'Title:' as prefixes for each line.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language and the number of sentences it contains. Then, if the text has more than one sentence, generate a suitable title for it. Otherwise, if the text contains only one sentence, write 'N/A' for the title."

# Create the output format
output_format = """The output should follow this format:
          - Text: <the given text>
          - Language: <the text language>
          - Title: <the generated title, or N/A>'."""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)


    # - Text: # In the heart of the forest, sunlight filters through the lush green canopy, creating a tranquil atmosphere that feels untouched by time. Shafts of golden light fall gently onto the forest floor, illuminating patches of moss and fallen leaves like scattered fragments of treasure. The air is cool and carries the earthy scent of damp soil and wildflowers, blending into a fragrance that soothes the mind.
    
    # # A narrow path winds quietly between ancient trees whose roots twist and curl above the ground like silent guardians of forgotten stories. Birds perch high above, their soft melodies weaving through the branches, while somewhere in the distance, the faint sound of a flowing stream adds a steady, calming rhythm. Occasionally, a gentle breeze stirs the leaves, sending whispers through the canopy as if the forest itself is breathing.
    
    # # Tiny insects hover in the beams of sunlight, their wings glimmering like specks of dust suspended in time. Ferns sway lightly at the edge of the path, and small woodland creatures move cautiously through the undergrowth, hidden yet present. Every step deeper into the forest feels like stepping further away from the noise of the outside world and closer to something ancient and quietly magical.
    
    # # Here, time slows. Thoughts soften. And for a brief moment, the forest offers a sanctuary where nature speaks not in words, but in light, sound, and stillness.
    # - Language: English
    # - Title: The Tranquil Sanctuary of the Forest