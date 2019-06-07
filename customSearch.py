from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyCMYA4L1LHBTYOcBPK-bo2ri-KAbHg5O08"
my_cse_id = "008339965132227158677:cl1qnxecpfs"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'colors halsey', my_api_key, my_cse_id, num=1)
for result in results:
    pprint.pprint(str(result["formattedUrl"]))