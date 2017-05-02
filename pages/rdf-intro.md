title: Introduction to RDF
description: Introducing (RDF) that is made of 3-part subject, predicate, object statements called triples. The big shift for libraries is going from managing MARC records to managing RDF triples
downloads: du-knowledge-graph.ttl
order: 0

Linked Data in libraries is constructed using Resource Description Framework (RDF) graphs, 
a type of directed graphs, where the nodes are made up
of either IRI (international resource indicator i.e. URLs or URIs), blank nodes (a 
type of identifier placeholder in a RDF graph), or literal values. 

Originating with the 
[World Wide Web Consortium][W3C] (W3C) specifications, RDF graphs are built using three element 
statements called <strong>triples</strong> that model relationships between resources, 
IRIs, and descriptive information.

In a RDF triple, the first element is called a **subject** and represents 
a resource with the second element, the **predicate**, describing an aspect
that connects to the third element, an **object** made up a value. One or more
triples make up a RDF graph.  



### Subject
Subjects must be either an IRI or a blank node and represents the resource or entity

Examples:
    
*   &lt;[http://www.du.edu/](http://www.du.edu/)&gt;
*   &lt;[http://id.loc.gov/authorities/subjects/sh85076723](http://id.loc.gov/authorities/subjects/sh85076723)&gt;
*   _:bnodeN99c9f143d0944c0898824e645c6885a5
    
## Predicate
A relationship between the subject and object is a predicate, also called a property. 
A predicate can only be an IRI.

Examples:

*   &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#type&gt;
*   &lt;http://schema.org/Book&gt;
*   &lt;http://id.loc.gov/ontologies/bibframe/Electronic&gt;

## Object
Object must be either an IRI, blank node, or literal value.

Examples:

*   &lt;[http://schema.org/CollegeOrUniversity](http://schema.org/CollegeOrUniversity)&gt;
*   "University of Denver"
*   _:bnodeNe0fe1c3caa9f499b8c405723886fd093

## Example RDF Graph in Turtle Serialization

<pre>@prefix bf: &lt;http://id.loc.gov/ontologies/bibframe/&gt; .
@prefix owl: &lt;http://www.w3.org/2002/07/owl#&gt; .
@prefix rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt; .
@prefix rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt; .
@prefix schema: &lt;http://schema.org/&gt; .
@prefix xml: &lt;http://www.w3.org/XML/1998/namespace&gt; .
@prefix xsd: &lt;http://www.w3.org/2001/XMLSchema#&gt; .

&lt;http://www.du.edu/&gt; a schema:CollegeOrUniversity ;
    rdfs:label "University of Denver"@en ;
    schema:department [ a bf:Organization ;
            rdfs:label "Library and Information Science"@en ;
            bf:subject &lt;http://id.loc.gov/authorities/subjects/sh85076723&gt; ;
            owl:sameAs &lt;http://morgridge.du.edu/programs/library-and-information-science/&gt; ] .
</pre>

[BF]: http://www.loc.gov/bibframe/docs/index.html
[MARC]: https://www.loc.gov/marc/bibliographic/
[SCHEMA]: http://schema.org/
[W3C]: https://www.w3.org/

