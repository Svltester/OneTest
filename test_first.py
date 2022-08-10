"""Смоук проверка API REST методов для метрик ИА/АМ с помощью GET запросов, проверка ответного кода 200 """

import json
import requests
import pytest
domen_test = "https://ia.rt-eu.ru"

domen = domen_test
api_metods = ["/realms/master/metrics/clients_count",
              "/realms/master/metrics/users_count",
              "/realms/master/metrics/auth_total",
              "/realms/master/metrics/auth_errors",
              "/realms/master/metrics/registration"]


@pytest.mark.parametrize("api_metod", api_metods)
def test_get_new_api(api_metod):
    url = domen + str(api_metod)

    payload = {}
    headers = {}

    response = requests.request(method="GET", url=url, headers=headers, data=payload, verify='russian_trust_root_ca.crt')
    response.encoding = "utf-8"
    assert response.status_code == 200, "Неправильный ответный код"

    assert str(type(response.json())) in ["<class 'dict'>", "<class 'list'>"], "Ошибка - в ответе не json"
    r = json.loads(response.text.encode("utf-8"))

    dump = json.dumps(r, indent=2, ensure_ascii=False)
    print("\n Тестируемый URL ", url, "\n", "Ответный код ", response.status_code, "\n Ответ \n", dump)
