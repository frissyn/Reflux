from app import db
from app import app

try:
    db.create_all(bind="__all__")
except Exception as e:
    print(f"DB Bind Error: {e}")

app.run(host="0.0.0.0", port=8080, debug=False)