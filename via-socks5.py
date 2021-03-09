from common import WrapPlus
boots_with_http = WrapPlus(protocol='socks5',timeout=500)
boots_with_http.run()