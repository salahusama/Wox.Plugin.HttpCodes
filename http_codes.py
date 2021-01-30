import webbrowser
from wox import Wox, WoxAPI
from status_code_data import StatusCodes

class HttpCodes(Wox):
    def query(self, key):
        results = []
        code_matches = StatusCodes.getAll(key)
        for code in code_matches:
            results.append({
                "Title": code["code"] + " - " + code["title"],
                "SubTitle": code["description"],
                "JsonRPCAction": {
                    "method": "openUrl",
                    "parameters": [code["url"]],
                    "dontHideAfterAction": True,
                },
                "IcoPath":"http.ico",
            })
        return results

    def openUrl(self, url):
        if url is not None:
            webbrowser.open(url)

if __name__ == "__main__":
    HttpCodes()
