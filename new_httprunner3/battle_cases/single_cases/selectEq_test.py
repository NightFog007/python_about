
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters

class TestCaseDemoTestcaseRef(HttpRunner):
    
    @pytest.mark.parametrize(
        "param", Parameters({"equipmentid": ["10001","10002","10003"]})
    )
    def test_start(self, param):
        super().test_start(param)


    config = (
        Config("battle: selectEq")
        .base_url("http://101.34.170.225:12356")
        .verify(False)
        .export(*["response_some_value"]) #提取响应字段
    )

    teststeps = [
        Step(
            RunRequest("post form data")
            # .with_variables(**{"foo1": "bar1"})  #单例级别变量
            .post("/selectEq")
            .with_headers(
                **{
                    "Content-Type": "application/x-www-form-urlencoded",
                }
            )
            .with_data("equipmentid=${equipmentid}")
            .extract()
            .with_jmespath("body.Message","response_some_value") #提取响应字段
            .validate()
            .assert_equal("status_code", 200)
            .assert_contains("body.Message", "your pick up equipmentid:${equipmentid}")

        ),
    ]

if __name__ == "__main__":
    TestCaseDemoTestcaseRef().test_start()
