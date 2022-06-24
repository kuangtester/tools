import pytest
import allure

from string import Template

from utils.yamlutil import ReadYaml
import requests
from utils import logutil

logger = logutil.LogUtil().log()


@pytest.mark.parametrize('datas', ReadYaml("login"))
def test_delcart_succ():
    pass


if __name__ == '__main__':
    pytest.main(['-vs'])
