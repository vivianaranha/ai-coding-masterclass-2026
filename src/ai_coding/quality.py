def gate(test_pass,lint_pass,security_pass,review_pass):
 c={"tests":test_pass,"lint":lint_pass,"security":security_pass,"review":review_pass};return {"pass":all(c.values()),"failed":[k for k,v in c.items() if not v]}
