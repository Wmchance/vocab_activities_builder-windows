import os
import openai

def match_words_to_definitions(OPENAI_API_KEY, word_str):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Key words and phrases: {word_str}. \n\nPut each of the above words in a box. Make the box horizontal. Add the text 'Word Bank:' above the box.\n\nWrite instructions telling students to \"match the key words to the definitions'.\n\nWrite definitions for each of the key words using CEFR A2 level English.\nPut the definitions in a separate section below the word bank. \nRemove the key words from the definitions. Add a small underlined empty space after each definition.",
        temperature=0.69,
        max_tokens=2015,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("Match Words to Definitions\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')