from common import WrapPlus
_REFERRER = "5fb12dd5-2cd6-474a-ae58-d6bd5ec2f51b"
boots_with_http = WrapPlus(referrer=_REFERRER,protocol='http',timeout=100)
boots_with_http.run()