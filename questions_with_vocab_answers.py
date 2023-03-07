import os
import openai

def questions_with_vocab_answers(OPENAI_API_KEY, word_str):
    
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=f'''
            Make a word bank for the following words: "{word_str}". 
            Write instructions asking the students to write an answer for each of the questions. 
            Tell the students that they should use the words from the word bank in their answers.
            Write an open-ended question for each word in the word bank. 
            The questions should not contain the words from the word bank. 
            The questions should be designed so that answers can use the words from the word bank.
            The questions should be at the CEFR A2 level.
            Do not provide answers to the questions.
            ''', 
        temperature=.5, 
        max_tokens=2000
        )

    response_text = response.choices[0]['text']

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("Answer with Vocab\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')