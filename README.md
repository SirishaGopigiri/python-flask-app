# Test App Flask python

Sample python project built using flask

To install python packages
```# python -m pip install -r requirements.txt```

To run the app locally use the below command
```# python3 -m flask run```

To run test cases
```# pytest test_app.py```

To build docker image
```# docker build -t testapp .```

To run the app as docker conatiner
```# sudo docker run -it --publish 8099:5000 testapp:latest```

Run curl command to test the app
```# curl -v localhost:8099/```
```# curl -v localhost:8099/return_version```
