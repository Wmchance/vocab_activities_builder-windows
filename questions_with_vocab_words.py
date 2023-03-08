import os
import openai

def questions_with_vocab_words(OPENAI_API_KEY, word_str):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Key words and phrases: {word_str}. \nCreate a horizontal word list for the above key words. Write 'Word Bank:' above the word list.\n\nFor each word in the word list, write two questions using that word.\nThe questions should be at the CEFR A2 English level.",
        temperature=0.7,
        max_tokens=2061,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("Questions with Vocab Words\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')