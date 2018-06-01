import psycopg2
import sys

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        dbList = []

        try:
            conn = psycopg2.connect("dbname='test_db' user='postgres' host='192.168.99.100' port='5432' password=''")
            cur = conn.cursor()
            cur.execute("""SELECT title FROM products""")
            rows = cur.fetchall()
            for row in rows:
                dbList.append(row[0])
        except:
            dbList.append('Empty')

        return {
            'products': dbList
        }

class Users(Resource):
	def get(self):
		return {
			'users': [
				'John',
				'Bill',
				'Jack'
			]
		}

		
api.add_resource(Product, '/products')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
