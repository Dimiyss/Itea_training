class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError



class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()


class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass




class Http:
    def __init__(self, http_service: Connection):
        self.http_service = http_service

    def get(self, url: str, options: dict):
        self.http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_service.request(url, 'POST')


xml_http = HTTP(XMLHttpService())
xml_http.get()
xml_http.post()

node_http = HTTP(NodeHttpService())
node_http.get()
node_http.post()