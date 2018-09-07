from neo4j.v1 import GraphDatabase


#1.install neo4j

#2.make neo4j serve as server  con/neo4j.conf 
#dbms.connectors.default_listen_address=0.0.0.0
#dbms.connectors.default_advertised_address=0.0.0.0 

#3.start,make constraint for unique node by run 'CREATE CONSTRAINT ON (node:Node) ASSERT node.name IS UNIQUE' in neo4j
#4.build

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "123"))

def add_node(tx, name1, relation,name2):

    tx.run("MERGE (a:Node {name: $name1}) "
        "MERGE (b:Node {name: $name2}) "
           "MERGE (a)-[:"+relation+"]-> (b)",
           name1=name1,name2=name2)



with driver.session() as session:
    lines=open('./triples.txt','r').readlines()
    print(len(lines))
    pattern=''
    for i,line in enumerate(lines):
        arrays=line.split('$$')
        name1=arrays[0]
        relation=arrays[1].replace('：','').replace(':','').replace('　','').replace(' ','').replace('【','').replace('】','')
        name2=arrays[2]
        print(str(i))
        try:
            session.write_transaction(add_node, name1, relation,name2)
        except Exception as e:
            print( name1, relation,name2,str(e))