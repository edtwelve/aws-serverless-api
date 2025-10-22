import json
import boto3
from decimal import Decimal

# Clase especial para convertir Decimales de DynamoDB a JSON
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

# Inicializa el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CV-Data')

def lambda_handler(event, context):

    try:
        # table.scan() lee los items de la tabla.
        response = table.scan()

        items = response.get('Items', [])

        # Devuelve una respuesta exitosa - API Gateway
        return {
            'statusCode': 200,
            'headers': {
                # Permitir llamada de desde cualquier sitio web
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET'
            },
            'body': json.dumps(items, cls=DecimalEncoder)
        }

    except Exception as e:
        # errores
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }