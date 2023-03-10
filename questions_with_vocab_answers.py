import os
import openai

def questions_with_vocab_answers(OPENAI_API_KEY, word_str, destination_path):
    
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Key words and phrases: "{word_str}". 
            Write an open-ended question for each of the key words. 
            The questions should not contain the key words. 
            The questions should be designed so that answers can use the key words.
            The questions should be at the CEFR A2 level.
            Do not provide answers to the questions.
            ''', 
        temperature=.5, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Answer with Vocab\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: Use the words above to answer the questions below\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')