from .params_builder import ParamsBuilder,ParamsBuilderAggregate
import json


class Resource():
    def __init__(self,api):
        self.api=api

    def get(self):
        raise NotImplementedError


# Table may have dependancy on Aggregate to get resources.
class Table(Resource):
    def __init__(self,api,tablename=None):
        super().__init__(api)
        self.tablename=tablename

    def get(self,query,fields,limit,offset=None,raw=False):
        url = self.api.host + ('/api/now/table/')+self.tablename
        pb=ParamsBuilder()
        pb.query=query
        pb.limit=limit
        if offset:
            pb.offset=offset
        pb.fields=[str(x) for x in str(fields).split(',')]


        r=self.api.session.get(url,params= pb.as_dict())
        if raw == True:
            return  r
        else:
            return json.loads(r.text())





class Aggregate(Resource):
    def __init__(self,api,tablename=None):
        super().__init__(api)
        self.tablename = tablename

    def get(self,query, avg_fields=None, count=False,
            min_fields=None, max_fields=None, sum_fields=None,
            group_by=None, order_by=None, having=None, display_value=False,
            query_category=None,**kwargs):
        url=url = self.api.host + ('/api/now/stats/')+self.tablename
        pba=ParamsBuilderAggregate()
        pba.query=query
        pba.count=count
        print(pba.as_dict())
        r = self.api.session.get(url, params=pba.as_dict())
        return json.loads(r.text)['result']['stats']





