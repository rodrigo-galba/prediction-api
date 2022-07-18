# prediction-api
 Python API to predict text (PT_BR)

## Setup

```
python -m venv venv
source .\venv\Scripts\activate
pip install -r .\requirements.txt
uvicorn main:app --reload     
```

## Endpoints

```
curl --request GET \
  --url http://localhost:8000/
```

- Predict

```
curl --request POST \
  --url http://localhost:8000/predict \
  --header 'Content-Type: application/json' \
  --data '{
	"message": "asdasdasdasdad"
}'
```