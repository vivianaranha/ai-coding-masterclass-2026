def context_budget(files,max_chars=12000):
 chosen=[];used=0
 for f in files:
  size=len(f.get("content",""))
  if used+size<=max_chars: chosen.append(f["path"]);used+=size
 return {"files":chosen,"chars":used}
