title: Colorado Alliance of Research Libraries BIBCAT Project
description: The Alliance BIBCAT Project is publishing Schema.org Library Linked Data for search engine indexing using BIBFRAME
order: 3 

Last summer a library linked data project was started with the 
[Colorado Alliance of Research Libraries][CARL] to publish  
converted MARC21 records the Alliance uses in their Gold Rush Comparison service 
to the web in a format that Google and other search engines can use
to index the site. The overarching goal of the project was an effort to
improve the search ranking of materials in Alliance's member libraries
catalogs. 


## Build-Measure-Learn (BML) Iteration One
Using a modified version of the Lean Startup [Build-Measure-Learn](https://en.wikipedia.org/wiki/Lean_startup#Build.E2.80.93Measure.E2.80.93Learn)
iterative development process, we constructed a minimum viable product, live at [bibcat.coalliance.org][ALLIANCE_BC] 

### Build
About 160,000 MARC records, half from [Colorado College](https://www.coloradocollege.edu/)
and half from [University of Colorado - Boulder](http://www.colorado.edu/), were 
converted to BIBFRAME 2.0 entities with the Instance URI being generated and linked 
from a XML site index file hosted at [http://bibcat.coalliance.org/][ALLIANCE_BC]. 
For the Instance URI, the permanent link back to the library's OPAC record was minted 
by extracting the value for subfield a from a MARC 907 field and then creating a bib code substring
that was appended to a URL. The BIBCAT Instance URL initially resolved to a JSON-LD page 
that was generated through SPARQL queries to map BIBFRAME to Schema.org. Further 
development was initiated after testing the initial release when Google search results were
including the BIBFRAME Instance page and we wanted a minimum HTML page.

For example, the following [http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008](http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008)
BIBFRAME Instance from CU is referenced from an XML sitemap. Here are the source RDF
triples for the BIBFRAME Item and Instance:

<pre><code>
&lt;http://libraries.colorado.edu/record=b6921805&gt; a bf:Item ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2016-10-05T00:46:50.313787" ;
            rdf:value "Generated by BIBCAT version 1.4.0 from KnowledgeLinks.io"@en ] ;
    bf:heldBy &lt;http://www.colorado.edu/libraries/&gt; ;
    bf:itemOf &lt;http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008&gt; ;
    bf:shelfMark [ a bf:ShelfMarkLcc ;
            rdf:value "TA355.P37 2012" ] .

&lt;http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008&gt; a bf:Instance ;
    bf:carrier [ a bf:Carrier ;
            rdf:value "cr",
                "online bron" ] ;
    bf:copyrightDate "©2012." ;
    bf:extent [ a bf:Extent ;
            rdf:value "1 online resource (xiii, 330 pages)" ] ;
    bf:generationProcess [ a bf:GenerationProcess ;
            bf:generationDate "2016-10-05T00:46:50.202287" ;
            rdf:value "Generated by BIBCAT version 1.4.0 from KnowledgeLinks.io"@en ] ;
    bf:identifiedBy [ a bf:Isbn ;
            rdf:value "1283443996",
                "1461410436 (electronic bk.)",
                "9781283443999",
                "9781461410430 (electronic bk.)" ] ;
    bf:instanceOf [ a bf:Work ;
            bf:originDate "2012" ] ;
    bf:provisionActivity [ a bf:Publication ;
            relators:pbl "Springer," ] ;
    bf:subject [ a bf:Topic ;
            rdf:value "Parametric vibration." ],
        [ a bf:Topic ;
            rdf:value "Dynamics." ] ;
    bf:summary [ a bf:Summary ;
            rdf:value ""The subject of the book is parametric resonance in marine and mechanical systems with focus on detection, mathematical modeling, and control. The book contains new results on modeling, detection, and control of parametric resonance and it is a supplement to engineers who are familiar with nonlinear systems"--Page v." ] ;
    bf:title [ a bf:InstanceTitle ;
            bf:mainTitle "Parametric resonance in dynamical systems" ] .

</code></pre>

Instead of embedding Schema.org as Microdata in the 
[http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008](http://bibcat.coalliance.org/32a0a540-8a95-11e6-999f-005056c00008) HTML page, 
we published the Schema.org metadata as JSON-LD in a `script` tag.
<pre><code>
{
   "@context": "http://schema.org",
   "@type": "Book",
   "author": [],
   "datePublished": [
      "2012"
   ],
   "isbn": [
      "1283443996",
      "1461410436 (electronic bk.)",
      "9781283443999",
      "9781461410430 (electronic bk.)"
   ],
   "mainEntityOfPage": {
      "@id": "http://libraries.colorado.edu/record=b6921805",
      "@type": "CreativeWork",
      "contentLocation": {
         "@id": "http://www.colorado.edu/libraries/",
         "@type": "Library",
         "address": {
            "@type": "PostalAddress",
            "addressLocality": "Boulder",
            "addressRegion": "Colorado",
            "postalCode": "80309-0184",
            "streetAddress": "1720 Pleasant Street"
         },
         "geo": {
            "@type": "GeoCoordinates",
            "latitude": "40.0087 N",
            "longitude": "105.2709 W"
         },
         "image": "http://www.colorado.edu/libraries/sites/default/files/styles/large_wide_thumbnail/public/callout/norlin.jpg",
         "name": "University Libraries - University of Colorado Boulder",
         "priceRange": "0",
         "telephone": "303-492-8705"
      }
   },
   "name": "Parametric resonance in dynamical systems",
   "publisher": {
      "@type": "Organization",
      "logo": {
         "@type": "ImageObject",
         "height": "90px",
         "url": "https://www.coalliance.org/sites/all/themes/minim/logo.png",
         "width": "257px"
      },
      "name": "Colorado Alliance of Research Libraries"
   },
   "version": "0.7.0"
}
</code></pre>

Part of the requirements for this project is to introduce the geolocation of the library that
holds the BIBFRAME Item in order to provide search engines hints on ranking
search results from BIBCAT by the geo coordinates (i.e. a person searching in Boulder should
get the CU Boulder Item hit before a Colorado College hit of the same item)

### Measure 
To measure the success and failures of the project iteration was a 
challenge as the specifics of how and why Google indexes and ranks a particular
web page is deliberately opaque. For more unique titles, the [bibcat.coalliance.org][ALLIANCE_BC]
BIBFRAME Instance pages would show up in individual testing but the corresponding
BIBFRAME Item link back to the institution's ILS was not appearing in Google. We also
continued to troubleshoot a problem where Google was not indexing the entire site, only the first
50k BIBFRAME Instances.   

### Learn
Working on this project required more research in Search Engine Optimization (SEO) for 
websites and created new requirements and enhancements for the second iteration of the
project. We
discovered that the ILS vendor for both Colorado College and University of Colorado Boulder
as a default prohibit search engine crawlers from indexing the public OPAC pages of each
library's catalog. 


## Build-Measure-Learn (BML) Iteration Two
Taking the lessons learned from the first BML iteration, we decided on a couple of changes
to the project for the second BML iteration for this project in the current **BUILD** phase
of this second iteration. We are improving Geo support by integrating the local HTML 
Geo API in the browser to rank all BIBFRAME Items in the BIBFRAME Instance web display.  

To assist in testing, a third partner has been added to the pilot, 
[SUNY Buffalo State](http://suny.buffalostate.edu/) which requires some slight integration
with their [Summon](http://www.proquest.com/products-services/The-Summon-Service.html)
discovery layer.

### Build
We decided to stop
trying to promote the vendor ILS link but instead mint a new BIBFRAME Item URL and landing
page that will appear in Google searches. Instead of using UUIDs for the BIBFRAME Instances
and Items URLs we decided to adopt SEO suggestions and mint URLs based on a "slugged" 
title. BIBFRAME Items would share the Instance's URL but with a forward slash and the slugged  
Institution name. 

For our current example the BIBFRAME Instance URI would now be
`https://bibcat.coalliance.org/parametric-resonance-in-dynamical-systems` and the BIBFRAME
Item URI would now be 
`https://bibcat.coalliance.org/parametric-resonance-in-dynamical-systems/university-of-colorado-boulder`

We also decided to use a newly released Library of Congress project for transforming
MARC XML into BIBFRAME RDF available at [https://github.com/lcnetdev/marc2bibframe2][MRC2BF2]
that we then enhance by replacing the URIs in the RDF with the newly
minted BIBFRAME Instances and Items.

## Important Links

*   [http://bibcat.coalliance.org/][ALLIANCE_BC] website hosting published RDF linked data
*   Github Source Code Repository [https://github.com/KnowledgeLinks/alliance-bibcat](https://github.com/KnowledgeLinks/alliance-bibcat)

[ALLIANCE_BC]: http://bibcat.coalliance.org/
[CARL]: https://coalliance.org/
[MRC2BF2]: https://github.com/lcnetdev/marc2bibframe2 
