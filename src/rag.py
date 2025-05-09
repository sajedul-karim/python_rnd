import vertexai
from vertexai.language_models import TextEmbeddingModel
import os
import singlestoredb as s2
import json

# Set the path to your service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "src/rag_service_key.json"

# Initialize Vertex AI with your project ID
PROJECT_ID = "gen-lang-client-0285648918"
vertexai.init(project=PROJECT_ID, location="us-central1")

# Function to insert data into the database
def insert_data(prompt, embedding_values):
    # Create a connection to the database
    with s2.connect("sajedul-65545:G1LldD96ETBvYope13qieme8cyJv3TMN@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/db_sajedul_d86d8") as conn:
        # Convert embedding values to JSON string
        embedding_json = json.dumps(embedding_values)
        # Prepare data for insertion
        data = (prompt, embedding_json)
        # SQL statement with placeholders
        stmt = 'INSERT INTO myvectortable (text, vector) VALUES (%s, JSON_ARRAY_PACK(%s))'
        with conn.cursor() as cur:
            cur.execute(stmt, data)
            print("Data inserted successfully")

# Function to search using embedding with dot_product
def search_embeddings(query_text):
    # Generate embedding for search query
    query_embedding = embedding_model.get_embeddings([query_text])[0].values
    # Convert embedding to JSON array format
    query_vector = json.dumps(query_embedding)
    # SQL query with dot_product function
    stmt = '''
    SELECT text, dot_product(vector, JSON_ARRAY_PACK(%s)) AS score
    FROM myvectortable
    ORDER BY score DESC
    LIMIT 5;
    '''

    print(stmt)
    print(query_vector)
    # Create a connection to the database
    with s2.connect("sajedul-65545:G1LldD96ETBvYope13qieme8cyJv3TMN@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/db_sajedul_d86d8") as conn:
        with conn.cursor() as cur:
            cur.execute(stmt, (query_vector,))
            results = cur.fetchall()
            print(f"Results count: {len(results)}")
            for row in results:
                print(f"Text: {row[0]}, Score: {row[1]}")

# Initialize the embedding model
embedding_model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")

# Define your prompt
prompt = "Hello aayaz"

# # Generate text embeddings
embeddings = embedding_model.get_embeddings([prompt])
embedding_values = embeddings[0].values

# # Insert data into the database
insert_data(prompt, embedding_values)

# Perform search
search_embeddings("Hello")

print('Search query vector generated')
