import os
import openai

def fill_in_the_blank_short_story(OPEN_API_KEY, word_str):

    openai.api_key = OPEN_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Write a short story the includes the following words: "{word_str}". 
            The story should be about an immigrant moving to another country and becoming successful.
            Create a blank space where the above given words should go so that students can fill them in.
            Make the story appropriate for CEFR A2 level students.
            ''', 
        temperature=.5, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("Fill-in-the-Blank: Short Story\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')