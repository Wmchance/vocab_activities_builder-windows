import os
import openai

def questions_with_vocab_words(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'''Key words and phrases: {word_str}. 
        \nFor each word in the word list, write two questions using that word.
        \nThe questions should be at the CEFR A2 English level.''',
        temperature=0.7,
        max_tokens=2061,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    
    response_text = response.choices[0]['text']

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Questions with Vocab Words\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: Answer each of the below questions. There are two for each word.\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')