---
title: "Getting Started with UCP: A Developer's Guide"
description: "A step-by-step guide for developers to get started with the Universal Commerce Protocol (UCP). Learn how to set up your environment, create a sample project, and integrate with UCP."
author: "webdesk"
date: 2024-07-30T10:00:00.000Z
tags:
  - ucp
  - developers
  - guide
  - tutorial
---

The Universal Commerce Protocol (UCP) is an open-source standard poised to revolutionize the world of e-commerce. For developers, it presents a unique opportunity to build the next generation of shopping experiences. This guide will walk you through the process of getting started with UCP, from setting up your environment to creating a sample project.

## Prerequisites

Before you begin, you'll need to have the following installed:

*   **Python 3.8+**: UCP's reference implementation is written in Python.
*   **Git**: For cloning the UCP repositories.
*   **`uv`**: A fast Python package installer and resolver. You can install it with `pip install uv`.

## Setting Up Your Environment

First, let's set up your development environment. We'll start by cloning the necessary UCP repositories from GitHub.

```bash
mkdir ucp-project
cd ucp-project
git clone https://github.com/Universal-Commerce-Protocol/python-sdk.git sdk/python
git clone https://github.com/Universal-Commerce-Protocol/samples.git
```

Next, let's install the dependencies for the Python SDK and the sample server.

```bash
cd sdk/python
uv sync
cd ../../samples/rest/python/server
uv sync
cd ../../../../
```

## Running the Sample Server

Now that you have the necessary code and dependencies, let's run the sample UCP server. This server simulates a business backend and comes with a sample product database.

First, create a local database with sample products:

```bash
mkdir /tmp/ucp_test
uv run import_csv.py \
    --products_db_path=/tmp/ucp_test/products.db \
    --transactions_db_path=/tmp/ucp_test/transactions.db \
    --data_dir=samples/rest/test_data/flower_shop
```

Now, start the server on port 8182:

```bash
uv run samples/rest/python/server/server.py \
   --products_db_path=/tmp/ucp_test/products.db \
   --transactions_db_path=/tmp/ucp_test/transactions.db \
   --port=8182 &
SERVER_PID=$!
```

## Interacting with the UCP Server

With the server running, you can now interact with it using `curl` or any other HTTP client. Let's start by discovering the business's capabilities.

```bash
export SERVER_URL=http://localhost:8182
curl -s -X GET $SERVER_URL/.well-known/ucp
```

This will return a JSON object containing information about the services and capabilities supported by the server.

Next, let's create a checkout session.

```bash
curl -s -X POST "$SERVER_URL/checkout-sessions" \
-H 'Content-Type: application/json' \
-H 'UCP-Agent: profile="https://agent.example/profile"' \
-H 'request-signature: test' \
-H 'idempotency-key: 0b50cc6b-19b2-42cd-afee-6a98e71eea87' \
-d '{"line_items":[{"item":{"id":"bouquet_roses","title":"Red Rose"},"quantity":1}],"buyer":{"full_name":"John Doe","email":"john.doe@example.com"},"currency":"USD"}'
```

This will create a checkout session and return a JSON object with the session details.

## Next Steps

This guide has shown you the basics of setting up your environment and interacting with a UCP server. From here, you can start to explore the other capabilities of UCP, such as:

*   **Applying discounts**: Add a `discounts` object to your checkout request to apply discounts to the order.
*   **Handling payments**: Integrate with a payment provider to handle the payment process.
*   **Managing orders**: Use the order management capabilities to track the status of an order.

The Universal Commerce Protocol is a powerful new standard that is set to change the face of e-commerce. By getting started with it today, you can be at the forefront of this exciting new wave of innovation.
