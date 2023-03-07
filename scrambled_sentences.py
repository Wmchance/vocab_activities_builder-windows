import os
import openai

def scrambled_sentences(OPENAI_API_KEY, word_str):
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Generate one sentence for each of the following words: "{word_str}". 
            The sentences should be appropriate for CEFR A2 level students.
            Write the sentences in a numbered bullet format.
            Write instructions telling students to rewrite the sentences in the correct order.
            ''', 
        temperature=.3, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open('C:\\Users\wchance\Desktop\worksheet.txt', 'a') as fp:
        pass
        fp.write("Scrambled Sentences\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')