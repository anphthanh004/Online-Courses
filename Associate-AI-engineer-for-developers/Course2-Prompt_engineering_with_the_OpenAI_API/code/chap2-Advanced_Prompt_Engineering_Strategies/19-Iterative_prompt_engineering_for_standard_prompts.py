# Iterative prompt engineering for standard prompts
# You are a developer using prompt engineering techniques for your various tasks, and you want to carefully select the right language model. You wrote an initial prompt to know what are the top ten pre-trained language models out there. Now, your goal is to refine this prompt to generate a table presenting information on each model's name, release year and its owning company.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# 100 XP
# Iteratively refine the prompt to get the desired outcome: a table with three columns for the top ten pre-trained language models, listing the model name, release year, and owning company.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = "Generate a table that I can copy to Excel, \
that table has three columns for the top ten pre-trained language models,\
listing the model name, release year, and owning company"

response = get_response(prompt)
print(response)

    # Here’s a table formatted for easy copying into Excel, listing the top ten pre-trained language models along with their release year and owning company:
    
    # | Model Name                | Release Year | Owning Company         |
    # |---------------------------|--------------|------------------------|
    # | BERT                      | 2018         | Google                 |
    # | GPT-2                     | 2019         | OpenAI                 |
    # | RoBERTa                   | 2019         | Facebook AI Research    |
    # | T5                        | 2019         | Google                 |
    # | GPT-3                     | 2020         | OpenAI                 |
    # | XLNet                     | 2019         | Google/CMU             |
    # | ALBERT                    | 2019         | Google                 |
    # | ELECTRA                   | 2020         | Google                 |
    # | Turing-NLG                | 2020         | Microsoft              |
    # | ChatGPT                   | 2020         | OpenAI                 |
    
    # You can copy this table directly into Excel, and it should format correctly into three columns.