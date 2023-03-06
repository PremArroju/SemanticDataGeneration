import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD

# Create an RDF graph and set the base namespace
covid_graph = Graph()
covid_ns = Namespace("http://example.com/covid-ontology#")
covid_graph.bind("covid", covid_ns)

# Create classes
covid_graph.add((covid_ns["DailyStatistics"], RDF.type, RDFS.Class))
covid_graph.add((covid_ns["CumulativeStatistics"], RDF.type, RDFS.Class))



# Create data properties for DailyStatistics
covid_graph.add((covid_ns["date"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["date"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["date"], RDFS.range, XSD.date))
covid_graph.add((covid_ns["population"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["population"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["population"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["cases"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["cases"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["cases"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["tests"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["tests"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["tests"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["deaths"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["deaths"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["deaths"], RDFS.range, XSD.integer))

# Create data properties for CumulativeStatistics
covid_graph.add((covid_ns["date"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["date"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["date"], RDFS.range, XSD.date))
covid_graph.add((covid_ns["population"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["population"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["population"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["cumulativeCases"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["cumulativeCases"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["cumulativeCases"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["cumulativeTests"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["cumulativeTests"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["cumulativeTests"], RDFS.range, XSD.integer))
covid_graph.add((covid_ns["cumulativeDeaths"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["cumulativeDeaths"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["cumulativeDeaths"], RDFS.range, XSD.integer))

# Create object properties
covid_graph.add((covid_ns["locatedIn"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["locatedIn"], RDFS.domain, covid_ns["DailyStatistics"]))
covid_graph.add((covid_ns["locatedIn"], RDFS.range, covid_ns["Area"]))

covid_graph.add((covid_ns["locatedIn"], RDF.type, RDF.Property))
covid_graph.add((covid_ns["locatedIn"], RDFS.domain, covid_ns["CumulativeStatistics"]))
covid_graph.add((covid_ns["locatedIn"], RDFS.range, covid_ns["Area"]))

# Read CSV file and add instances
with open('State.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:


        # Create instances for DailyStatistics
        daily_uri = URIRef(f"{covid_ns}daily/{row['name']}/{row['date']}")
        covid_graph.add((daily_uri, RDF.type, covid_ns["DailyStatistics"]))
        covid_graph.add((daily_uri, covid_ns["date"], Literal(row['date'], datatype=XSD.date)))
        covid_graph.add((daily_uri, covid_ns["population"], Literal(row['population'], datatype=XSD.integer)))
        covid_graph.add((daily_uri, covid_ns["cases"], Literal(row['cases'], datatype=XSD.integer)))
        covid_graph.add((daily_uri, covid_ns["tests"], Literal(row['tests'], datatype=XSD.integer)))
        covid_graph.add((daily_uri, covid_ns["deaths"], Literal(row['deaths'], datatype=XSD.integer)))
        covid_graph.add((daily_uri, covid_ns["locatedIn"], Literal(row['name'])))

        # Create instances for CumulativeStatistics
        cumulative_uri = URIRef(f"{covid_ns}cumulative/{row['name']}/{row['date']}")
        covid_graph.add((cumulative_uri, RDF.type, covid_ns["CumulativeStatistics"]))
        covid_graph.add((cumulative_uri, covid_ns["date"], Literal(row['date'], datatype=XSD.date)))
        covid_graph.add((cumulative_uri, covid_ns["population"], Literal(row['population'], datatype=XSD.integer)))
        covid_graph.add((cumulative_uri, covid_ns["cumulativeCases"], Literal(row['cumulative_cases'], datatype=XSD.integer)))
        covid_graph.add((cumulative_uri, covid_ns["cumulativeTests"], Literal(row['cumulative_tests'], datatype=XSD.integer)))
        covid_graph.add((cumulative_uri, covid_ns["cumulativeDeaths"], Literal(row['cumulative_deaths'], datatype=XSD.integer)))
        covid_graph.add((cumulative_uri, covid_ns["locatedIn"], Literal(row['name'])))

# Serialize RDF graph to a file
covid_graph.serialize(destination='State.owl', format='xml')
