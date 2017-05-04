title: BIBFRAME
description: The Library of Congress's BIBFRAME is a linked data vocabulary for eventually replace MARC21.
order: 1 
downloads: contemporary-pottery.ttl

First released in 2011, the Bibliographic Framework, or [BIBFRAME][BF] is an effort by the
Library of Congress to replace [MARC21][MARC] in library systems.

![BIBFRAME 2.0 Model](http://www.loc.gov/bibframe/docs/images/bf2-model.jpg)  


## Primary BIBFRAME 2.0 Classes
### BIBFRAME Work
<i class="fa fa-lightbulb-o fa-4x" aria-hidden="true"></i>
**Definition**: *The highest level of abstraction, a Work, in the BIBFRAME context, reflects the conceptual essence 
of the cataloged resource:  authors, languages, and what it is about (subjects).* [source][BFOVERVIEW] 

<pre>&lt;http://example.org/3506720#Work&gt; a bf:Text,
        bf:Work ;
    rdfs:label "Contemporary pottery techniques in Southern and Central Mexico /" ;
    bf:contribution [ a bf:Contribution ;
            bf:agent &lt;http://example.org/3506720#Agent710-16&gt; ;
            bf:role &lt;http://id.loc.gov/vocabulary/relators/ctb&gt; ],
        [ a  bf:Contribution ;
            bf:agent &lt;http://example.org/3506720#Agent100-9&gt; ;
            bf:role &lt;http://id.loc.gov/vocabulary/relators/ctb&gt; ] ;
    bf:genreForm &lt;http://id.loc.gov/vocabulary/marcgt/bib&gt; ;
    bf:hasInstance &lt;http://example.org/3506720#Instance&gt; ;
    bf:hasSeries &lt;http://example.org/3506720#Work830-17&gt; ;
    bf:language &lt;http://id.loc.gov/vocabulary/languages/eng&gt; ;
    bf:seriesEnumeration "22, pt. 1" ;
    bf:subject &lt;http://example.org/3506720#Topic650-15&gt; ;
    bf:title [ a bf:Title ;
      rdfs:label "Contemporary pottery techniques in Southern and Central Mexico /" ;
      bf:mainTitle "Contemporary pottery techniques in Southern and Central Mexico" ] .
</pre>

### BIBFRAME Instance
<i class="fa fa-commenting-o fa-4x" aria-hidden="true"></i>
**Definition**:  *A Work may have one or more individual, material embodiments, for example, a particular 
published form. These are Instances of the Work.  An Instance reflects information such as its publisher, 
place and date of publication, and format.* [source][BFOVERVIEW]

<pre>&lt;http://example.org/3506720#Instance&gt; a bf:Instance ;
    rdfs:label "Contemporary pottery techniques in Southern and Central Mexico /" ;
    bf:dimensions "27 cm." ;
    bf:extent [ a bf:Extent ;
            rdfs:label "35 p., 6 leaves of plates" ] ;
    bf:illustrativeContent &lt;http://id.loc.gov/vocabulary/millus/ill&gt;,
        &lt;http://id.loc.gov/vocabulary/millus/map&gt;,
        &lt;http://id.loc.gov/vocabulary/millus/plt&gt; ;
    bf:instanceOf &lt;http://example.org/3506720#Work&gt; ;
    bf:issuance &lt;http://id.loc.gov/vocabulary/issuance/mono&gt; ;
    bf:note [ a bf:Note ;
            rdfs:label "ill., map (fold.)" ;
            bf:noteType "Physical details" ],
        [ a bf:Note ;
            rdfs:label "Bibliography: p. 33." ;
            bf:noteType "bibliography" ] ;
    bf:provisionActivity [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:agent [ a bf:Agent ;
                    rdfs:label "Tulane University" ] ;
            bf:date "1955" ;
            bf:place [ a bf:Place ;
                    rdfs:label "New Orleans" ] ],
        [ a bf:ProvisionActivity,
                bf:Publication ;
            bf:date "1955"^^&lt;http://id.loc.gov/datatypes/edtf&gt; ;
            bf:place &lt;http://id.loc.gov/vocabulary/countries/lau&gt; ] ;
    bf:provisionActivityStatement "New Orleans : Tulane University, 1955." ;
    bf:responsibilityStatement "George M. Foster" ;
    bf:seriesEnumeration "no. 22 pt. 1." ;
    bf:seriesStatement "Tulane University. Middle American Research Institute. Publication." ;
    bf:supplementaryContent [ a bf:SupplementaryContent ;
       rdfs:label "Index present" ] ;
    bf:title [ a bf:Title ;
      rdfs:label "Contemporary pottery techniques in Southern and Central Mexico /" ;
      bf:mainTitle "Contemporary pottery techniques in Southern and Central Mexico" ] .
</pre>
### BIBFRAME Item
<i class="fa fa-file-text fa-4x" aria-hidden="true"></i>
**Definition**: *An item is an actual copy (physical or electronic) of an Instance. It reflects information 
such as its location (physical or virtual), shelf mark, and barcode.* [source][BFOVERVIEW]
<pre>&lt;http://example.org/3506720#Item&gt; a bf:Item ;
    bf:heldBy &lt;https://www.coloradocollege.edu/library/&gt; ;
    bf:itemOf &lt;http://example.org/3506720#Instance&gt; .
</pre> 
<hr>
## Secondary BIBFRAME 2.0 Classes
### BIBFRAME Agent with Person and Organization Subclasses
<i class="fa fa-user fa-3x" aria-hidden="true"></i>
<i class="fa fa-home fa-3x" aria-hidden="true"></i>
**Definition**:  *Agents are people, organizations, jurisdictions, etc., associated with a Work or Instance 
through roles such as author, editor, artist, photographer, composer, illustrator, etc.*  [source][BFOVERVIEW]

An interesting note is that `bf:Agent` class is actually a subclass of the [FOAF](http://xmlns.com/foaf/0.1/Person)
Person class that contains additional properites normally associated with a Person including `foaf:familyName`,
and `foaf:givenName`.

#### Example BIBFRAME Organization
<pre>&lt;http://example.org/3506720#Agent710-16&gt; a bf:Agent,
        bf:Organization ;
    rdfs:label "Tulane University. Middle American Research Institute." . 
</pre>

#### Example BIBFRAME Person
<pre>&lt;http://example.org/3506720#Agent100-9&gt; a bf:Agent,
        bf:Person ;
    rdfs:label "Foster, George M. (George McClelland), 1913-2006." .
</pre>

### BIBFRAME Subjects
<i class="fa fa-user fa-3x" aria-hidden="true"></i>
<i class="fa fa-home fa-3x" aria-hidden="true"></i>
<i class="fa fa-tag fa-3x" aria-hidden="true"></i>
<i class="fa fa-map-marker fa-3x" aria-hidden="true"></i>
**Definition**: *A Work might be "about" one or more concepts. Such a concept is said to be a "subject" 
of the Work. Concepts that may be subjects include topics, places, temporal.* [source][BFOVERVIEW]
<pre>&lt;http://example.org/3506720#Topic650-15&gt; a bf:Topic,
        madsrdf:ComplexSubject ;
    rdfs:label "Pottery--Mexico." ;
    bf:source [ a bf:Source ;
            bf:code "lcsh" ] ;
    madsrdf:authoritativeLabel "Pottery--Mexico." ;
    madsrdf:componentList ( [ a madsrdf:Topic ;
                madsrdf:authoritativeLabel "Pottery" ] [ a madsrdf:Geographic ;
                madsrdf:authoritativeLabel "Mexico" ] ) ;
    madsrdf:isMemberofMADSScheme &lt;http://id.loc.gov/authorities/subjects&gt; 
</pre>

### BIBFRAME Events
<i class="fa fa-microphone fa-3x" aria-hidden="true"></i>
<i class="fa fa-music fa-3x" aria-hidden="true"></i>
<i class="fa fa-video-camera fa-3x" aria-hidden="true"></i>
<i class="fa fa-bullhorn fa-3x" aria-hidden="true"></i>

**Definition**: *Occurrences, the recording of which may be the content of a Work.* [source][BFOVERVIEW]


[BF]: http://www.loc.gov/bibframe/docs/index.html
[BFOVERVIEW]: https://www.loc.gov/bibframe/docs/bibframe2-model.html
[MARC]: https://www.loc.gov/marc/bibliographic/
