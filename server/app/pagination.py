# coding: utf-8
from abc import ABCMeta, abstractproperty


class Pagination:
    __metaclass__ = ABCMeta

    @abstractproperty
    def is_start(self):
        pass

    @abstractproperty
    def is_end(self):
        pass

    @abstractproperty
    def prev(self):
        pass

    @abstractproperty
    def next_(self):
        pass

    @abstractproperty
    def page_count(self):
        pass

    @abstractproperty
    def total(self):
        pass

    @abstractproperty
    def items(self):
        pass


class PaginationSqlalchemy(Pagination):

    @property
    def prev(self):
        return self._pagination.prev_num

    @property
    def is_end(self):
        return not self._pagination.has_next

    @property
    def page_count(self):
        return self._pagination.pages

    @property
    def total(self):
        return self._pagination.total

    @property
    def next_(self):
        return self._pagination.next_num

    @property
    def is_start(self):
        return not self._pagination.has_prev

    @property
    def items(self):
        return self._pagination.items

    def __init__(self, pagination):
        self._pagination = pagination
