import os
import openai

def words_to_picture(OPENAI_API_KEY, word_str):
    
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Make a word bank for the following words: "{word_str}". 
            Write instructions asking students to draw a picture for each of the words in the word bank.
            Write instructions asking the students to write a sentence to accompany each of the pictures they have drawn.
            Create an area for student to complete the above tasks.
            Make the instructions appropriate for CEFR A2 level students.
            ''', 
        temperature=.5, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("Words to Pictures\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')