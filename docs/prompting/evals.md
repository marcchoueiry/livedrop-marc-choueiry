# RAG System Evaluation

This file is meant as a simple checklist to test if my RAG system works properly. I divided it into 3 sections: retrieval quality, response quality, and some edge cases. The idea is that when I run my system, I can ask these questions and manually check if the behavior is correct.

---

## Retrieval Quality Tests (10 tests)

Here I just want to see if the system pulls the correct documents when I ask a question. If it doesn’t, then the retrieval part is not working well.

| Test ID | Question | Expected Documents | Pass Criteria |
|---------|----------|-------------------|---------------|
| R01 | How do I create a seller account on Shoplite? | Seller Account Setup and Management | Retrieved docs should contain this title clearly |
| R02 | What are Shoplite’s return policies? | Return and Refund Policies | Retrieved doc is relevant and contains refund/return details |
| R03 | How can I track my order delivery status? | Order Tracking and Delivery | Correct doc about tracking and delivery is retrieved |
| R04 | What security measures protect payment info? | Payment Methods and Security | Should pull doc that mentions encryption and safe checkout |
| R05 | Can I edit my personal info after registration? | User Registration and Account Management | Retrieval must show the limits on editing name/date of birth |
| R06 | How do sellers manage their product inventory? | Inventory Management for Sellers | Retrieval is correct if it brings the inventory doc |
| R07 | What fees does Shoplite charge sellers? | Commission and Fee Structure | Retrieval should include fees/commission details |
| R08 | How can I leave a product review? | Product Reviews and Ratings | Should bring doc that explains reviews and rating rules |
| R09 | Does Shoplite have mobile app features? | Mobile App Features | Retrieval correct if the app features doc is shown |
| R10 | How are promotional codes used in checkout? | Promotional Codes and Discounts | Retrieval must bring the doc about applying promo codes |

---

## Response Quality Tests (15 tests)

Here I’m checking not just the retrieval, but also the answer. It should have the right keywords, avoid wrong terms, and actually answer in a useful way.

| Test ID | Question | Required Keywords | Forbidden Terms | Expected Behavior |
|---------|----------|-------------------|-----------------|-------------------|
| Q01 | How do I change my password on Shoplite? | ["old password", "new password", "success message"] | ["automatic reset"] | Must explain the password change process with the success message |
| Q02 | What payment options are available on Shoplite? | ["credit card", "PayPal", "secure checkout"] | ["cash only"] | Should mention the payment methods and that it’s secure |
| Q03 | How can I apply a promo code during checkout? | ["apply", "checkout", "discount applied"] | ["automatic discounts"] | Clear explanation of how promo codes are applied |
| Q04 | What steps are needed to become a seller? | ["seller registration", "business verification", "2-3 business days"] | ["instant approval"] | Must mention seller verification and approval time |
| Q05 | How can I contact Shoplite support? | ["help center", "ticket", "response time"] | ["no support"] | Must show support options and expected response |
| Q06 | How does Shoplite handle refunds? | ["30-day return window", "refund authorization", "refund process"] | ["no refunds"] | Should explain 30-day policy and steps |
| Q07 | What kind of seller fees exist on Shoplite? | ["commission", "final value fee", "subscription"] | ["free forever"] | Needs to explain fees realistically |
| Q08 | How do sellers keep track of stock? | ["inventory", "update quantities", "real-time"] | ["no inventory system"] | Explain inventory management features |
| Q09 | Can I check my order status after purchase? | ["order tracking", "status update", "delivery"] | ["no tracking available"] | Must clearly explain how order tracking works |
| Q10 | What privacy protections does Shoplite have? | ["data protection", "encryption", "privacy policy"] | ["no privacy policy"] | Should describe protections and privacy guidelines |
| Q11 | How do I submit a product review? | ["review", "rating", "guidelines"] | ["anonymous posting without rules"] | Needs to cover review submission rules |
| Q12 | Can I edit my name or birthday in account settings? | ["limited changes", "wait 1 month", "2 times"] | ["unlimited changes"] | Must mention limits on personal info edits |
| Q13 | How do sellers adjust product prices? | ["update price", "inventory", "seller dashboard"] | ["price fixed forever"] | Should mention the seller dashboard and editing options |
| Q14 | How can I download and use Shoplite’s mobile app? | ["mobile app", "download", "notifications"] | ["desktop only"] | Must explain mobile app availability and main features |
| Q15 | What happens if I enter an expired promo code? | ["invalid", "error message", "not applied"] | ["automatic acceptance"] | Must explain that expired codes are rejected |

---

## Edge Case Tests (5 tests)

Finally, I want to see how the system behaves in special cases, like when the question doesn’t exist or when it’s confusing.

| Test ID | Scenario | Expected Response Type |
|---------|----------|----------------------|
| E01 | Question not in knowledge base (e.g., “Who is the CEO of Shoplite?”) | Refusal with explanation like “Not in documentation” |
| E02 | Ambiguous question (e.g., “How do I manage my account?”) | Assistant should ask for clarification |
| E03 | Very long or multi-part question | Assistant should break it down and answer what is possible |
| E04 | Question mixing unrelated topics (e.g., “How do I return an order and change my password at the same time?”) | Assistant should handle each part separately or ask clarification |
| E05 | Empty question or nonsense input | Assistant should respond politely asking user to rephrase |

---
