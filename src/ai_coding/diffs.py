def diff_risk(files_changed,lines_changed,critical_files=0):
 return round(min(100,files_changed*3+lines_changed/20+critical_files*20),1)
def tier(score):
 return "high" if score>=60 else "medium" if score>=30 else "low"
