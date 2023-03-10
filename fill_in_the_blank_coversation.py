import os
import openai

def fill_in_the_blank_conversation(OPEN_API_KEY, word_str, destination_path):

    openai.api_key = OPEN_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'''Key words and phrases: {word_str}. \n
        Topic: Travel.\n
        Write a short dialogue between two people about the given topic and using the key words.\n
        Use CEFR A2 level English for the dialogue.\n
        In the dialogue, replace the key words with a space for students to fill in the missing word.
        ''',
        temperature=0.7,
        max_tokens=2084
        )

    response_text = response.choices[0]['text']

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Fill-in-the-Blank: Conversation\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: Use the words above to fill in the blanks in the conversation below\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')