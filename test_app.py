from fastapi.testclient import TestClient
from app import app
client=TestClient(app)
payload={"Pclass":3,"Sex":"male","Age":22,"SibSp":1,"Parch":0,"Fare":7.25,"Embarked":"S"}
def test_root(): assert client.get("/").status_code==200
def test_health():
 r=client.get("/health"); assert r.status_code==200 and r.json()["model_loaded"] is True
def test_predict():
 r=client.post("/predict",json=payload); assert r.status_code==200
 b=r.json(); assert b["prediction"] in [0,1] and 0<=b["probability"]<=1 and .5<=b["confidence"]<=1
def test_invalid_pclass():
 bad=payload.copy(); bad["Pclass"]=5; assert client.post("/predict",json=bad).status_code==422
