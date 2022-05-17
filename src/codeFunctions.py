from rdflib import RDFS, Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import RDF, XSD, FOAF
from logging import debug


def createAval(graph, ns, id, nome, nMinima, perc):
    graph.add((ns[id], RDF.type, ns.Avaliacao))
    graph.add((ns[id], ns.temNome, Literal(nome, datatype=XSD.string)))
    graph.add((ns[id], ns.temNotaMinima, Literal(nMinima, datatype=XSD.int)))
    graph.add((ns[id], ns.temPercentagem, Literal(perc, datatype=XSD.float)))

def createGraph():
    graph = Graph()
    ns = Namespace('')

    graph.bind("", ns)

    # Professores
    graph.add((ns.PauloUrbano, RDF.type, ns.Professor))
    graph.add((ns.PauloUrbano, FOAF.name, Literal("Paulo Urbano", datatype=XSD.string)))

    graph.add((ns.GracaGaspar, RDF.type, ns.Professor))
    graph.add((ns.GracaGaspar, FOAF.name, Literal("Graca Gaspar", datatype=XSD.string)))
    
    graph.add((ns.AndreSouto, RDF.type, ns.Professor))
    graph.add((ns.AndreSouto, FOAF.name, Literal("Andre Souto", datatype=XSD.string)))

    graph.add((ns.LuisCorreia, RDF.type, ns.Professor))
    graph.add((ns.LuisCorreia, FOAF.name, Literal("Luis Correia", datatype=XSD.string)))

    graph.add((ns.HelenaAidos, RDF.type, ns.Professor))
    graph.add((ns.HelenaAidos, FOAF.name, Literal("Helena Aidos", datatype=XSD.string)))

    graph.add((ns.AnaRespicio, RDF.type, ns.Professor))
    graph.add((ns.AnaRespicio, FOAF.name, Literal("Ana Respicio", datatype=XSD.string)))

    graph.add((ns.JoaoNeto, RDF.type, ns.Professor))
    graph.add((ns.JoaoNeto, FOAF.name, Literal("Joao Neto", datatype=XSD.string)))

    graph.add((ns.IsalbelNunes, RDF.type, ns.Professor))
    graph.add((ns.IsalbelNunes, FOAF.name, Literal("Isalbel Nunes", datatype=XSD.string)))

    graph.add((ns.AnaClaudio, RDF.type, ns.Professor))
    graph.add((ns.AnaClaudio, FOAF.name, Literal("Ana Claudio", datatype=XSD.string)))

    graph.add((ns.AntoniaLopes, RDF.type, ns.Professor))
    graph.add((ns.AntoniaLopes, FOAF.name, Literal("Antonia Lopes", datatype=XSD.string)))

    graph.add((ns.Wellington, RDF.type, ns.Professor))
    graph.add((ns.Wellington, FOAF.name, Literal("Wellington", datatype=XSD.string)))

    graph.add((ns.BeatrizCarmo, RDF.type, ns.Professor))
    graph.add((ns.BeatrizCarmo, FOAF.name, Literal("Beatriz Carmo", datatype=XSD.string)))


    # Cadeiras
    graph.add((ns.EC, RDF.type, ns.Cadeira))
    graph.add((ns.EC, FOAF.name, Literal("EC", datatype=XSD.string)))
    graph.add((ns.TC, RDF.type, ns.Cadeira))
    graph.add((ns.TC, FOAF.name, Literal("TC", datatype=XSD.string)))
    graph.add((ns.IIA, RDF.type, ns.Cadeira))
    graph.add((ns.IIA, FOAF.name, Literal("IIA", datatype=XSD.string)))
    graph.add((ns.LABP, RDF.type, ns.Cadeira))
    graph.add((ns.LABP, FOAF.name, Literal("LabP", datatype=XSD.string)))
    graph.add((ns.IP, RDF.type, ns.Cadeira))
    graph.add((ns.IP, FOAF.name, Literal("IP", datatype=XSD.string)))

    #Anos Letivos
    graph.add((ns.Ano2122, RDF.type, ns.AnoLectivo))
    graph.add((ns.Ano1920, RDF.type, ns.AnoLectivo))
    graph.add((ns.Ano2021, RDF.type, ns.AnoLectivo))
    graph.add((ns.Ano2223, RDF.type, ns.AnoLectivo))
    graph.add((ns.Ano1516, RDF.type, ns.AnoLectivo))
    
    
    # -------------------------- Avaliacoes ----------------------------

    # 1
    createAval(graph, ns, "avaliacao1", "proj1", 10, 0)
    createAval(graph, ns, "avaliacao2", "proj2", 10, 0)
    createAval(graph, ns, "avaliacao3", "proj3", 10, 0)
    createAval(graph, ns, "avaliacao4", "exame", 70, 9.5)

    # 2
    createAval(graph, ns, "avaliacao5", "avalCont1", 5, 0)
    createAval(graph, ns, "avaliacao6", "avalCont2", 5, 0)
    createAval(graph, ns, "avaliacao7", "avalCont3", 5, 0)
    createAval(graph, ns, "avaliacao8", "avalCont4", 5, 0)
    createAval(graph, ns, "avaliacao9", "exame", 80, 9)

    # 3
    createAval(graph, ns, "avaliacao10", "proj1", 10, 8.5)
    createAval(graph, ns, "avaliacao11", "proj2", 10, 8.5)
    createAval(graph, ns, "avaliacao12", "exame", 80, 9)
    
    # 4
    createAval(graph, ns, "avaliacao13", "exame", 90, 9)
    createAval(graph, ns, "avaliacao14", "avalCont1", 5, 10)
    createAval(graph, ns, "avaliacao15", "avalCont2", 5, 10)

    # 5
    createAval(graph, ns, "avaliacao16", "projetos", 70, 9)
    createAval(graph, ns, "avaliacao17", "exercicios", 30, 9)

    # 6
    createAval(graph, ns, "avaliacao18", "projeto1", 10, 9)
    createAval(graph, ns, "avaliacao19", "exercicios", 10, 0)
    createAval(graph, ns, "avaliacao20", "projeto2", 20, 9)
    createAval(graph, ns, "avaliacao21", "projeto3", 30, 9)
    createAval(graph, ns, "avaliacao22", "projeto4", 30, 9)

    # 7
    createAval(graph, ns, "avaliacao23", "proj1", 15, 9)
    createAval(graph, ns, "avaliacao24", "exame", 70, 9)
    createAval(graph, ns, "avaliacao25", "proj2", 15, 9)

    # 8
    createAval(graph, ns, "avaliacao26", "projeto1", 10, 9)
    createAval(graph, ns, "avaliacao27", "exercicios", 10, 0)
    createAval(graph, ns, "avaliacao28", "projeto2", 20, 9)
    createAval(graph, ns, "avaliacao29", "projeto3", 30, 9)
    createAval(graph, ns, "avaliacao30", "projeto4", 30, 9)

    # 9
    createAval(graph, ns, "avaliacao31", "avalCont", 10, 0)
    createAval(graph, ns, "avaliacao32", "proj", 20, 8.5)
    createAval(graph, ns, "avaliacao33", "exame", 70, 9)
    
    # -------------------------- Execucoes ----------------------------

    # 1
    graph.add((ns.execucao1, RDF.type, ns.Execucao))
    graph.add((ns.execucao1, ns.temCadeira, ns.EC))
    graph.add((ns.execucao1, ns.temAno, ns.Ano2122))
    graph.add((ns.execucao1, ns.temProfessor, ns.PauloUrbano))
    graph.add((ns.execucao1, ns.temProfessor, ns.GracaGaspar))

    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao1))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao2))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao3))
    graph.add((ns.execucao1, ns.temAvaliacao, ns.avaliacao4))

    # 2
    graph.add((ns.execucao2, RDF.type, ns.Execucao))
    graph.add((ns.execucao2, ns.temCadeira, ns.TC))
    graph.add((ns.execucao2, ns.temAno, ns.Ano1920))
    graph.add((ns.execucao2, ns.temProfessor, ns.AndreSouto))
    graph.add((ns.execucao2, ns.temProfessor, ns.PauloUrbano))

    graph.add((ns.execucao2, ns.temAvaliacao, ns.avaliacao5))
    graph.add((ns.execucao2, ns.temAvaliacao, ns.avaliacao6))
    graph.add((ns.execucao2, ns.temAvaliacao, ns.avaliacao7))
    graph.add((ns.execucao2, ns.temAvaliacao, ns.avaliacao8))
    graph.add((ns.execucao2, ns.temAvaliacao, ns.avaliacao9))

    # 3
    graph.add((ns.execucao3, RDF.type, ns.Execucao))
    graph.add((ns.execucao3, ns.temCadeira, ns.IIA))
    graph.add((ns.execucao3, ns.temAno, ns.Ano2021))
    graph.add((ns.execucao3, ns.temProfessor, ns.LuisCorreia))
    graph.add((ns.execucao3, ns.temProfessor, ns.PauloUrbano))
    graph.add((ns.execucao3, ns.temProfessor, ns.HelenaAidos))

    graph.add((ns.execucao3, ns.temAvaliacao, ns.avaliacao10))
    graph.add((ns.execucao3, ns.temAvaliacao, ns.avaliacao11))
    graph.add((ns.execucao3, ns.temAvaliacao, ns.avaliacao12))

    # 4
    graph.add((ns.execucao4, RDF.type, ns.Execucao))
    graph.add((ns.execucao4, ns.temCadeira, ns.TC))
    graph.add((ns.execucao4, ns.temAno, ns.Ano2021))
    graph.add((ns.execucao4, ns.temProfessor, ns.AnaRespicio))
    graph.add((ns.execucao4, ns.temProfessor, ns.JoaoNeto))

    graph.add((ns.execucao4, ns.temAvaliacao, ns.avaliacao13))
    graph.add((ns.execucao4, ns.temAvaliacao, ns.avaliacao14))
    graph.add((ns.execucao4, ns.temAvaliacao, ns.avaliacao15))

    # 5
    graph.add((ns.execucao5, RDF.type, ns.Execucao))
    graph.add((ns.execucao5, ns.temCadeira, ns.LABP))
    graph.add((ns.execucao5, ns.temAno, ns.Ano1920))
    graph.add((ns.execucao5, ns.temProfessor, ns.IsabelNunes))
    graph.add((ns.execucao5, ns.temProfessor, ns.AndreSouto))
    graph.add((ns.execucao5, ns.temProfessor, ns.GracaGaspar))

    graph.add((ns.execucao5, ns.temAvaliacao, ns.avaliacao16))
    graph.add((ns.execucao5, ns.temAvaliacao, ns.avaliacao17))

    # 6
    graph.add((ns.execucao6, RDF.type, ns.Execucao))
    graph.add((ns.execucao6, ns.temCadeira, ns.LABP))
    graph.add((ns.execucao6, ns.temAno, ns.Ano2223))
    graph.add((ns.execucao6, ns.temProfessor, ns.AnaClaudio))
    graph.add((ns.execucao6, ns.temProfessor, ns.JoaoNeto))

    graph.add((ns.execucao6, ns.temAvaliacao, ns.avaliacao18))
    graph.add((ns.execucao6, ns.temAvaliacao, ns.avaliacao19))
    graph.add((ns.execucao6, ns.temAvaliacao, ns.avaliacao20))
    graph.add((ns.execucao6, ns.temAvaliacao, ns.avaliacao21))
    graph.add((ns.execucao6, ns.temAvaliacao, ns.avaliacao22))

    # 7
    graph.add((ns.execucao7, RDF.type, ns.Execucao))
    graph.add((ns.execucao7, ns.temCadeira, ns.EC))
    graph.add((ns.execucao7, ns.temAno, ns.Ano2021))
    graph.add((ns.execucao7, ns.temProfessor, ns.PauloUrbano))
    graph.add((ns.execucao7, ns.temProfessor, ns.GracaGaspar))

    graph.add((ns.execucao7, ns.temAvaliacao, ns.avaliacao23))
    graph.add((ns.execucao7, ns.temAvaliacao, ns.avaliacao24))
    graph.add((ns.execucao7, ns.temAvaliacao, ns.avaliacao25))

    # 8
    graph.add((ns.execucao8, RDF.type, ns.Execucao))
    graph.add((ns.execucao8, ns.temCadeira, ns.LABP))
    graph.add((ns.execucao8, ns.temAno, ns.Ano1516))
    graph.add((ns.execucao8, ns.temProfessor, ns.IsabelNunes))
    graph.add((ns.execucao8, ns.temProfessor, ns.BeatrizCarmo))

    graph.add((ns.execucao8, ns.temAvaliacao, ns.avaliacao26))
    graph.add((ns.execucao8, ns.temAvaliacao, ns.avaliacao27))
    graph.add((ns.execucao8, ns.temAvaliacao, ns.avaliacao28))
    graph.add((ns.execucao8, ns.temAvaliacao, ns.avaliacao29))
    graph.add((ns.execucao8, ns.temAvaliacao, ns.avaliacao30))

    # 9
    graph.add((ns.execucao9, RDF.type, ns.Execucao))
    graph.add((ns.execucao9, ns.temCadeira, ns.IP))
    graph.add((ns.execucao9, ns.temAno, ns.Ano2122))
    graph.add((ns.execucao9, ns.temProfessor, ns.AntoniaLopes))
    graph.add((ns.execucao9, ns.temProfessor, ns.Wellington))
    graph.add((ns.execucao9, ns.temProfessor, ns.GracaGaspar))

    graph.add((ns.execucao9, ns.temAvaliacao, ns.avaliacao31))
    graph.add((ns.execucao9, ns.temAvaliacao, ns.avaliacao32))
    graph.add((ns.execucao9, ns.temAvaliacao, ns.avaliacao33))

    return (graph, ns)


(g,n) = createGraph()


# ----------------------------------- Queries ------------------------------------------------------------
q_allcourses = """
    SELECT ?cname
    WHERE {
        ?c a :Cadeira;
            foaf:name ?cname
    } 
"""


q_allResults = """
    SELECT ?nome ?nota
    WHERE {
        ?aval foaf:name ?labelComponent .
        ?result :eResultadoDe ?aval ;
            :temNota ?nota ;
            :temAluno ?aluno .
        ?aluno :temNome ?nome
    } 
"""



print(g.serialize(format='turtle'))

print("///////////////////////////////////////////////////////////////////////////////////////////////////////////\n 1\n")

qres = g.query(q_allcourses)

for row in qres:
    print(row.cname)


print("\n///////////////////////////////////////////////////////////////////////////////////////////////////////////\n 2\n")

qres = g.query(q_allResults, initBindings = { "labelComponent": Literal("proj1 de EC(2021/2022)") } )

for row in qres:
    print(row.exec)


#print("///////////////////////////////////////////////////////////////////////////////////////////////////////////\n 3\n")