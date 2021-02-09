# guajira_py_light_sensor

Python project that communicates with a light sensor via GPIO on a RaspberryPi

## **Dependencies installation**

1. Install python3 interpreter [`python3`](https://www.python.org/)
2. It is recommended to create a virtual environment [`venv`](https://docs.python.org/3/library/venv.html)
3. Install dependencies:
   \$ pip install -r requirements.txt

## **Usage**

```
    $ python start_light_sensor_service.py 4
```

The command above will run a loop and when the light sensor feels that the light has change it will communicate with the backend

