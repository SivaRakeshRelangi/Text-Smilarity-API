# Flask API for predictionscore
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
app = Flask(__name__)

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(text1, text2):
    # Encode the input texts into embeddings (numerical vector representations)
    embedding1 = model.encode(text1, convert_to_tensor=True)
    embedding2 = model.encode(text2, convert_to_tensor=True)
    # Compute the cosine similarity
    similarity = util.pytorch_cos_sim(embedding1, embedding2).item()
    
    # Ensure similarity score is between 0 and 1
    return max(0.0, min(1.0, similarity))
@app.route('/')
def home():
    return "Welcome to the Text Similarity API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Extract the two texts (text1 and text2) from the request body
    text1 = data.get("text1", "") # Default to empty string if text1 is not provided
    text2 = data.get("text2", "")
    
    similarity_score = compute_similarity(text1, text2)
    return jsonify({"similarity score": similarity_score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    