import os
import openai

def words_to_drawings(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Key words and phrases: {word_str}. \n\nPut each of the above words in a box. Make the box horizontal. Add the text 'Word Bank:' above the box.\n\nAdd the instructions telling students to draw one picture for each picture and write one sentence for each picture.\n\nAdd areas for students to complete their drawings and sentences.\n\nDon't complete the sentences. Leave this activity for students to complete.",
        temperature=0.68,
        max_tokens=2015,
        top_p=1
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Words to Drawings\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')