# coding: utf-8


from flask import jsonify, request, url_for

from app.api.v1 import api_v1
from app.service.solidsrv import SolidServiceDBImp as SolidService

solid_service = SolidService()


@api_v1.route('/solids/<int:solid_id>')
def get_solid(solid_id):
    solid = solid_service.get_solid_by_id(solid_id)
    return jsonify(solid)


@api_v1.route('/solids/')
def get_solids():
    default_page = '1'
    default_size = '10'
    default_level = 'basic'

    level = request.args.get('level', default_level)
    keyword = request.args.get('keyword')
    page = request.args.get('page', default_page)
    size = request.args.get('size', default_size)

    if level != 'basic' and level != 'advanced':
        level = default_level

    if not page.isdigit():
        page = default_page
    page = int(page)
    if page < 1:
        page = int(default_page)

    if not size.isdigit():
        size = default_size
    size = int(size)
    if size < 1:
        size = int(default_size)

    solids = solid_service.get_solids_by_keyword(keyword, level, page, size)
    resp = {
        'c': 0,
        'data': [solid.to_json() for solid in solids.items],
        'total': solids.total,
        'paging': {
            'is_start': solids.is_start,
            'is_end': solids.is_end,
            'prev': url_for('api_v1.get_solids', _external=True, level=level, keyword=keyword, page=solids.prev, size=size),
            'next': url_for('api_v1.get_solids', _external=True, level=level, keyword=keyword, page=solids.next_, size=size),
            'count': solids.page_count,
        }
    }
    return jsonify(resp)
