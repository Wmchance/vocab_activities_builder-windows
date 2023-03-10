import os
import openai

def new_sentences_same_meaning(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'''Key words and phrases: {word_str}.
        \nUse CEFR A2 level English to write one sentence for each of the key words.
        Below each sentence, add two blank lines.
        ''',
        temperature=0.5,
        max_tokens=2000,
        top_p=1
        )

    response_text = response.choices[0]['text']

    with open(destination_path, 'a') as fp:
        pass
        fp.write("New Sentences with the Same Meaning\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: For each sentence, write a new sentence that has the same meaning but uses different words.\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')