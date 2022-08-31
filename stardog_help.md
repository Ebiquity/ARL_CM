# Stardog Help

## Installing stardog on your computer

(1) goto https://www.stardog.com/get-started/

(2) click on download, creating an account if needed

(3) get license key

(4) install version for your computer,
https://docs.stardog.com/get-started/install-stardog/

(5) create a directory that stardog will use to to store your databases
(e.g. /var/stardog on unix or macosx)
(5.1) put the license key in that directory
(5.2) on unix ands mac set STARDOG_HOME as an alias for this directory

(5) start the stardog server using the stardog-admin program that was
installed

    stardog-admin server start

The stardog-admin program can also be used to create or drop databases,
load data into them, and many other tasks.  Type stardog-admin with no
arguments to see the top-level commands.  Type "stardog-admin help"
for more details.

The default is that the server's endpoint is to
http://localhost:5820.  This will be used by the web intergace and can
also be used by programs to send SPARAL queries to the server.



## The stardog command

Stardog can be used from the command line via the stardog command

type "stardog help" to see what the options are

Example:

stardog query execute sim "select * where { ?s ?p ?o } limit 3"

+--------------------------------------+----------+------------------------+
|                  s                   |    p     |           o            |
+--------------------------------------+----------+------------------------+
| http://purl.org/artiamas/cm/         | rdf:type | owl:Ontology           |
| http://purl.org/artiamas/cm/wikidata | rdf:type | owl:AnnotationProperty |
| http://purl.org/artiamas/cm/action   | rdf:type | owl:ObjectProperty     |
+--------------------------------------+----------+------------------------+

Query returned 3 results in 00:00:00.242


## Using the web interface: 

See [Stardog Studio](https://docs.stardog.com/stardog-applications/studio/)

Stardog has a nice web interface called stardog studio that you will
probably want to use for most interactions adter you have started your server.

[Using Stardog Studio](https://docs.stardog.com/get-started/access-studio)

https://www.stardog.com/studio/


https://cloud.stardog.com/u/1/studio/#/
