from pysn import params_builder as pb
pba=pb.ParamsBuilderAggregate()
pba.add_custom({'hello':None})
print(pba.as_dict())

