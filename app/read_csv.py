import csv

def write_txt(path,text):
  '''Con r+ se tienen permisos de lectura y escritura y se respeta el contenido del archivo
     Con w+ se sobrescribe el contenido del archivo
  '''
  with open(path,'r+') as file:
    file.write(text)

def read_txt(path):
  with open(path) as file:#with automáticamente cierra el archivo
    for line in file:
      print(line)

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)