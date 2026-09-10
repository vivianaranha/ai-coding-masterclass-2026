import sys,unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from ai_coding.specs import completeness
from ai_coding.diffs import diff_risk,tier
from ai_coding.secrets import findings
from ai_coding.quality import gate
from ai_coding.context import context_budget
from ai_coding.eval import workflow_score
class T(unittest.TestCase):
 def test_spec(self): self.assertEqual(completeness({"goal":1,"acceptance":1,"constraints":1,"tests":1}),1)
 def test_diff(self): self.assertEqual(tier(diff_risk(1,10)), "low")
 def test_secret(self): self.assertTrue(findings('password="secret"'))
 def test_gate(self): self.assertTrue(gate(True,True,True,True)["pass"]);self.assertIn("tests",gate(False,True,True,True)["failed"])
 def test_context(self): self.assertEqual(context_budget([{"path":"a","content":"123"},{"path":"b","content":"456"}],4)["files"],["a"])
 def test_eval(self): self.assertEqual(workflow_score(1,1,1,1),100)
if __name__=="__main__":unittest.main()
