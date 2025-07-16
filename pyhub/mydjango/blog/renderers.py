# blog/renderers.py

from io import BytesIO

from rest_framework.renderers import BaseRenderer

import pandas as pd


class PandasXlsxRenderer(BaseRenderer):
    media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # 응답 시의 content type
    format = "xlsx"
    render_style = "binary"   # "text" or "binary"

    def render(self, data, accepted_media_type=None, renderer_context=None) -> BytesIO:
        io = BytesIO()
        df = pd.DataFrame(data)
        df.to_excel(io)  # noqa
        io.seek(0)
        return io
