title: Plains2Peaks DP.LA Service Hub for Colorado and Wyoming
description: A regional DP.LA service hub using BIBFRAME and BIBCAT
order: 4
downloads: cc-example.ttl,denver-public-example.ttl

![Plains2Peaks Temporary Logo](https://bibcat.org/static/img/plains2peaks-tmp-logo.png)

In 2016 the State of Library of Colorado started an effort to 
provide a [DP.LA][DPLA] service hub for states of Colorado and Wyoming. 
This project uses [BIBCAT][BIBCAT] to transform different formats and 
vocabularies from multiple sources including Denver Public Library's 
RDF [Dublin Core][DC], Colorado College and University of Wyoming [MODS][MODS] metadata, 
and a metadata provided as custom Comma-Separated-Value file from the History Colorado museum 
into BIBFRAME 2.0 entities stored in a triplestore. 

[BIBCAT][BIBCAT] uses RDF-based rules, based upon [RDF Mapping Language][RML] to ingest 
these different types of sources while allowing for easy customization and modification 
through simple editing of RDF turtle MAP file. 

## Build-Measure-Learn (BML) Iteration One
For the pilot [DP.LA][DPLA] service hub, we are targeting approximately 50,000 source
records to ingest into our RDF triplestore as BIBFRAME 2.0 Entities. We are actively
building out [BIBCAT][BIBCAT]'s functionality to generate an XML [ResourceSync](http://www.openarchives.org/rs/toc)
that will link to JSON-LD representations of the BIBFRAME Works, Instances, and Items
as [DP.LA][DPLA] Metadata Application Profile version 4 ([MAPv4](https://dp.la/info/developers/map/)). 

### MODS Example from Colorado College Digital CC
![Van Diest Map from Colorado College](https://digitalcc.coloradocollege.edu/islandora/object/coccc%3A17900/datastream/PREVIEW/view)


[MODS][MODS] short for *Metadata Object Description Schema* is a Library of
Congress XML metadata format used in many digital repositories, particularly
those repositories based on [Islandora][ISLAND].

For this example, the BIBFRAME Item will be the link to [Van Diet Maps](https://digitalccbeta.coloradocollege.edu/pid/coccc:6286)
in Colorado College's [Islandora][ISLAND] repository at 
[https://digitalcc.coloradocollege.edu/islandora/object/coccc:6286](https://digitalcc.coloradocollege.edu/islandora/object/coccc:6286)
and the BIBFRAME Instance is a minted URI with base url of [https://plains2peaks.org/][P2P] followed by
a UUID. The source [MODS XML](https://digitalcc.coloradocollege.edu/islandora/object/coccc%3A6286/datastream/MODS/view) is 
transformed into the following RDF triples in Turtle format:
<pre><code>  
&lt;https://digitalcc.coloradocollege.edu/islandora/object/coccc:6286&gt; a bf:Item ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2017-05-04T18:22:16.109466" ;
            rdf:value "Generated by BIBCAT version 1.8.1 from KnowledgeLinks.io"^^xsd:string ] ;
    bf:heldBy &lt;https://www.coloradocollege.edu/library/&gt; ;
    bf:itemOf "https://plains2peaks.org/99f41c7e-30f6-11e7-83a7-005056c00008" .

&lt;https://plains2peaks.org/99f41c7e-30f6-11e7-83a7-005056c00008&gt; a bf:Instance ;
    bf:extent [ a bf:Extent ;
            rdf:value "5 maps"^^xsd:string ] ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2017-05-04T18:22:16.109466" ;
            rdf:value "Generated by BIBCAT version 1.8.1 from KnowledgeLinks.io"^^xsd:string ] ;
    bf:genreForm [ a bf:GenreForm ;
            rdf:value "map"^^xsd:string ] ;
    bf:language [ a bf:Language ;
            rdf:value "English"^^xsd:string ] ;
    bf:note [ a bf:Note ;
            rdf:noteType "admin"@en ;
            rdf:value "Original files digitized by an outside firm at the expense of researchers in 2012."^^xsd:string ] ;
    bf:subject [ a bf:Topic ;
            rdf:value "Costilla County (Colo.)"^^xsd:string ] ;
    bf:summary [ a bf:Summary ;
            rdf:value "Maps of Southern Colorado and Northern New Mexico, including the Costilla Estate in Costilla County."^^xsd:string ] ;
    bf:title [ a bf:InstanceTitle ;
            bf:mainTitle "Van Diest Maps"^^xsd:string ],
        [ a bf:InstanceTitle ;
            bf:mainTitle "Costilla Estate maps"^^xsd:string ],
        [ a bf:VarientTitle ;
            bf:mainTitle "Costilla Estate maps"^^xsd:string ] ;
    relators:aut &lt;https://plains2peaks.org//99f4cc50-30f6-11e7-89cc-005056c00008&gt; .

&lt;https://plains2peaks.org//99f4cc50-30f6-11e7-89cc-005056c00008&gt; a bf:Person ;
    rdfs:label "Van Diest, Edmond C."^^xsd:string .
</code></pre>

### Dublin Core Example from Denver Public Library
![Native American on Horseback](http://cdm16079.contentdm.oclc.org/utils/ajaxhelper/?CISOROOT=p15330coll22&CISOPTR=6&action=2&DMSCALE=15&DMWIDTH=512&DMHEIGHT=403&DMX=0&DMY=0&DMTEXT=&DMROTATE=0)


The Denver Public Library uses OCLC's [ContentDM][CDM] to host their over 100,000 digital objects 
in their repository. [ContentDM][CDM] currently exports [Dublin Core]() metadata records that we
then transform into BIBFRAME RDF triples. The BIBFRAME Item URI is the link back to the 
[ContentDM][CDM] at [http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/6](http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/6)
the BIBFRAME Instance URI is minted `https://plains2peaks.org/3e89592c-e40f-11e6-8180-005056c00008`. 

Here is the BIBFRAME Output in Turtle Format
<pre><code>
&lt;http://cdm16079.contentdm.oclc.org:80/cdm/ref/collection/p15330coll22/id/6&gt; a bf:Item ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2017-01-26T21:34:41.177594" ;
            rdf:value "Generated by BIBCAT version 1.7.0 from KnowledgeLinks.io"@en ] ;
    bf:heldBy &lt;http://denverpubliclibrary.org/&gt; ;
    bf:itemOf &lt;https://plains2peaks.org/3e89592c-e40f-11e6-8180-005056c00008&gt; ;
    bf:usageAndAccessPolicy [ a bf:UsePolicy ;
            rdf:value "Restrictions applying to use or reproduction of this image available from the Western History/Genealogy Dept., Denver Public Library." ] .

&lt;https://plains2peaks.org/3e89592c-e40f-11e6-8180-005056c00008&gt; a bf:Instance ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2017-01-26T21:34:41.086576" ;
            rdf:value "Generated by BIBCAT version 1.7.0 from KnowledgeLinks.io"@en ] ;
    bf:identifiedBy [ a bf:Local ;
            rdf:value "NS-856" ],
        [ a bf:Local ;
            rdf:value "00105856.tif" ] ;
    bf:instanceOf [ a bf:Work ;
            bf:originDate "[between 1885 and 1900?]" ] ;
    bf:language [ a bf:Language ;
            rdf:value "eng" ] ;
    bf:layout [ a bf:Layout ;
            rdf:value """1 photoprint ; 12 x 17 cm. (4 1/2 x 6 3/4 in.)
Photograph""" ] ;
    bf:note [ a bf:Note ;
            rdf:value """A Native American man rides a horse in front of a group of Native American men on horseback in a dirt arena during a rehearsal for Buffalo Bill's Wild West Show. Several of the men wear small clusters of feathers on the backs of their heads. A large tent is in the background at the far end of the arena.
Photoprint has "31" handwritten in middle left side.""" ],
        [ a bf:Note ;
            rdf:value "Vintage photographic print." ],
        [ a bf:Note ;
            rdf:value "Title supplied by cataloger." ],
        [ a bf:Note ;
            rdf:value "R7001058569" ] ;
    bf:partOf [ a pcdm:Collection ;
            rdfs:label """Salsbury collection, Buffalo Bill's Wild West Show.
Image File: ZZR700105856

http://photoswest.org/cgi-bin/imager?00105856+NS-856""" ] ;
    bf:subject [ a bf:Topic ;
            rdf:value "Indians of North America--Clothing & dress--1880-1900.; Wild west shows--1880-1920.; Rehearsals--1900-1910.; Buffalo Bill, 1846-1917.; Buffalo Bill's Wild West Show." ] ;
    bf:title [ a bf:InstanceTitle ;
            bf:mainTitle "Native Americans on horseback" ] .

 

</code></pre>

## Important Links

*  [Plains2Peaks.org](https://plains2peaks.org/) - official service hub website
*  Github Source Code Repository [https://github.com/KnowledgeLinks/dpla-service-hub](https://github.com/KnowledgeLinks/dpla-service-hub)

[BIBCAT]: https://bibcat.org/
[CDM]: http://www.oclc.org/en/contentdm.html
[DC]: http://dublincore.org/
[DPLA]: https://dp.la
[ISLAND]: http://islandora.ca/
[MODS]: http://www.loc.gov/standards/mods/
[P2P]: https://plains2peaks.org/
[RML]: http://rml.io/
