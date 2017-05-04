title: Schema.org Metadata
description: Schema.org RDF is a community Linked-Data Vocabulary and Extensions for the Semantic Web
order: 2

One of the most popular metadata vocabularies is [schema.org][SCHEMA], a RDF vocabulary that was 
originally founded by Google, Microsoft, Pinterest, and others, as a way to provide structured
data on the Internet. [Schema.org][SCHEMA] encourages the use of [microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))
to directly embedded metadata within the HTML of a webpage. [Schema.org][SCHEMA] also has a robust extension process
with officially sponsored vocabularies that extend [schema.org][SCHEMA] into other knowledge domains. The Library community
has an official extension [bib.schema.org](http://bib.schema.org/) that includes library-specific classes like 
[Audiobook](http://bib.schema.org/Audiobook), [Collection](http://bib.schema.org/Collection), [Newspaper](http://bib.schema.org/Newspaper),
and [Thesis](http://bib.schema.org/Thesis). Other extensions include [automobiles](http://auto.schema.org/) and 
[health and life sciences](http://health-lifesci.schema.org/).

[Schema.org][SCHEMA] has a hierarchy of classes with [Thing](http://schema.org/Thing) being the most 
basic entity with such subclasses as [Book](http://schema.org/Book), [Movie](http://schema.org/Movie), 
[Event](http://schema.org/Event), [Organization](http://schema.org/Organization), [Person](http://schema.org/Person)

<pre><code>&lt;div itemscope="" itemtype="http://schema.org/Book"&gt;
    &lt;h1 itemprop="name"&gt;
        Contemporary pottery techniques in Southern and Central Mexico /
    &lt;/h1&gt;
    by 
    &lt;span itemprop="author" 
       itemtype="http://schema.org/Person"&gt; 
       George M. Foster
    &lt;/span&gt;
 &lt;/div&gt;
</code></pre>

## Using [Schema.org][SCHEMA] in Library Applications
A web-based application at Colorado College allows senors to self-submit 
their thesis along with any accompanying datasets, video, or audio to Colorado College's 
[Fedora-based institutional repository](https://digitalccbeta.coloradocollege.edu). This
application queries a Colorado College RDF Knowledge Graph to generate a list of 
academic departments at the college along with faculty advisors. The Knowledge Graph
is built using existing websites with faculty being generated an URI if the faculty
member does not have a [ORCID](https://orcid.org/) or [LC Name Authority URI](http://id.loc.gov/) id.  

Below are Colorado College RDF Files that make Knowledge Graph for the 2016-2017 Academic year:

*  [colorado-college.ttl][CCBASE] - set of basic facts about the college that rarely change including
   department and different units on campus.
*  [cc-people.ttl][CCPEOPLE] - Triples for people associated with the Colorado College, focused
   on administrators, faculty and staff.
*  [cc-2016-2017.ttl][CC2016_2017] - Triples for the academic year, associates the departments 
   and link to the faculty and rank (professor, associate professor, adjunct, etc.) 

 
[SCHEMA]: http://schema.org/
[CCBASE]: https://github.com/Tutt-Library/tiger-catalog/blob/master/custom/colorado-college.ttl
[CCPEOPLE]: https://github.com/Tutt-Library/tiger-catalog/blob/master/custom/cc-people.ttl
[CC2016_2017]: https://github.com/Tutt-Library/tiger-catalog/blob/master/custom/cc-2016-2017.ttl
