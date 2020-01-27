# -*- coding: utf-8 -*-
_CLIENT_IP_HEADERS = ["X-Forwarded-For", "Proxy-Client-IP", "WL-Proxy-Client-IP", "Real-ClientIP"]


def get_client_ip(http_request):
    """
    获取用户IP,
    由于是经过了CDN，有可能被用户找到真实后端外网地址，篡改HTTP头进行请求，所有可能不真实
    :param http_request:
    :return:
    """
    _headers = http_request.headers
    for hk in _CLIENT_IP_HEADERS:
        if _headers.get(hk):
            return _headers.get(hk)
    return http_request.remote_addr
