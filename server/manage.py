# coding: utf-8

import os
from app import create_app, db
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    from app.models import Solid
    return dict(app=app, db=db, Solid=Solid)

manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
