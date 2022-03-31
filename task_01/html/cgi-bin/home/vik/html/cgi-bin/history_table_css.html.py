# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1644260218.0311065
_enable_loop = True
_template_filename = '/home/vik/html/cgi-bin/history_table_css.html'
_template_uri = '/home/vik/html/cgi-bin/history_table_css.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h_list = context.get('h_list', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <head>\n        <title>Page Title</title>\n        <meta charset="UTF-8">\n        <style>\n            table {\n            font-family: arial, sans-serif;\n            border-collapse: collapse;\n            width: 100%;\n            }\n            \n            td, th {\n            border: 1px solid #dddddd;\n            text-align: left;\n            padding: 8px;\n            }\n            \n            tr:nth-child(even) {\n            background-color: #dddddd;\n            }\n        </style>\n    </head>\n    \n    <body>\n<table cellspacing = "2" cellpadding = "5" border="1px">\n  <tr>\n    <th>Время визита</th>\n    <th>Ссылка на сайт</th>\n  </tr>\n')
        for title, url, dt in h_list:
            __M_writer('\n')
            if len(title) < 1:
                __M_writer('        <tr>    <td>')
                __M_writer(str(dt))
                __M_writer('</td>   <td><a href = "')
                __M_writer(str(url))
                __M_writer('" > ')
                __M_writer(str(url))
                __M_writer(' </a></td>  </tr>\n')
            else:
                __M_writer('        <tr>    <td>')
                __M_writer(str(dt))
                __M_writer('</td>   <td><a href = "')
                __M_writer(str(url))
                __M_writer('" > ')
                __M_writer(str(title))
                __M_writer(' </a></td>  </tr>\n')
            __M_writer('\n')
        __M_writer('\n\n</table> \n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/vik/html/cgi-bin/history_table_css.html", "uri": "/home/vik/html/cgi-bin/history_table_css.html", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 31, "25": 32, "26": 33, "27": 34, "28": 34, "29": 34, "30": 34, "31": 34, "32": 34, "33": 34, "34": 35, "35": 36, "36": 36, "37": 36, "38": 36, "39": 36, "40": 36, "41": 36, "42": 38, "43": 40, "49": 43}}
__M_END_METADATA
"""
