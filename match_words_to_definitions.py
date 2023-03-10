import os
import openai

def match_words_to_definitions(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'''Key words and phrases: {word_str}.
        \nWrite definitions for each of the key words without using the key words in the definition.
        \nUse CEFR A2 level English to write the definitions.
        \nAdd a long underlined empty space after each definition.
        ''',
        temperature=0.69,
        max_tokens=2015,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Match Words to Definitions\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: Match the above words to the definitions below\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')