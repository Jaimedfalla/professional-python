import csv

def write_txt(path,text,permission='r+'):
  '''Con r+ se tienen permisos de lectura y escritura y se respeta el contenido del archivo
     Con w+ se sobrescribe el contenido del archivo
  '''
  with open(path,permission) as file:
    file.write(text)

def read_txt(path)->str:
  text = ''
  with open(path) as file:#with automáticamente cierra el archivo
    for line in file:
      print(line)
      text += line
    
    return text

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