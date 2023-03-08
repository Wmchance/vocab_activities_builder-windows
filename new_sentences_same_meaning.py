import os
import openai

def new_sentences_same_meaning(OPENAI_API_KEY, word_str):

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Key words and phrases: {word_str}.\nTopic: Travel\n\nCreate an activity for esl students that uses the above information to create example sentences for each word and asks students to write new sentences for each of the examples that use different words.\nDon't provide the new sentences for students, but create a blank line for each sentence that they are to create.",
        temperature=0.5,
        max_tokens=2000,
        top_p=1
        )

    response_text = response.choices[0]['text']

    # add spaces blanks to text manually so that ChatGPT is relied on for this part
    # add a word bank

    with open('worksheet.txt', 'a') as fp:
        pass
        fp.write("New Sentences with the Same Meaning\n")
        fp.write(" \n")
        fp.write(f'{response_text}\n')
        fp.write(' \n')
        fp.write('--------------------------------------------------------------------------------\n')
        fp.write(' \n')