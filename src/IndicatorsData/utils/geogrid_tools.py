import requests
from decouple import config



class GeogridTool():
    def get_geogrid(self):
        resp = requests.get(url=config(
            'URL')+config('Tablename')+'/GEOGRID/features')
        geogrid = resp.json()
        return geogrid

   
    def get_geogriddata():
        resp = requests.get(url=config(
            'URL')+config('Tablename')+'/GEOGRIDDATA')
        geogriddata = resp.json()
        return geogriddata
    
    def get_cityscopy_patterns():
        patterns=[]
        geogridata=GeogridTool.get_geogriddata()
        for i in range (len(geogridata)):

            if  geogridata[i]["cityscopy_id"]=="0000000000000000":
                dict={i:"0000000000000000"}
                patterns.append(dict)
            else:
                dict={i:geogridata[i]["cityscopy_pattern"]}
                patterns.append(dict)

        return patterns