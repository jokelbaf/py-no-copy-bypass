import re
from mitmproxy import http

class RemoveBlockCopy:
    _RE_POINTER       = re.compile(r'pointer-events\s*:\s*none\s*;?', re.IGNORECASE)
    _RE_USERSELECT    = re.compile(r'(?:-webkit-|-moz-|-ms-)?user-select\s*:\s*none\s*;?', re.IGNORECASE)
    _RE_INLINE_EV     = re.compile(r'on(?:copy|cut|paste|contextmenu|selectstart)\s*=\s*"(?:\\.|[^"])*"', re.IGNORECASE)
    _RE_EVENT_LISTENERS = re.compile(
        r'document\.addEventListener\(\s*["\'](?:copy|cut|paste|contextmenu|selectstart|keydown)["\']\s*,'
        r'[\s\S]*?\}\s*\)\s*;?',
        re.IGNORECASE
    )
    _RE_CONTENTEDITABLE = re.compile(r'\scontenteditable\s*=\s*"(?:false|0)"', re.IGNORECASE)
    _RE_SELECTION       = re.compile(r'::selection\s*\{[\s\S]*?\}', re.IGNORECASE)

    def response(self, flow: http.HTTPFlow):
        ct = flow.response.headers.get("Content-Type", "")
        text = flow.response.get_text()

        # HTML
        if "text/html" in ct:
            text = self._RE_POINTER.sub("", text)
            text = self._RE_USERSELECT.sub("", text)
            text = self._RE_INLINE_EV.sub("", text)
            text = self._RE_EVENT_LISTENERS.sub("", text)
            text = self._RE_CONTENTEDITABLE.sub("", text)
            flow.response.set_text(text)

        # CSS
        elif "text/css" in ct:
            text = self._RE_POINTER.sub("", text)
            text = self._RE_USERSELECT.sub("", text)
            text = self._RE_SELECTION.sub("", text)
            flow.response.set_text(text)

        # JavaScript
        elif "javascript" in ct:
            text = self._RE_EVENT_LISTENERS.sub("", text)
            flow.response.set_text(text)

addons = [RemoveBlockCopy()]
