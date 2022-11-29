from datetime import datetime #Función para trabajar con fechas

def execution_time(func):
    def wrapper(*args, **kwargs): #Con *args, **kwargs indicamos que los parámetros pueden ser enviados o no y que pueden ser ilimitados
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")

    return wrapper

@execution_time #Se decora la función random_func con la función execution_time
def random_func():
    for _ in range(1,1000000):
        pass

@execution_time
def sum(a:int,b:int) -> int :
    return a + b

if __name__ == '__main__':
    random_func()
    sum(5,5)