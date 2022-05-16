from rdflib import RDFS, Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDF, XSD, FOAF
from logging import debug

import csv


def read_csv(csvf):
    with open(csvf, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            yield row



def createGraph2():
    graph = Graph()
    ns = Namespace('')

    

    # Professores
    graph.add((ns.PauloUrbano, RDF.type, ns.Professor))
    graph.add((ns.GracaGaspar, RDF.type, ns.Professor))
    graph.add((ns.AndreSouto, RDF.type, ns.Professor))
    graph.add((ns.LuisCorreia, RDF.type, ns.Professor))
    graph.add((ns.HelenaAidos, RDF.type, ns.Professor))
    graph.add((ns.AnaRespicio, RDF.type, ns.Professor))
    graph.add((ns.JoaoNeto, RDF.type, ns.Professor))
    graph.add((ns.IsalbelNunes, RDF.type, ns.Professor))
    graph.add((ns.AnaClaudio, RDF.type, ns.Professor))
    graph.add((ns.AntoniaLopes, RDF.type, ns.Professor))
    graph.add((ns.Wellington, RDF.type, ns.Professor))

    # Cadeiras
    graph.add((ns.EC, RDF.type, ns.Cadeira))
    graph.add((ns.TC, RDF.type, ns.Cadeira))
    graph.add((ns.IIA, RDF.type, ns.Cadeira))
    graph.add((ns.LABP, RDF.type, ns.Cadeira))
    graph.add((ns.IP, RDF.type, ns.Cadeira))


    # Execucoes
    graph.add((ns.execucao1, RDF.type, ns.Execucao))
    graph.add((ns.execucao1, ns.temAno, Literal("2021/2022")))
    # Nao sei se devia ser tipo materia para nao estar a reutilizar Cadeira
    graph.add((ns.execucao1, ns.temCadeira, ns.EC))
    graph.add((ns.execucao1, ns.temProfessor, ns.PauloUrbano))
    graph.add((ns.execucao1, ns.temProfessor, ns.GracaGaspar))
    

    # Avaliacoes
    graph.add((ns.avaliacao1, RDF.type, ns.Avaliacao))
    graph.add((ns.avaliacao1, ns.temNome, Literal("proj1", datatype=XSD.string)))
    graph.add((ns.avaliacao1, ns.temNotaMinima, Literal(10, datatype=XSD.int)))
    graph.add((ns.avaliacao1, ns.temPercentagem, Literal(0, datatype=XSD.float)))

    graph.add((ns.avaliacao2, RDF.type, ns.Avaliacao))
    graph.add((ns.avaliacao2, ns.temNome, Literal("proj2", datatype=XSD.string)))
    graph.add((ns.avaliacao2, ns.temNotaMinima, Literal(10, datatype=XSD.int)))
    graph.add((ns.avaliacao2, ns.temPercentagem, Literal(0, datatype=XSD.float)))

    graph.add((ns.avaliacao3, RDF.type, ns.Avaliacao))
    graph.add((ns.avaliacao3, ns.temNome, Literal("proj3", datatype=XSD.string)))
    graph.add((ns.avaliacao3, ns.temNotaMinima, Literal(10, datatype=XSD.int)))
    graph.add((ns.avaliacao3, ns.temPercentagem, Literal(0, datatype=XSD.float)))

    graph.add((ns.avaliacao4, RDF.type, ns.Avaliacao))
    graph.add((ns.avaliacao4, ns.temNome, Literal("exame", datatype=XSD.string)))
    graph.add((ns.avaliacao4, ns.temNotaMinima, Literal(70, datatype=XSD.int)))
    graph.add((ns.avaliacao4, ns.temPercentagem, Literal(9.5, datatype=XSD.float)))

    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao1))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao2))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao3))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao4))

    return (graph, ns)

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

    return (graph, ns)

(g,n) = createGraph()
    
(g2,n2) = createGraph2()

print(g2.serialize(format='turtle'))
