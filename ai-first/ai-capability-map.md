## AI capabilities:
Conversational product suggestion, Typeahead search suggestion, Personalised product recommendation, Order tracking assistant.

## Selected:
Conversational product suggestion, Typeahead search suggestion.

## Table:

| Capability     | Intent (user) |   Inputs (this sprint)    |    Risk 1–5 (tag)   |   p95 ms  |  Est. cost/action  |  Fallback  | Selected |
|----------------|---------------|---------------------------|---------------------|-----------|--------------------|------------|----------|
|Conversational product suggestion|User finds products by describing his needs|User query(text) + inventory data|2 (low)|<=500 ms|0.07$|Show top category matches|yes|
|Typeahead search suggestion|user finds products while typing|User query text + product catalog + popularity data|2 (low)| <= 300 |0.0045$|Show popular products|yes|

## Why these two:

I selected Typeahead search suggestion and conversational product suggestion because both improve product discovery. Typeahead helps user find products faster just by typing some letters, while conversational suggestion allows users to describe their needs in natural language, providing personalised recommendations. Both capabilities are low risk to integrate using the existing product catalog. Together they enhance user experience and can indirectly reduce support contact rates by making it easier for users to find what they want without additional help.
