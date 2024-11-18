# UFO Sightings Ontology Project

This repository contains the ontology and resources for analyzing and querying UFO sightings using data from the National UFO Reporting Center (NUFORC) in the USA and the UK Ministry of Defense’s UFO reports. The ontology enables structured querying and analysis of sighting patterns, observer demographics, geographic locations, and UFO characteristics.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Cleaning](#data-cleaning)
- [Ontology Design](#ontology-design)
- [Data Transformation in OntoRefine](#data-transformation-in-ontorefine)
- [Storage and Querying in GraphDB](#storage-and-querying-in-graphdb)
- [SPARQL Query Examples](#sparql-query-examples)
- [Demo Application](#demo-application)
- [Validation](#validation)
- [Challenges](#challenges)
- [Tools Used](#tools-used)
- [Future Applications](#future-applications)

---

## Project Overview
- **Authors**: Atherly Rachel, Azim Fairooz, Ciubotaru Alexandra, Naava Namuwonge Hedwig
- **Instructor**: Mathieu D’Aquin
- **Academic Year**: 2023-2024

This ontology models UFO sightings data to support in-depth analysis, with datasets from both UK and US sources, covering over 67,000 reports. It includes classes such as `UFO`, `Location`, `Observer`, and properties linking these classes for detailed analysis of UFO sighting patterns.

## Data Cleaning
We standardized and cleaned the datasets to ensure uniformity in column headers, date formats, and datatype consistency. This involved:
- Resolving datatype mismatches.
- Converting all date formats to a standard format.
- Aligning naming conventions across datasets.

## Ontology Design
The ontology was built using **Protégé** with classes like:
- `UFO`
- `Location`
- `Observer`

Key object properties were defined, such as `hasLocation`, `reportedBy`, and `isInCountry`, allowing linkage across classes. We also included detailed UFO characteristics, like shape (e.g., circular, triangular), to allow more precise filtering.

## Data Transformation in OntoRefine
Data was transformed and refined in **OntoRefine**:
- Applied custom mapping rules.
- Created blank nodes for certain class properties.
- Used SPARQL to resolve limitations in blank node representation.

## Storage and Querying in GraphDB
The ontology was stored in **GraphDB** to support advanced SPARQL queries. This enabled data retrieval based on complex relationships, such as sightings by shape or observer location.

## SPARQL Query Examples
Here are some examples of SPARQL queries implemented:
- Retrieve sighting occurrences by location.
- Filter sightings based on UFO shape.
- Retrieve sightings by date.
- Access specific observer demographic details.

These queries allow in-depth analysis of sighting patterns based on location, date, and UFO characteristics.

## Demo Application
A demo application provides a simple interface for users to explore the data. Users can:
- Browse sightings by location.
- View unique UFO shapes.
- Filter sightings by date or month.
- Access random UFO reports for exploration.

Future versions may include additional filters and improved data consistency.

## Validation
We validated the ontology using **HermiT** and **SHACL**:
- **HermiT**: Checked logical consistency across relationships.
- **SHACL**: Ensured data quality by enforcing constraints on data types and relationships.

## Challenges
Key challenges included:
- Managing hierarchical location data.
- Handling reflexive relationships.
- Validating data with SHACL, especially for date formats and blank nodes.

These challenges were addressed through refinement and additional data transformations.

## Tools Used
- **Protégé**: For ontology development.
- **OntoRefine**: For data cleaning and mapping.
- **GraphDB**: For RDF storage and SPARQL querying.
- **SHACL**: For validation and quality assurance.

## Future Applications
The ontology has potential uses in:
- Public safety and national security, enabling pattern detection in unusual sightings.
- Aviation protocols, by correlating sightings with real-time pilot reports for enhanced aerial safety.

---

This project establishes a structured, searchable database for UFO sightings, fostering data-driven insights and analysis in UFO research.

---

## Getting Started
To clone this repository and explore the ontology:
```bash
git clone https://github.com/username/ufo-sightings-ontology.git
cd ufo-sightings-ontology
