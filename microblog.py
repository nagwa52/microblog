from app import create_app, db, cli
from app.user_app import Client, Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': Client, 'Post' :Post}