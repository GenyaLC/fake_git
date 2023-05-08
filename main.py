import uuid
import sys
import datetime
import random
from git import Repo
import pathlib
import os

    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python main.py <initial_date> <final_date>" +
              "\n\tinitial_date: YYYY-MM-DD")
        exit(1)

    initial_date = sys.argv[1]
    final_date = sys.argv[2]

    date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
    date = date.replace(tzinfo=datetime.timezone.utc)
    final = datetime.datetime.strptime(final_date, '%Y-%m-%d')
    final = final.replace(tzinfo=datetime.timezone.utc)

    path = pathlib.Path(__file__).parent.resolve()
    
    repo = Repo.init(path).git
    index = Repo.init(path).index
    
    fake_files = []
    
    while date != final:
        date = date + datetime.timedelta(days=1)
        for x in range(random.randint(0, 4)):
            name = str(uuid.uuid4())
            fake_files.append(name)
            with open(name, "w") as f:
                f.write("Nothing to see here")
                f.close()
                repo.add(name)
        
            index.commit("Fake commiting for date: " + date.isoformat(), commit_date = date, author_date = date)
        
        for file in fake_files:
            os.remove(file)
        fake_files.clear()