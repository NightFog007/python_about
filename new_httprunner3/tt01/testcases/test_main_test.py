
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from .login_battle_test import TestCaseDemoTestcaseRef,TestCaseDemoTestcaseRef22


if __name__ == "__main__":
    TestCaseDemoTestcaseRef().test_start()
    TestCaseDemoTestcaseRef22().test_start()
