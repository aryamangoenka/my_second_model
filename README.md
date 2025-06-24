# Sentiment Analysis Model

This model analyzes text sentiment and classifies it as positive or negative.

## API Usage

```json
{
  "data": {
    "text": "Your text here for sentiment analysis"
  }
}
```

## Response Format

```json
{
  "prediction": "positive" or "negative",
  "confidence": 0.XX,
  "probabilities": {
    "negative": 0.XX,
    "positive": 0.XX
  }
}
```
