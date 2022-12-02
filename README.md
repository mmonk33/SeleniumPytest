# SeleniumPytest
Yandex search test task  (Selenium (Selenoid) + Py.test + Allure) 

## Running tests

```bash
$ pip install -r requirements.txt
$ python -m pytest Tests/ selenoid=<y/N> browser=<chrome> --alluredir=test_results
$ allure serve test_results
```
## Running marked tests

```bash
$ pytest -v -m pictures/search
```

## Selenoid install
[Installation instructions in the official repository](https://github.com/aerokube/selenoid#one-command-installation)
```bash
$ ./cm selenoid start --vnc --tmpfs 128
```
## Allure report with steps and failed assertion logs
![image](https://user-images.githubusercontent.com/102417439/205257272-8c8496c2-eb80-41f8-8945-5b7cac56a8f7.png)
