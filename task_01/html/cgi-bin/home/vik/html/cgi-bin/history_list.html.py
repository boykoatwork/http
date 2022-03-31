# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1644260639.6555986
_enable_loop = True
_template_filename = '/home/vik/html/cgi-bin/history_list.html'
_template_uri = '/home/vik/html/cgi-bin/history_list.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        h_list = context.get('h_list', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Page Title</title>\n        <meta charset="UTF-8">\n    </head>\n    \n    <body>\n    <h1>Это - история посещений сайтов</h1>\n\n<ul>\n\n')
        for title, url, dt in h_list:
            __M_writer('\n')
            if len(title) < 1:
                __M_writer('        <li>')
                __M_writer(str(dt))
                __M_writer(' <a href = "')
                __M_writer(str(url))
                __M_writer('" > ')
                __M_writer(str(url))
                __M_writer(' </a></li>\n')
            else:
                __M_writer('        <li>')
                __M_writer(str(dt))
                __M_writer(' <a href = "')
                __M_writer(str(url))
                __M_writer('" > ')
                __M_writer(str(title))
                __M_writer(' </a></li>\n')
            __M_writer('\n')
        __M_writer('\n\n</ul> \n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/vik/html/cgi-bin/history_list.html", "uri": "/home/vik/html/cgi-bin/history_list.html", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 13, "25": 14, "26": 15, "27": 16, "28": 16, "29": 16, "30": 16, "31": 16, "32": 16, "33": 16, "34": 17, "35": 18, "36": 18, "37": 18, "38": 18, "39": 18, "40": 18, "41": 18, "42": 20, "43": 22, "49": 43}}
__M_END_METADATA
"""
