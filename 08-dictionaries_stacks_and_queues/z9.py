mobile_phone = {
    "ram": 4,
    "battery_capacity": 3400,
    "review": 3.9,
    "model": "Xiaomi Redmi Note 5",
    "has_nfc": False,
    "derivative_products": [
        "Mi 5",
        "Mi Note 4"
    ],
}

for item in mobile_phone.items():
    print(f"{item[0]} : {item[1]}")