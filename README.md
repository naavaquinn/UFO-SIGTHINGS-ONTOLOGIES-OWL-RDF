This project is focused on creating a detailed ontology for UFO sightings, drawing on data from the National UFO Reporting Center (NUFORC) in the USA and the UK Ministry of Defense’s UFO reports. The goal was to model this domain in a way that supports in-depth querying and analysis of UFO sighting patterns, observer details, geographical information, and specific sighting attributes.

Project Overview
Authors: Atherly Rachel, Azim Fairooz, Ciubotaru Alexandra, Naava Namuwonge Hedwig
Instructor: Mathieu D’Aquin
Academic Year: 2023-2024
Contents
Introduction
The ontology captures elements of UFO sightings, such as reports, sighting locations, observer details, and associated descriptive properties. It integrates data from both UK and US sources, covering over 67,000 UFO sightings in total.

Data Cleaning
We standardized and cleaned the datasets from both countries, aligning column headers, date formats, and resolving datatype discrepancies. This prepared the data for a consistent ontology structure.

Ontology Design with Protégé
Using Protégé, we created classes like UFO, Location, Observer, and others. Key object properties like hasLocation, reportedBy, and isInCountry link these classes. We enriched data with terms describing UFO shapes (e.g., circular, triangular) for accurate classification.

Data Transformation in OntoRefine
The combined datasets were refined in OntoRefine, using custom mapping rules and schema alignment to ensure consistency. We generated unique blank nodes for certain classes, later constructed using SPARQL to overcome interface limitations.

Storage and Querying in GraphDB
The ontology was stored in GraphDB, supporting SPARQL queries to retrieve data such as unique UFO shapes, sightings by location, and observer details. The RDF structure allows efficient, flexible querying.

SPARQL Query Examples
Example queries include retrieving sighting occurrences by location, shape-based filtering, sightings by date, and observer attributes. This allowed us to analyze sighting patterns based on location, time, and UFO characteristics.

Demo Application
A simple application allows users to explore sightings based on location, unique UFO shapes, sightings by month, and random UFO reports. Future functionality could include additional queries and improved data consistency.

Validation with HermiT and SHACL
Using reasoners like HermiT, we checked the ontology for logical consistency. SHACL was used to ensure data quality, checking for missing or incorrect data types and invalid relationships.

Challenges
Managing hierarchical location data and ensuring reflexive relationships were complex. We faced data validation issues with SHACL, such as date formats and blank node constraints, which were resolved through further refinement.

Tools Used
Protégé: Ontology building
OntoRefine: Data cleaning and mapping
GraphDB: RDF storage and SPARQL querying
SHACL: Validation and data quality assurance
Future Applications
The ontology has potential for public safety and national security uses, enabling pattern detection for unusual sightings and incident correlation for aerial safety. It could also support real-time pilot report integrations to enhance aviation protocols.
