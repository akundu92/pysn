import codecs
import json
class Util():
    @staticmethod
    def count_json_elemets(jsonobj):

        pass

    @staticmethod
    def write_json_to_file(json,filename,location=''):
        file = codecs.open(location+filename + ".json", "w", "utf-8")
        file.write(json)
        file.close()

