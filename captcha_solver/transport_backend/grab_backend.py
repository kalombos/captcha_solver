from grab import Grab


class GrabBackend(object):
    def request(self, url, post_data):
        g = Grab(connect_timeout=10)
        g.setup(url=url)
        if post_data:
            g.setup(post=post_data)
        g.request()
        return {'code': g.doc.code, 'body': g.doc.body, 'url': url}

    def make_grab_instance(self, url, post_data):
        g = Grab()
        g.setup(url=url)
        if post_data:
            g.setup(post=post_data)
        return g
