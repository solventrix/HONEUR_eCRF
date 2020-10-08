FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
RUN git -C /code clone https://github.com/solventrix/HONEUR_ecrf.git
# COPY requirements.txt /code/
RUN pip install -r HONEUR_ecrf/requirements.txt
RUN cp -r HONEUR_ecrf/. /code/
RUN python manage.py migrate 
RUN python manage.py createopalsuperuser 
RUN python manage.py load_lookup_lists 
RUN ls /code
