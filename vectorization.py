import pinecone
from sentence_transformers import SentenceTransformer, util
import scrape as sr
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key="your_api_key", environment='env_name')
index = pinecone.Index("your-index-name")

index.describe_index_stats()

def addData(corpusData, url):
    id = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk = corpusData[i]
        chunkInfo = (str(id+i),
                     model.encode(chunk).tolist(),
                     {'title' : url, 'context': chunk})
        index.upsert(vectors = [chunkInfo])

def find_match(query, k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k = k, include_metadata= True)
    return [result['matches'][i]['metadata']['title']for i in range(k)],[result['matches'][i]['metadata']['context']for i in range(k)]
