import os
import openai

def finish_the_conversation(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'''Key words and phrases: {word_str}.\n
        Topic: travel.\n
        Create a two-sentence coversation between two people using the above topic.\n
        Don't use the key words in the conversation.\n
        ''',
        temperature=0.7,
        max_tokens=2061,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open(destination_path, 'a') as fp:
        pass
        fp.write("Finish the Conversation\n")
        fp.write(" \n")
        fp.write("Word Bank:\n")
        fp.write(f'{word_str}\n')
        fp.write(" \n")
        fp.write("Instructions: Use the words above to finish the conversation below\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write('________________________________________________________________________________\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')