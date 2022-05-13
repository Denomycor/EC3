from rdflib import RDFS, Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDF, XSD, FOAF
from logging import debug

import csv


def read_csv(csvf):
    with open(csvf, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            yield row


def createGraph():
    graph = Graph()
    ns = Namespace('')

    graph.add((ns._2021_2022, ns.cadeiras, ns.EC))
    graph.add((ns.EC, ns.lecionadoPor, ns.Paulo_Urbano))
    graph.add((ns.EC, ns.lecionadoPor, ns.Graça_Gaspar))
    graph.add((ns.EC, ns.avaliação, Literal('proj1;10;0', datatype=XSD.string)))
    graph.add((ns.EC, ns.avaliação, Literal('proj2;10;0', datatype=XSD.string)))
    graph.add((ns.EC, ns.avaliação, Literal('proj3;10;0', datatype=XSD.string)))
    graph.add((ns.EC, ns.avaliação, Literal('exame;70;9.5', datatype=XSD.string)))



    graph.add((ns._2019_2020, ns.cadeiras, ns.TC))
    graph.add((ns.TC, ns.lecionadoPor, ns.Paulo_Urbano))
    graph.add((ns.TC, ns.lecionadoPor, ns.André_Souto))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont1;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont2;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont3;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont4;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('exame;80;9', datatype=XSD.string)))

    graph.add((ns._2020_2021, ns.cadeiras, ns.IIA))
    graph.add((ns.IIA, ns.lecionadoPor, ns.Paulo_Urbano))
    graph.add((ns.IIA, ns.lecionadoPor, ns.Luis_Correia))
    graph.add((ns.IIA, ns.lecionadoPor, ns.Helena_Aidos))
    graph.add((ns.IIA, ns.avaliação, Literal('proj1;10;8.5', datatype=XSD.string)))
    graph.add((ns.IIA, ns.avaliação, Literal('proj2;10;8.5', datatype=XSD.string)))
    graph.add((ns.IIA, ns.avaliação, Literal('exame;80;9', datatype=XSD.string)))

    graph.add((ns._2020_2021, ns.cadeiras, ns.TC))
    graph.add((ns.TC, ns.lecionadoPor, ns.Ana_Respácio))
    graph.add((ns.TC, ns.lecionadoPor, ns.João_Neto))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont1;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('avalCont2;5;0', datatype=XSD.string)))
    graph.add((ns.TC, ns.avaliação, Literal('exame;90;9', datatype=XSD.string)))

    graph.add((ns._2019_2020, ns.cadeiras, ns.LabP))
    graph.add((ns.LabP, ns.lecionadoPor, ns.Graça_Gaspar))
    graph.add((ns.LabP, ns.lecionadoPor, ns.André_souto))
    graph.add((ns.LabP, ns.lecionadoPor, ns.Isabel_Nunes))
    graph.add((ns.LabP, ns.avaliação, Literal('projetos;70;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('exercicios;30;9', datatype=XSD.string)))

    graph.add((ns._2022_2023, ns.cadeiras, ns.LabP))
    graph.add((ns.LabP, ns.lecionadoPor, ns.João_Neto))
    graph.add((ns.LabP, ns.lecionadoPor, ns.Ana_Paula_Cláudio))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto1;10;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('exercicios;10;0', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto2;20;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto3;30;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto4;30;9', datatype=XSD.string)))

    graph.add((ns._2020_2021, ns.cadeiras, ns.EC))
    graph.add((ns.EC, ns.lecionadoPor, ns.Paulo_Urbano))
    graph.add((ns.EC, ns.lecionadoPor, ns.Graça_Gaspar))
    graph.add((ns.EC, ns.avaliação, Literal('proj1;15;9', datatype=XSD.string)))
    graph.add((ns.EC, ns.avaliação, Literal('exame;70;9', datatype=XSD.string)))
    graph.add((ns.EC, ns.avaliação, Literal('proj2;15;9', datatype=XSD.string)))

    graph.add((ns._2015_2016, ns.cadeiras, ns.LabP))
    graph.add((ns.LabP, ns.lecionadoPor, ns.Isabel_Nunes))
    graph.add((ns.LabP, ns.lecionadoPor, ns.Beatriz_Carmo))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto1;10;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('exercicios;10;0', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto2;20;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto3;30;9', datatype=XSD.string)))
    graph.add((ns.LabP, ns.avaliação, Literal('projeto4;30;9', datatype=XSD.string)))

    graph.add((ns._2021_2022, ns.cadeiras, ns.IP))
    graph.add((ns.IP, ns.lecionadoPor, ns.Antónia_Lopes))
    graph.add((ns.IP, ns.lecionadoPor, ns.Wellington))
    graph.add((ns.IP, ns.lecionadoPor, ns.Graça_Gaspar))
    graph.add((ns.IP, ns.avaliação, Literal('avalCont;10;0', datatype=XSD.string)))
    graph.add((ns.IP, ns.avaliação, Literal('proj;20;8.5', datatype=XSD.string)))
    graph.add((ns.IP, ns.avaliação, Literal('exame;70;9', datatype=XSD.string)))

    print(graph.serialize(format='turtle'))
    return (graph, ns)

createGraph()
    
