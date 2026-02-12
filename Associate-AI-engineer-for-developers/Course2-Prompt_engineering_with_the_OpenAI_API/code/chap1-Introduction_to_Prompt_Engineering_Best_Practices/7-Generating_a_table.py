# Generating a table
# Imagine you are a developer working for a renowned online bookstore known for its extensive collection of science fiction novels. Today, you have a task at hand: to create a table of ten must-read science fiction books for the website's homepage. This will enhance the user experience on the website, helping fellow sci-fi enthusiasts discover their next great read.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# 0 XP
# Craft a prompt that generates a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover.
# Get the response.







client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = "Generate a table containing 10 books I should read if I am a science fiction lover, with columns for Title, Author, and Year."

# Get the response
response = get_response(prompt)
print(response)


#  Here's a table of 10 must-read science fiction books:
    
#     | Title                          | Author                | Year  |
#     |--------------------------------|----------------------|-------|
#     | Dune                           | Frank Herbert         | 1965  |
#     | Neuromancer                    | William Gibson        | 1984  |
#     | The Left Hand of Darkness      | Ursula K. Le Guin    | 1969  |
#     | Foundation                     | Isaac Asimov         | 1951  |
#     | Snow Crash                     | Neal Stephenson      | 1992  |
#     | Hyperion                       | Dan Simmons          | 1989  |
#     | The Dispossessed               | Ursula K. Le Guin    | 1974  |
#     | Ender's Game                   | Orson Scott Card     | 1985  |
#     | The Martian                   | Andy Weir            | 2011  |
#     | The Three-Body Problem         | Liu Cixin            | 2008  |
    
#     These books represent a range of themes and styles within the science fiction genre, making them essential reads for any fan.