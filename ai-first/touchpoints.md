## Conversational product suggestion:

## Problem statement: 

Users often struggle to describe exactly what they want in the products catalog, which may lead to frustration and abandoned searches.
A conversational AI that interprets user queries and suggests products in accordance to user's needs, can make product discovery faster.

## Happy path:

- User access the chat interface and type a query describing his needs.
- Front end captures the user's query.
- query is sent to the AI service alongside inventory data.
- AI processes the input and matches it to products using attributes and categories.
- AI ranks the suggestions based on relevance, availability, and popularity.
- AI returns a number of product suggestions to the frontend.
- Frontend displays suggestions to the user.
- User clicks on a suggested product.

## Grounding & guardrails:

Source of truth: Product catalog + product attributes.
Retrieval scope: Only current catalog items; no external websites or unrelated data or unavailable products.
Max context: Limit AI input to last 200 tokens of user query + product attributes.
Refuse outside scope: AI must decline suggestions for products not in catalog or unrelated requests.

## Human-in-the-loop

Escalation triggers: Queries AI cannot answer or inaccurate matches.
UI surface: Admin dashboard showing failed queries and AI confidence score.
Reviewer & SLA: Product manager or support agent reviews within 24 hours to improve AI prompts or fallback rules.

## Latency budget

Frontend captures and sends query: 50 ms
AI inference: 400 ms
Frontend renders suggestions: 50 ms
Total: 500 ms p95
Cache strategy: Store last 10 user queries with results to reduce repeated computation.

## Error & fallback behavior

If AI fails: show top category matches from catalog.
If catalog is empty: show popular products.

## PII handling

What leaves the app: Only user query text (no account info or payment data).
Redaction rules: Remove names, emails, phone numbers if included.
Logging policy: Log query text with product suggestions only; anonymized user ID.

## Success metrics

Product metric 1: Search-to-click conversion = (# of product clicks / # of queries) * 100
Product metric 2: Time-to-find-product = average time from query submission to product click
Business metric: Increase in sales = total revenue from suggested products / total revenue * 100

## Feasibility note

Data is available via existing product catalog API.
Use GPT-4o-mini or similar small LLM for inference.
Next prototype step: implement frontend chat box, connect to AI service, and validate suggestions on 50 sample queries.


## Typeahead Search Suggestions

## Problem statement

Users often abandon searches because they cannot quickly find the right product or don’t know the exact spelling of product names. This results in longer search times, and missed sales opportunities. Typeahead suggestions reduce friction by helping users find products as they type.

## Happy path

- User clicks the search bar on the ShopLite website.
- User begins typing a product name.
- The frontend captures the keystrokes and sends them to the AI service.
- The AI looks up the partial query against the product catalog index.
- AI ranks results by relevance, popularity, and availability.
- Suggestions are returned to the frontend.
- Suggestions appear instantly under the search bar.
- User clicks a suggestion to go directly to the product or category page.

## Grounding & guardrails

Source of truth: Product catalog metadata (name, category, tags, popularity).
Retrieval scope: Only existing SKUs in the catalog.
Max context: Last 50 characters of user query.
Refuse outside scope: If no matches, show “No matches” instead of guessing.

## Human-in-the-loop

Escalation triggers: If AI suggestions have <10% click-through rate for 3 consecutive days.
UI surface: Analytics dashboard for product team.
Reviewer & SLA: Product manager reviews within 48 hours and adjusts ranking signals or retraining.

## Latency budget

Frontend captures keystroke and sends: 50 ms
AI query + retrieval: 200 ms
AI ranking & response formatting: 30 ms
Frontend renders results: 20 ms
Total: 300 ms p95
Cache strategy: Cache top 1,000 most frequent queries to serve instantly on repeat.

## Error & fallback behavior

If AI service is down: fallback to keyword-based search index.
If query returns no results: display “Top trending products” or nearest category matches.

## PII handling

What leaves the app: Only search query text (no user IDs, no sensitive data).
Redaction rules: Remove accidental entries like email or phone numbers.
Logging policy: Store anonymized query text with click events for analytics.

## Success metrics

Product metric 1: Search-to-click rate = (# of searches with a clicked suggestion / total searches) * 100
Product metric 2: Time-to-result = average time from typing query to clicking a suggestion
Business metric: Conversion uplift = (revenue from search sessions / total revenue) * 100

## Feasibility note

Data available from the existing product catalog and search API.
Use GPT-4o-mini or Llama 3.1 Instruct for ranking queries.
Next prototype step: integrate keystroke logging, connect to AI for retrieval, and benchmark latency on 100 sample queries.
