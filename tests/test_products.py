import unittest
from src.products import put_item

import boto3

class TestProductsCase(unittest.TestCase):

    dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4569/')

    @classmethod
    def setUpClass(cls):
        TestProductsCase.dynamodb.create_table(
            TableName='products',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

    def test_put_item(self):
        print("testing put_item.")
        table = TestProductsCase.dynamodb.Table('products')
        item = {
            'id': '1',
            'name': 'book1',
        }

        result = put_item(table, item)
        print(result)
        self.assertEqual(result['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
