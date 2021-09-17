FROM python:3


COPY . /home/ruleragent/.
WORKDIR /home/ruleragent
RUN python -m pip install -r requirements.txt

CMD [ "python", "main.py"]