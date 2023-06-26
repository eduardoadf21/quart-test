import sqlite3

import click
from quart import current_app, g

# g is a special object unique for each request
async def get_db():
    g.db = await sqlite3.connect(
        current_app.config['DATABASE'],
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = await sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

async def init_db():
    db = await get_db()

    async with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

"""Clear the existing data and create new tables."""
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

