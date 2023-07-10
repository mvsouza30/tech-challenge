curl -X POST \
      'https://api.mercadopago.com/v1/payments' \
       -H 'Authorization: Bearer TEST-6548685724317480-070618-b0584689f0b9752493897144dc66aec7-130024145 \
       -H 'Content-Type: application/json' \ 
      -d '{
  "additional_info": {
    "items": [
      {
        "id": "MLB2907679857",
        "title": "Point Mini",
        "description": "Producto Point para cobros con tarjetas mediante bluetooth",
        "picture_url": "https://http2.mlstatic.com/resources/frontend/statics/growth-sellers-landings/device-mlb-point-i_medium@2x.png",
        "category_id": "electronics",
        "quantity": 1,
        "unit_price": 58.8
      }
    ],
    "payer": {
      "first_name": "Test",
      "last_name": "Test",
      "phone": {
        "area_code": 11,
        "number": "987654321"
      },
      "address": {}
    },
    "shipments": {
      "receiver_address": {
        "zip_code": "12312-123",
        "state_name": "Rio de Janeiro",
        "city_name": "Buzios",
        "street_name": "Av das Nacoes Unidas",
        "street_number": 3003
      }
    }
  },
  "description": "Payment for product",
  "external_reference": "MP0001",
  "installments": 1,
  "metadata": {},
  "payer": {
    "entity_type": "individual",
    "type": "customer",
    "identification": {}
  },
  "payment_method_id": "visa",
  "token": "ff8080814c11e237014c1ff593b57b4d",
  "transaction_amount": 58.8
}'
