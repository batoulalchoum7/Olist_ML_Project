# Task 01 — Dataset & Database Setup

## Objective

Understand the Olist Brazilian e-commerce dataset, its tables and relationships, load the dataset into a local relational database, and verify the database using SQL queries and JOIN operations.

## Dataset

The Olist dataset contains information about orders, customers, products, sellers, payments, reviews, and geolocation.

### Main Tables

| Table                          |      Rows |
| ------------------------------ | --------: |
| `orders`                       |    99,441 |
| `customers`                    |    99,441 |
| `order_items`                  |   112,650 |
| `products`                     |    32,951 |
| `sellers`                      |     3,095 |
| `order_payments`               |   103,886 |
| `order_reviews`                |    99,224 |
| `geolocation`                  | 1,000,163 |
| `product_category_translation` |        71 |

## Main Relationships

* `orders.order_id` → `order_items.order_id`
* `orders.customer_id` → `customers.customer_id`
* `order_items.product_id` → `products.product_id`
* `order_items.seller_id` → `sellers.seller_id`

## Database Setup

The dataset was loaded into a local PostgreSQL database named:

```text
olist
```

The tables were successfully loaded and verified using SQL queries.

## JOIN Verification

A JOIN between orders and customers was used to verify the relationship between the tables:

```sql
SELECT
    o.order_id,
    o.customer_id,
    c.customer_unique_id,
    o.order_status
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
LIMIT 10;
```

The query successfully returned records from both related tables.

## Problem Understanding

The machine learning problem is to predict whether an order will be delivered **late or on time**.

The target label will be created in a later task by comparing the actual delivery date with the estimated delivery date.

EDA and model development are outside the scope of Task 01.

## Completion

* [x] Dataset understood
* [x] CSV files loaded
* [x] PostgreSQL database created
* [x] Tables verified
* [x] Relationships understood
* [x] SQL JOIN tested
* [x] Machine le
