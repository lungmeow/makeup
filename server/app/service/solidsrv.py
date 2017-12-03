# coding: utf-8
import abc
from app.models import Solid
from app.pagination import PaginationSqlalchemy as Pagination


class SolidService:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_solid_by_id(self, solid_id):
        pass

    @abc.abstractmethod
    def get_solids_by_keyword(self, keyword, level, page, size):
        pass


class SolidServiceDBImp(SolidService):

    def get_solid_by_id(self, solid_id):
        return Solid.query.get(solid_id)

    def get_solids_by_keyword(self, keyword, level, page, size):
        query = Solid.query
        if keyword:
            query = query.filter(Solid.title.like('%' + keyword + '%'))
        if level:
            query = query.filter(Solid.level == level)
        query = query.order_by(Solid.id)
        return Pagination(query.paginate(page=page, per_page=size))
