import os
import sys
import json
from datetime import date

# https://rdflib.github.io/sparqlwrapper/
from SPARQLWrapper import SPARQLWrapper, JSON

from config import PROJECT_ROOT, DATA_ROOT


endpoint_url = "https://query.wikidata.org/sparql"


def get_results(endpoint_url, query):
    user_agent = "Film Title Analysis, Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def get_data():
    with open(os.path.join(PROJECT_ROOT, 'src', 'query.sparql')) as f:
        query = f.read()
        results = get_results(endpoint_url, query)
        items = results["results"]["bindings"]
        with open(os.path.join(DATA_ROOT, 'films-%s.json' % date.today()), 'w') as data_file:
            json.dump(items, data_file)


if __name__ == "__main__":
    get_data()
