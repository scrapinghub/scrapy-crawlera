from scrapy import Request


class CrawleraSessionReuseMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __init__(self, crawler):
        setting = 'CRAWLERA_SESSION_REUSE_DEFAULT_SESSION'
        self._default_session = crawler.settings.get(setting)

    def process_spider_output(self, response, result, spider):
        def _set_session(request_or_item):
            if not isinstance(request_or_item, Request):
                return request_or_item

            request = request_or_item
            header = b'X-Crawlera-Session'
            meta_key = 'crawlera_session_reuse'

            if request.meta.get(meta_key) is not True:
                return request

            session = response.headers.get(header)
            error = response.headers.get(b'X-Crawlera-Error')
            session_is_bad = error == b'bad_session_id'

            if session is not None and not session_is_bad:
                request.headers[header] = session
            elif self._default_session:
                request.headers[header] = self._default_session
            return request

        return (_set_session(request_or_item)
                for request_or_item in result or ())
