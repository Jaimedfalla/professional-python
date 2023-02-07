from screeninfo import get_monitors

monitor = get_monitors()[0]
print(monitor.width)
print(monitor.height)