# start by pulling the python image
#sudo docker run -p 5000:5000 -d test:3


#FROM python:3.8-alpine
FROM python:3.8-slim
WORKDIR /app
COPY . /app
# copy the requirements file into the image
#COPY ./requirements.txt /app/requirements.txt
#COPY ./employees.py /app/employees.py
#RUN mkdir /app
#RUN cd /app
#sudo docker run -p 5000:5000 -d test:3 


#RUN apt-get -y update
#RUN apt-get -y install git
#RUN git clone https://github.com/DimaBaringoltz/final-project.git
#RUN cd final-project/employees
#WORKDIR /app/final-project/employees
# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt


# switch working directory


#EXPOSE 5000


# configure the container to run in an executed manner
#ENTRYPOINT [ "python" ]
ENV FLASK_APP=employees.py
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
