---
title: "Building a UCP-Powered Shopping Agent with Gemini"
description: "A technical tutorial on how to build a shopping agent powered by the Universal Commerce Protocol (UCP) and Google's Gemini. Learn how to leverage the power of AI to create a seamless and conversational shopping experience."
author: "webdesk"
date: 2024-08-02T10:00:00.000Z
tags:
  - ucp
  - gemini
  - ai
  - developers
  - tutorial
---

The Universal Commerce Protocol (UCP) and large language models (LLMs) like Google's Gemini are a match made in heaven. UCP provides the standardized language for e-commerce, and Gemini provides the conversational intelligence to create a truly seamless and agentic shopping experience. In this tutorial, we'll walk through the process of building a simple UCP-powered shopping agent with Gemini.

## Prerequisites

Before we begin, you'll need to have the following:

*   **A running UCP server**: Follow our "Getting Started with UCP: A Developer's Guide" to get a sample server up and running.
*   **A Google AI Studio API key**: You can get one for free from the [Google AI Studio website](https://aistudio.google.com/).
*   **The `google-generativeai` Python library**: You can install it with `pip install google-generativeai`.

## The Core Concept: From Natural Language to UCP

The core concept of our shopping agent is to take a natural language query from the user, use Gemini to translate it into a UCP-compliant API request, and then send that request to our UCP server.

Let's say a user says, "I want to buy a bouquet of red roses." Our agent will:

1.  **Parse the query**: Use Gemini to extract the key information from the user's query, such as the product they want to buy and the quantity.
2.  **Construct the UCP request**: Use the extracted information to construct a UCP-compliant JSON object for a checkout session.
3.  **Send the request**: Send the JSON object to the `/checkout-sessions` endpoint of our UCP server.
4.  **Return the response**: Parse the response from the server and present it to the user in a natural and conversational way.

## A Simple Python Implementation

Here's a simple Python script that demonstrates this concept:

```python
import google.generativeai as genai
import requests
import json
import os

# Configure the Gemini API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Set the UCP server URL
UCP_SERVER_URL = "http://localhost:8182"

def create_checkout_session(product_name, quantity):
    """Creates a UCP checkout session."""

    # Construct the UCP request body
    request_body = {
        "line_items": [
            {
                "item": {
                    "id": product_name.replace(" ", "_"),
                    "title": product_name.title()
                },
                "quantity": quantity
            }
        ],
        "buyer": {
            "full_name": "John Doe",
            "email": "john.doe@example.com"
        },
        "currency": "USD"
    }

    # Send the request to the UCP server
    response = requests.post(
        f"{UCP_SERVER_URL}/checkout-sessions",
        headers={
            "Content-Type": "application/json",
            "UCP-Agent": 'profile="https://agent.example/profile"',
            "request-signature": "test",
            "idempotency-key": "a-unique-key"
        },
        data=json.dumps(request_body)
    )

    return response.json()

def main():
    """The main function of the shopping agent."""

    # Get the user's query
    user_query = input("What would you like to buy? ")

    # Use Gemini to extract the product and quantity
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        f"Extract the product and quantity from the following sentence: '{user_query}'. Return the result as a JSON object with the keys 'product' and 'quantity'."
    )

    # Parse the JSON response from Gemini
    gemini_response = json.loads(response.text)
    product = gemini_response["product"]
    quantity = gemini_response["quantity"]

    # Create the UCP checkout session
    checkout_session = create_checkout_session(product, quantity)

    # Print the checkout session details
    print(json.dumps(checkout_session, indent=2))

if __name__ == "__main__":
    main()
```

## Running the Agent

To run the agent, save the code as `shopping_agent.py` and run it from your terminal:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
python shopping_agent.py
```

The agent will then prompt you for your query. Try entering "I want to buy a bouquet of red roses," and you should see a UCP checkout session created in response.

## The Future is Conversational

This is just a simple example, but it demonstrates the power of combining UCP and LLMs like Gemini. As these technologies continue to evolve, we can expect to see more and more sophisticated shopping agents that can understand our needs, make personalized recommendations, and even negotiate prices on our behalf. The future of e-commerce is conversational, and it's being built on the foundation of UCP.
