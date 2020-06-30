import os
import sys

# https://rdflib.github.io/sparqlwrapper/
from SPARQLWrapper import SPARQLWrapper, JSON

from config import PROJECT_ROOT


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
        for result in results["results"]["bindings"]:
            print(result)


if __name__ == "__main__":
    get_data()
