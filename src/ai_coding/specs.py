def completeness(spec):
 fields=["goal","acceptance","constraints","tests"];return sum(bool(spec.get(x)) for x in fields)/len(fields)
