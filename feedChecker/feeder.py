import datetime

class Feeder:
    def __init__(self):
        self.entries = []
    
    def set(self, parsed_xml):
        for entry in parsed_xml['entries']:
            tmp = {}

            # Convert "Tue, 06 Mar 2018 05:20:30 +0000" => Type(Date)
            entry_date_raw = entry['published']
            entry_date = datetime.datetime.strptime(entry_date_raw, '%a, %d %b %Y %H:%M:%S %z')
            tmp['date'] = str(entry_date.strftime('%Y/%m/%d'))

            # Convert from internal-uri to external-uri
            entry_uri = entry['links'][0]['href']
            tmp['uri'] = entry_uri.replace("//inside.teu.ac.jp/", "//service.cloud.teu.ac.jp/inside2/")

            tmp['title'] = entry['title'] 
            tmp['author'] = entry['author']
            tmp['content'] = entry['content'][0]['value']
            self.entries.append(tmp)

    def get(self):
        return self.entries

    def print(self, items=[]):
        for i in self.entries:
            for key in items:
                print(i[key])
            print("-----")

