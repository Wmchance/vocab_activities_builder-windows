import os
import openai

def finish_the_conversation(OPENAI_API_KEY, word_str, destination_path):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Key words and phrases: {word_str}. \nCreate a horizontal word list using the key words. Add the text 'Word Bank:' above the word list.\n\nTopic: travel.\nCreate a two-sentence coversation between two people using the above topic.\nDon't use the key words in the conversation.\n\nAdd instructions telling the reader to complete the conversation using the words from the word list. ",
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
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')