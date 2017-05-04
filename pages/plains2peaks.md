title: Plains2Peaks DP.LA Service Hub for Colorado and Wyoming
description: A regional DP.LA service hub using BIBFRAME and BIBCAT
order: 4

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

[MODS][MODS] short for *Metadata Object Description Schema* is a Library of
Congress XML metadata format used in many digital repositories, particularly
those repositories based on [Islandora][ISLAND].

## Important Links

*  [Plains2Peaks.org](https://plains2peaks.org/) - official service hub website
*  Github Source Code Repository [https://github.com/KnowledgeLinks/dpla-service-hub](https://github.com/KnowledgeLinks/dpla-service-hub)

[BIBCAT]: https://bibcat.org/
[DC]: http://dublincore.org/
[DPLA]: https://dp.la
[ISLAND]: http://islandora.ca/
[MODS]: http://www.loc.gov/standards/mods/
[RML]: http://rml.io/
