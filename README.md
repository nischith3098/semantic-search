# semantic-search
Please make sure that you have installed all the necessary modules as follows in your command prompt or terminal.

pip install requests

pip install beautifulsoup4

pip install openai

pip install pinecone-client

pip install streamlit

pip installsentence_transformers pinecone-client openai -q

**vectorization.py**

In summary, this code sets up and interacts with a Pinecone index for semantic search. It provides functions to add data to the index and find the nearest matches based on a query using sentence embeddings generated by the SentenceTransformer model.

**QnA.py**

In summary, this code sets up a way to generate answers to questions using the OpenAI API. The create_prompt function prepares a prompt string by combining the context and query, while the generate_answer function sends the prompt to the API and retrieves the generated answer.

**scrape.py**

In summary, this code provides functions to scrape text content from a given URL. It retrieves the HTML content, extracts the plain text, and splits it into smaller chunks based on the maximum character limit. This can be useful for processing and analyzing large amounts of text data from web pages.

**main.py**

Overall, the code creates a user interface using Streamlit to interact with the semantic search engine for question-answering. Users can either update the database by providing a URL or ask questions and receive answers based on the existing database.
