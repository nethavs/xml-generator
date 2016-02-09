<p />
xml-generator is a Python based toolkit for generation of well formed <br />
XML sample documents. Its primary purpose is to generate documents for <br />
performance evaluation of XML parsing routines and data mining experimentation.<br />
<p />
xml-generator, in its current implementation, is a command line based tool.<br />
It allows users to specify the size, depth and the randomness of the generated <br />
XML tree. The text nodes are populated with randomly chosen words from the vocabulary <br />
of several hundred English words.<br />
<p />
xml-generator generates a 100 MB XML document in ~17 sec and 1GB document <br />
in ~3.5 min on P 2.4 dual core machine with 4 GB of memory.