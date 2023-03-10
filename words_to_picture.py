import os
import openai

def words_to_picture(OPENAI_API_KEY, word_str, destination_path):
    
    openai.api_key = OPENAI_API_KEY

    word_list = list(word_str.split(", "))

    # response = openai.Completion.create(
    #     model="text-davinci-003", 
    #     prompt=f'''
    #         Key words: "{word_str}". 
    #         \nMake a three column table
    #         \nAdd one row for each key word
    #         \nAdd a header row.
    #         \nIn the header row, the first column should be labeled "Word", the second "Picture", and the third "sentence"
    #         ''', 
    #     temperature=.5, 
    #     max_tokens=2000
    #     )

    # response_text = response.choices[0]['text']

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Words to Pictures\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: \n")
        fp.write("Step 1: For each word in the word bank, draw one picture. \n")
        fp.write("Step 2: Write a sentence for each picture using the word. \n")
        fp.write(" \n")
        fp.write(" \n")
        for word in word_list:
            fp.write(f'{word.capitalize()}:\n')
            fp.write('Picture:\n')
            fp.write(' \n')
            fp.write(' \n')
            fp.write('Sentence:_______________________________________________________________________\n')
            fp.write(' \n')
            fp.write('**************************\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')