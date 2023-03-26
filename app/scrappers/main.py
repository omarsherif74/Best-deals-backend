import sys
root_dir = '/home/mazen/ssp/term 9/BestDeals/backend/app/scrappers'
sys.path.append(root_dir)

from Heuristic import Heuristic
from helpers import get_file_path
from os import listdir
from os.path import isfile, join

WEBSITES_PATH = get_file_path('websites')
scrappingFiles = ['websites.' + f.split('.')[0] for f in listdir(WEBSITES_PATH) if isfile(join(WEBSITES_PATH, f))]

SEARCH_KEYS = ' '.join(sys.argv[1:])

products = []

for scrappingFile in scrappingFiles:
  products += __import__(scrappingFile, fromlist=['scrap']).scrap(SEARCH_KEYS)

heuristic = Heuristic(products)
heuristic.normalize()

productsData = []
for product in products: productsData.append(product.toJson())

print(productsData)
