# Автотесты и GitHub Actions

Автотесты из лабораторных работ №5 и №6:

- `tests/test_calculator.py` — модульные тесты класса `Calculator`;
- `tests/test_users_api.py` — тесты REST API JSONPlaceholder.

Запуск локально:

```
pip install -r requirements.txt
pytest -v
```

При каждом push в ветку `main` тесты запускает GitHub Actions (`.github/workflows/run-tests.yml`).
