import connexion

if __name__ == '__main__':
	app = connexion.FlaskApp(__name__, specification_dir='.')
	app.add_api('my_api.yaml')
	app.run(port=8080)
