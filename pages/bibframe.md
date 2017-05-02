title: BIBFRAME
description: The Library of Congress's BIBFRAME is a linked data vocabulary for eventually replace MARC21.
order: 1 

First released in 2011, the Bibliographic Framework, or [BIBFRAME][BF] is an effort by the
Library of Congress to replace [MARC21][MARC] in library systems.

![BIBFRAME 2.0 Model](http://www.loc.gov/bibframe/docs/images/bf2-model.jpg)  


## Primary BIBFRAME 2.0 Classes
### BIBFRAME Work
<i class="fa fa-lightbulb-o fa-4x" aria-hidden="true"></i>
**Definition**: *The highest level of abstraction, a Work, in the BIBFRAME context, reflects the conceptual essence 
of the cataloged resource:  authors, languages, and what it is about (subjects).* [source][BFOVERVIEW] 

### BIBFRAME Instance
<i class="fa fa-commenting-o fa-4x" aria-hidden="true"></i>
**Definition**:  *A Work may have one or more individual, material embodiments, for example, a particular 
published form. These are Instances of the Work.  An Instance reflects information such as its publisher, 
place and date of publication, and format.* [source][BFOVERVIEW]

### BIBFRAME Item
<i class="fa fa-file-text fa-4x" aria-hidden="true"></i>
**Definition**: *An item is an actual copy (physical or electronic) of an Instance. It reflects information 
such as its location (physical or virtual), shelf mark, and barcode.* [source][BFOVERVIEW]
 

## Secondary BIBFRAME 2.0 Classes
### BIBFRAME Agent with Person and Organization Subclasses
<i class="fa fa-user fa-3x" aria-hidden="true"></i>
<i class="fa fa-home fa-3x" aria-hidden="true"></i>
**Definition**:  *Agents are people, organizations, jurisdictions, etc., associated with a Work or Instance 
through roles such as author, editor, artist, photographer, composer, illustrator, etc.*  [source][BFOVERVIEW]

An interesting note is that `bf:Agent` class is actually a subclass of the [FOAF](http://xmlns.com/foaf/0.1/Person)
Person class that contains additional properites normally associated with a Person including `foaf:familyName`,
and `foaf:givenName`.

### BIBFRAME Subjects
<i class="fa fa-user fa-3x" aria-hidden="true"></i>
<i class="fa fa-home fa-3x" aria-hidden="true"></i>
<i class="fa fa-tag fa-3x" aria-hidden="true"></i>
<i class="fa fa-map-marker fa-3x" aria-hidden="true"></i>
**Definition**: *A Work might be "about" one or more concepts. Such a concept is said to be a "subject" 
of the Work. Concepts that may be subjects include topics, places, temporal. [source][BFOVERVIEW]

### BIBFRAME Events
<i class="fa fa-microphone fa-3x" aria-hidden="true"></i>
<i class="fa fa-music fa-3x" aria-hidden="true"></i>
<i class="fa fa-video-camera fa-3x" aria-hidden="true"></i>
<i class="fa fa-bullhorn fa-3x" aria-hidden="true"></i>

**Definition**: *Occurrences, the recording of which may be the content of a Work.* [source][BFOVERVIEW]


[BF]: http://www.loc.gov/bibframe/docs/index.html
[BFOVERVIEW]: https://www.loc.gov/bibframe/docs/bibframe2-model.html
[MARC]: https://www.loc.gov/marc/bibliographic/


