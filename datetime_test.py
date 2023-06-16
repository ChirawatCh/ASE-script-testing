from datetime import datetime
import os

def remove_outdated_file(source_name, path):

  date_format = '%Y%m%d'
  current_date = datetime.now().strftime(date_format)
  current_date_file = str(str(current_date) + '.csv')
  print(current_date_file)

  for file in os.listdir(path):
    if file.endswith('.csv'):
      if source_name in file and not file.endswith(current_date_file):
        os.remove(os.path.join(path, file))

if __name__ == '__main__':
    remove_outdated_file('storeline', '/Users/chirawatchitpakdee/vasp_database/ase_test')