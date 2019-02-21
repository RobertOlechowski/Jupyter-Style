import sys

if sys.version_info < (3, 5):
    raise Exception("Python 3.5 required")


class StyleHelper(object):
    template_file_name = "style_template.css_template"

    def __init__(self):
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(dir_path, self.template_file_name)
        self.styles_template = open(file_name, "r").read()

    def _generate_style_text(self, **kwargs):
        from string import Template
        template = Template(self.styles_template)
        default_values = {
            "selector": "",
            "col_header_color": "antiquewhite",
            "row_header_color": "cornsilk"
        }

        values = {**default_values, **kwargs}
        return template.substitute(values)

    def emit_style(self, **kwargs):
        from IPython.display import HTML, display
        style_text = "<style > {} </style>".format(self._generate_style_text(**kwargs))
        display(HTML(style_text))

