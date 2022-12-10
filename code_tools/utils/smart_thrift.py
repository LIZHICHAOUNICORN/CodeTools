import os
import thriftpy2

pwd = os.path.dirname(os.path.dirname(__file__))
iris_thrift = thriftpy2.load(os.path.join(pwd, 'thrift_service',
                                          'iris_service.thrift'),
                             module_name='iris_thrift')
base_thrift = thriftpy2.load(os.path.join(pwd, 'thrift_service',
                                          'base.thrift'),
                             module_name='base_thrift')