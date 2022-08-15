import csv
import os
from coins.models import Coin


def run():
  list_path_data = os.listdir("./scripts/data")
  for file_data in list_path_data:
    print(file_data)
    file = open(os.path.join(os.getcwd()+"/scripts/data", file_data))
    read_file = csv.reader(file)
    
    count=1
    for record in read_file:
      if count == 1:
        pass
      else:
        
        Coin.objects.create(SNo=record[0], Name=record[1], Symbol=record[2],
                            Date=record[3], High=record[4], Low=record[5],
                            Open=record[6], Close=record[7], Volume=record[8],
                            Marketcap=record[9])
        
      count = count + 1
