# ControlStack (FastAPI + MongoDB)

A lean, containerized setup to manage and track expenses, incomes, and services — built the modern way.

## Features

- Create transactions
- Read transactions (all or single transaction)
- Update transactions
- Delete transactions
- MongoDB integration

## API Endpoints

### Get All transactions
`GET /transactions`

### Get Single transaction
`GET /transactions/{transaction_id}`

### Create transaction
`POST /transactions`

### Update transaction
`PUT /transactions/{transaction_id}`

### Delete transaction
`DELETE /transactions/{transaction_id}`

## Requirements

- Python 3.7+
- MongoDB

## Run

1. Clone or download this repository
2. Make sure docker is up and running:
   ```bash
   make build
   make up
   ```

The API will be available at `http://localhost:8000`

## API Documentation

The API includes automatic interactive documentation:

- **Swagger UI**: `http://localhost:8000/docs`

## Usage Examples

### Create an transaction
```bash
curl -X POST "http://localhost:8000/transactions" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample transaction",
    "description": "This is a sample transaction",
    "price": 29.99
  }'
```

### Get all transactions
```bash
curl -X GET "http://localhost:8000/transactions"
```

### Get a specific transaction
```bash
curl -X GET "http://localhost:8000/transactions/{transaction_id}"
```

### Update an transaction
```bash
curl -X PUT "http://localhost:8000/transactions/{transaction_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated transaction Name",
    "price": 39.99
  }'
```

### Delete an transaction
```bash
curl -X DELETE "http://localhost:8000/transactions/{transaction_id}"
```

## License

This project is licensed under the MIT License.
