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
            {"enemyid-equipmentid-res":"${P(/Users/gsky/my_github/python_about/new_httprunner3/battle_cases/datas/kill_data.csv)}"},
            # {"enemyid-equipmentid-res": [
            #         ["20001", "10002","You win Level 1"],
            #        ["20001", "10001","Your and your enemy all dead!!!"],
            #        ["", "10002","Error 9904: Your kill yourself!!"],
            #        ["20004", "","Error 9905: Your fight your enemy by nothing!And you are  died!"],
            #     ]}
        ),
    )
    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("battle: kill")
		.base_url("http://101.34.170.225:12356")
        .verify(False)
    )

    teststeps = [

        Step(
            RunRequest("两个字段都有值的正反用例")
            .post("/kill")
            .with_data({"enemyid":"$enemyid","equipmentid":"$equipmentid"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_regex_match("body", "${res}")
            
        ),
        # Step(
        #     RunRequest("enemyid字段缺失用例")
        #     .post("/kill")
        #     .with_data({"equipmentid":"10002"})
        #     .validate()
        #     .assert_equal("status_code", 200)
        #     .assert_regex_match("body", "Error 9904: Your kill yourself!!")
        # ),
        # Step(
        #     RunRequest("equipmentid字段缺失用例")
        #     .post("/kill")
        #     .with_data({"enemyid":"20004"})
        #     .validate()
        #     .assert_equal("status_code", 200)
        #     .assert_regex_match("body", "Error 9905: Your fight your enemy by nothing!And you are  died!")
        # ),
    ]


if __name__ == "__main__":
    TestCaseBattle().test_start()