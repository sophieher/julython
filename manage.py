from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell

from food_mood import app as ap
import food_mood.models

app = ap

from food_mood.models import db

migrate = Migrate(app, db)


@MigrateCommand.command
def check_defaults(*a, **kw):
    '''compare db server defaults to SQLAlchemy models'''
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'tools'))
    import pg_default_col_comparer
    pg_default_col_comparer.run(app)


def _make_context():
    print('connected to db: {}'.format(db.get_engine().url))
    return dict(app=app, db=db, models=food_mood.models)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run()
