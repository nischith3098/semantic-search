import openai
openai.api_key="api_key"
def create_prompt(context,query):
    header = "Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text and requires some latest information to be updated, print 'Sorry! no sufficient context to answer your query' \n"
    return header + context + "\n\n" + query + "\n"

def generate_answer(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,   
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop = ['END']
    )
    return (response.choices[0].text).strip()
