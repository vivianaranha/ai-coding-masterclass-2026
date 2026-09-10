"""Project 09 scaffold."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_coding.quality import gate
def main(): print({"project":"AI Debugging Case","gate":gate(True,True,True,True)})
if __name__=="__main__":main()
