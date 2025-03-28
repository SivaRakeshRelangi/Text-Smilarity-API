# Model to compute similarity
!pip install sentence-transformers  # Ensure the necessary package is installed

import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load dataset
df = pd.read_csv("DataNeuron_Text_Similarity.csv")

# Handle missing data by filling NaN with empty strings or dropping rows
df['text1'] = df['text1'].fillna('')
df['text2'] = df['text2'].fillna('')

# Function to compute similarity score
def compute_similarity(text1, text2):
    if not text1 or not text2:  # Skip empty text entries
        return 0.0
    
    # Encode the texts to embeddings
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    
    # Compute the cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    
    # Ensure similarity score is between 0 and 1
    return max(0.0, min(1.0, similarity))  # Clip the result to the range [0, 1]
    # return util.pytorch_cos_sim(embedding1, embedding2).item()

# Apply similarity function
df["similarity_score"] = df.apply(lambda x: compute_similarity(x["text1"], x["text2"]), axis=1)

# Ensure the 'data' directory exists before saving the file
import os
if not os.path.exists('data'):
    os.makedirs('data')

# Save processed dataset
df.to_csv("data/processed_train_data.csv", index=False)

print("Processing complete! Saved as data/processed_train_data.csv")
