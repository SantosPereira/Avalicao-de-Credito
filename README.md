# Avaliação de Crédito

Esse é um modelo de Machine Learning que pode ser acessado por API Rest e é capaz de
predizer com certa acurácia a possibilidade de aprovação numa avaliação de crédito.

[Dataset no Kaggle](https://www.kaggle.com/datasets/ppb00x/credit-risk-customers)

## Uso

Primeiro é necessário a instalação das depêndencias com o comando:

~~~bash
pip install -r requirements.txt
~~~

Após instalar as depêndencias, é necessário rodar a API com o comando: 

~~~bash
uvicorn "main:app"
~~~

Para consultar a API é necessário enviar uma requisição POST pra o endpoint:

~~~bash
http://localhost:8000/model
~~~

tendo como corpo da requisição um json com formato como no exemplo:

~~~json
{
    "duration": 15.0,
    "credit_amount": 806.0,
    "installment_commitment": 4.0,
    "residence_since": 4.0,
    "age": 22.0,
    "existing_credits": 1.0,
    "num_dependents": 1.0,
    "checking_status_0<=X<200": false,
    "checking_status_<0": true,
    "checking_status_>=200": false,
    "checking_status_no checking": false,
    "credit_history_all paid": false,
    "credit_history_critical/other existing credit": false,
    "credit_history_delayed previously": false,
    "credit_history_existing paid": true,
    "credit_history_no credits/all paid": false,
    "purpose_business": true,
    "purpose_domestic appliance": false,
    "purpose_education": false,
    "purpose_furniture/equipment": false,
    "purpose_new car": false,
    "purpose_other": false,
    "purpose_radio/tv": false,
    "purpose_repairs": false,
    "purpose_retraining": false,
    "purpose_used car": false,
    "savings_status_100<=X<500": false,
    "savings_status_500<=X<1000": false,
    "savings_status_<100": true,
    "savings_status_>=1000": false,
    "savings_status_no known savings": false,
    "employment_1<=X<4": true,
    "employment_4<=X<7": false,
    "employment_<1": false,
    "employment_>=7": false,
    "employment_unemployed": false,
    "personal_status_female div/dep/mar": true,
    "personal_status_male div/sep": false,
    "personal_status_male mar/wid": false,
    "personal_status_male single": false,
    "other_parties_co applicant": false,
    "other_parties_guarantor": false,
    "other_parties_none": true,
    "property_magnitude_car": false,
    "property_magnitude_life insurance": true,
    "property_magnitude_no known property": false,
    "property_magnitude_real estate": false,
    "other_payment_plans_bank": false,
    "other_payment_plans_none": true,
    "other_payment_plans_stores": false,
    "housing_for free": false,
    "housing_own": true,
    "housing_rent": false,
    "job_high qualif/self emp/mgmt": false,
    "job_skilled": false,
    "job_unemp/unskilled non res": false,
    "job_unskilled resident": true,
    "own_telephone_none": true,
    "own_telephone_yes": false,
    "foreign_worker_no": false,
    "foreign_worker_yes": true
}
~~~

**Ou usar a [collection](./docs/Requisi%C3%A7%C3%B5es.postman_collection.json) para postman**
