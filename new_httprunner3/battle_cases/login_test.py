import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters


class TestCaseBattle(HttpRunner):
    
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"username-password-res":"${P(../datas/account.csv)}"}
        ),
    )
    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("battle: login")
		.base_url("http://101.34.170.225:12356")
        .verify(False)
    )

    teststeps = [

        Step(
            RunRequest("post form data")
            .post("/login")
            .with_data({"username":"$username","password":"$password"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_regex_match("body", "${res}")

        ),
    ]


if __name__ == "__main__":
    TestCaseBattle().test_start()

