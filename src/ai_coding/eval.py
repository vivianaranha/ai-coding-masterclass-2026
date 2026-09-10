def workflow_score(correct,tested,secure,maintainable):
 return round((correct*.4+tested*.25+secure*.2+maintainable*.15)*100,1)
