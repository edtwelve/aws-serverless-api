# Proyecto: API Serverless para CV (AWS)

Este proyecto despliega una API RESTful sin servidor utilizando la pila "serverless" de AWS (API Gateway, Lambda y DynamoDB) para servir datos de un CV en formato JSON.

## Arquitectura

La API utiliza **API Gateway** como punto de entrada HTTP. Cuando se realiza una solicitud `GET` al endpoint `/cv`, API Gateway activa una función **Lambda** (escrita en Python). Esta función escanea una tabla de **DynamoDB** (`CV-Data`), recupera todos los ítems y los devuelve como una respuesta JSON.


## Tecnologías Utilizadas

* **AWS API Gateway:** Para crear, desplegar y gestionar la API RESTful (endpoint `GET /cv`).
* **AWS Lambda:** Para ejecutar el código de lógica de negocio (Python 3.12) sin necesidad de gestionar servidores.
* **AWS DynamoDB:** Como la base de datos NoSQL para almacenar los datos del CV.
* **AWS IAM:** Para gestionar de forma segura los permisos entre Lambda y DynamoDB (usando un Rol de Ejecución).

## Endpoint de la API

### `GET /v1/cv`

Recupera todos los datos almacenados del CV.

* **URL:** `https://b6dupztzie.execute-api.us-east-1.amazonaws.com/v1/cv`

### Respuesta de Ejemplo (JSON)

```json
[
    {
        "Role": "Interpreter",
        "Company": "Teleperformance",
        "Category": "Experience",
        "ItemID": "1"
    },
    {
        "Degree": "Computer Science and Engineering",
        "Institution": "Unicatolica",
        "Category": "Education",
        "ItemID": "1"
    },
    {
        "Name": "AWS Certified Cloud Practitioner",
        "IssuedBy": "Amazon Web Services",
        "Category": "Certifications",
        "ItemID": "1"
    }
]
```