FROM python:3.10
WORKDIR /SeleniumPytestTestTask/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=/allure_results/ /SeleniumPytestTestTask/Tests/