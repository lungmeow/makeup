# coding: utf-8
from sqlalchemy import Integer, String, Enum

from app import db


class Solid(db.Model):
    __tablename__ = 'solid'
    id = db.Column(Integer(), autoincrement=True, primary_key=True)
    title = db.Column(String(length=25), nullable=False)
    img = db.Column(String(length=1000), nullable=False)
    description = db.Column(String(length=250), nullable=False)
    uri = db.Column(String(length=1000), nullable=False)
    level = db.Column(Enum('basic', 'advanced'), nullable=False)

    def to_json(self):
        json_solid = {
            'id': self.id,
            'img': self.img,
            'title': self.title,
            'description': self.description,
            'uri': self.uri,
            'level': self.level
        }
        return json_solid

    @classmethod
    def generate_fake(cls, count=100):
        from random import seed, choice
        import forgery_py
        level_choices = ['basic', 'advanced']
        seed()
        for i in range(count):
            s = cls(
                title=forgery_py.lorem_ipsum.title(),
                img=forgery_py.internet.domain_name(),
                description=forgery_py.lorem_ipsum.sentence(),
                uri=forgery_py.internet.domain_name(),
                level=choice(level_choices),
            )
            db.session.add(s)
            db.session.commit()
