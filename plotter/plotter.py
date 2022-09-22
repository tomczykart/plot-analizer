from app import app, db
from app.models import User, search_query

#register commands for flask shell for convinient tesing
@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'User':User, 'search_query':search_query}
