# Sentiment Analysis Model

This model analyzes the sentiment of text input and classifies it as positive or negative.

## API Usage

### Input Format

```json
{
  "data": {
    "text": "Your text here for sentiment analysis"
  }
}
```

### Output Format

The model returns a prediction with confidence scores:

```json
{
  "prediction": "positive", // or "negative"
  "confidence": 0.95, // confidence score between 0 and 1
  "probabilities": {
    "negative": 0.05,
    "positive": 0.95
  }
}
```

### Error Response

If there's an error, the response will be:

```json
{
  "prediction": null,
  "confidence": 0.0,
  "error": "Error message here"
}
```

## Example Usage

```bash
curl -X POST "https://your-api-endpoint/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "data": {
      "text": "This is a fantastic product! I absolutely love it."
    }
  }'
```
