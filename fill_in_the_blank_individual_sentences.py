import os
import openai

def fill_in_the_blank_individual_sentences(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Write an individual sentence for each of the following words: "{word_str}". 
            Create a blank space where the above given words should go so that students can fill them in.
            Present the  sentences in a numbered bullet format.
            Make the sentences appropriate for CEFR A2 level students.
            ''', 
        temperature=.7, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Fill-in-the-Blank: Sentences\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')