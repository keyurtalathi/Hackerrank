from rq import Connection, Worker

with Connection():
        qs = ['op_email', 'new_lmd', 'incentive_structure']
        # TODO check why the exception handling is not working
        w = Worker(qs)
        w.work()
