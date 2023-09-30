from flaskblog import create_app

# Creating app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
