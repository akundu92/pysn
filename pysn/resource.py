from .params_builder import ParamsBuilder

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

    def get(self,query,fields,limit,offset=None,raw=True):
        url = self.api.host + ('/api/now/table/sys_audit')
        pb=ParamsBuilder()
        pb.query=query
        pb.limit=limit
        if offset:
            pb.offset=offset
        pb.fields=[str(x) for x in str(fields).split(',')]


        r=self.api.session.get(url,params= pb.as_dict())
        return  r




class Aggregate(Resource):
    def __init__(self,api,tablename=None):
        Table.__init__(api,tablename)


