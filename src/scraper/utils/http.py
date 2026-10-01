from urllib.request import Request, urlopen

DEFAULT_USER_AGENT = "cc-scraper/0.1"

def get(url: str, timeout: int = 10) -> str:
	request = Request(url, headers={"User-Agent": DEFAULT_USER_AGENT})

	with urlopen(request, timeout=timeout) as response:
		charset = response.headers.get_content_charset() or "utf-8"
		return response.read().decode(charset, errors="replace")
