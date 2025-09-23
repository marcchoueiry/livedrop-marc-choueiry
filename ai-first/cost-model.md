## Assumptions
- Model: GPT-3.5 at $0.0015 / 1K prompt tokens, $0.002 / 1K completion tokens
- Conversational suggestion: Avg tokens in = 300, Avg tokens out = 150
- Typeahead search suggestion: Avg tokens in = 100, Avg tokens out = 50
- Requests/day: 5,000
- Cache hit rate: 20% (apply miss cost only)

## Calculation

Conversational product suggestion
Cost/action = (300/1000 * 0.0015) + (150/1000 * 0.002)  
Cost/action = 0.00045 + 0.0003 = $0.00075

Daily cost = 0.00075 * 5,000 * (1 - 0.2)  
Daily cost = 0.00075 * 4,000 = $3.00/day

Typeahead search suggestion 
Cost/action = (100/1000 * 0.0015) + (50/1000 * 0.002)  
Cost/action = 0.00015 + 0.0001 = $0.00025

Daily cost = 0.00025 * 5,000 * (1 - 0.2)  
Daily cost = 0.00025 * 4,000 = $1.00/day

## Results
- Conversational product suggestion: Cost/action = $0.00075, Daily = $3.00
- Typeahead search suggestion: Cost/action = $0.00025, Daily = $1.00

## Cost lever if over budget
- Reduce input tokens by limiting context length.  
- Cache common queries to reduce duplicate calls.  
- Use embeddings or a lighter model for typeahead suggestions.
