import pickle
import numpy as np
from typing import Dict, Any
import os
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
model_path = script_dir / 'model.pkl'

# Load the model once when module is imported
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Predict sentiment (positive/negative) from text input.
    
    Args:
        input_data: Dictionary with text input
        
    Returns:
        Dictionary with prediction and confidence
    """
    try:
        # Extract text from input data
        text = input_data.get("text", "")
        if not text:
            raise ValueError("No text provided for sentiment analysis")
            
        # Simple feature extraction (example)
        features = np.array([
            len(text),  # Length of text
            text.count('!'),  # Number of exclamation marks
            text.count('?'),  # Number of question marks
            len([w for w in text.split() if w.isupper()])  # Number of uppercase words
        ]).reshape(1, -1)
        
        # Get prediction and probability
        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities))
        
        # Map prediction to sentiment
        sentiment = "positive" if prediction == 1 else "negative"
        
        return {
            "prediction": sentiment,
            "confidence": confidence,
            "probabilities": {
                "negative": float(probabilities[0]),
                "positive": float(probabilities[1])
            }
        }
        
    except Exception as e:
        return {
            "prediction": None,
            "confidence": 0.0,
            "error": str(e)
        }
