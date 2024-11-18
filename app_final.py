from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import XSD
import random
from collections import Counter
from datetime import datetime
import calendar

# Initialize RDF graph and namespaces
g = Graph()
g.parse('query-result.ttl', format='turtle')

onto = Namespace('http://www.aliens.com/ontology/')
base = Namespace('http://www.aliens.com/base/')

def query_ufos(city=None, area=None, country=None):
    # Prepare the base SPARQL query
    query = '''
    PREFIX onto: <http://www.aliens.com/ontology/>
    PREFIX base: <http://www.aliens.com/base/>

    SELECT ?ufo ?description ?dateTime ?observer ?city ?area ?country
    WHERE {
      ?ufo a onto:UFO ;
           onto:hasDescription ?description ;
           onto:hasDocumentedDateTime ?dateTime ;
           onto:hasObserver ?observer ;
           onto:hasLocation ?location ;
           onto:wasObservedIn ?city, ?area, ?country .

      ?location onto:hasCity ?city ;
                onto:hasRegion ?area ;
                onto:hasCountry ?country .
    '''

    # Add filters for the optional parameters
    filters = []
    if city:
        filters.append(f'FILTER (?city = base:{city})')
    if area:
        filters.append(f'FILTER (?area = base:{area})')
    if country:
        filters.append(f'FILTER (?country = base:{country})')

    # Combine query with filters
    if filters:
        query += ' '.join(filters)
    
    # Close the WHERE clause
    query += '} LIMIT 10'

    results = g.query(query)
    return results

def get_top_shapes():
    query = '''
    PREFIX onto: <http://www.aliens.com/ontology/>
    
    SELECT ?shape (COUNT(?ufo) as ?count)
    WHERE {
      ?ufo a onto:UFO ;
           onto:hasShape ?shape .
    }
    GROUP BY ?shape
    ORDER BY DESC(?count)
    '''
    results = g.query(query)
    for row in results:
        shape = row.shape
        count = row.count
        print(f"Shape: {shape}, Count: {count}")


# def get_sightings_by_month():
#     query = '''
#     PREFIX onto: <http://www.aliens.com/ontology/>
    
#     SELECT ?dateTime
#     WHERE {
#       ?ufo a onto:UFO ;
#            onto:hasDocumentedDateTime ?dateTime .
#     }
#     '''
#     results = g.query(query)
#     months = [datetime.strptime(str(row.dateTime), '%Y-%m-%dT%H:%M:%S').month for row in results]
#     counter = Counter(months)
#     for month, count in sorted(counter.items()):
#         print(f"Month: {month}, Count: {count}")

def get_sightings_by_month():
    query = '''
    PREFIX onto: <http://www.aliens.com/ontology/>
    
    SELECT ?dateTime
    WHERE {
      ?ufo a onto:UFO ;
           onto:hasDocumentedDateTime ?dateTime .
    }
    '''
    results = g.query(query)
    
    # Extract month names from dateTime values
    months = [datetime.strptime(str(row.dateTime), '%Y-%m-%dT%H:%M:%S').month for row in results]
    month_names = [calendar.month_name[month] for month in months]
    
    # Count occurrences of each month
    counter = Counter(month_names)
    
    # Print results sorted by month name
    for month, count in sorted(counter.items()):
        print(f"Month: {month}, Count: {count}")

def get_random_ufo_sighting():
    query = '''
    PREFIX onto: <http://www.aliens.com/ontology/>
    
    SELECT ?ufo ?description ?dateTime ?observer ?city ?area ?country
    WHERE {
      ?ufo a onto:UFO ;
           onto:hasDescription ?description ;
           onto:hasDocumentedDateTime ?dateTime ;
           onto:hasObserver ?observer ;
           onto:hasLocation ?location .
      
      
      OPTIONAL { ?ufo onto:wasObservedIn ?city . }
      OPTIONAL { ?location onto:hasCity ?city . }
      OPTIONAL { ?location onto:hasRegion ?area . }
      OPTIONAL { ?location onto:hasCountry ?country . }
    }
    '''
    results = list(g.query(query))
    if results:
        sighting = random.choice(results)
        city = sighting.city if 'city' in sighting else "N/A"
        area = sighting.city if 'area' in sighting else "N/A"
        country = sighting.city if 'country' in sighting else "N/A"
        print("Random UFO Sighting:")
        print(f"UFO: {sighting.ufo}")
        print(f"Description: {sighting.description}")
        print(f"Date: {sighting.dateTime.split('T')[0]}")
        print(f"Observer: {sighting.observer}")
        print(f"City: {city}")
        print(f"Area: {area}")
        print(f"Country: {country}")
    else:
        print("No sightings found.")
    

def print_results(results):
    for row in results:
        ufo = row.ufo
        description = row.description
        dateTime = row.dateTime.split('T')[0]
        observer = row.observer
        city = row.city if 'city' in row else "N/A"
        area = row.area if 'area' in row else "N/A"
        country = row.country if 'country' in row else "N/A"

        print(f"UFO: {ufo}")
        print(f"Description: {description}")
        print(f"DateTime: {dateTime}")
        print(f"Observer: {observer}")
        print(f"City: {city}")
        print(f"Area: {area}")
        print(f"Country: {country}")
        print("------")

# Main application loop
if __name__ == "__main__":
    print("Welcome to the UFO Sightings Query Application!")

    while True:
        print("\nSelect an option:")
        print("1. Query UFO sightings by location")
        print("2. Get top UFO shapes")
        print("3. Get sightings by month")
        print("4. Get a random UFO sighting")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            print("\nEnter the location details to search for UFO sightings:")
            city = input("City (e.g., Knutsford): ").strip()
            area = input("Area (e.g., Cheshire): ").strip()
            country = input("Country (e.g., uk): ").strip()

            if city or area or country:
                results = query_ufos(city=city, area=area, country=country)
                print_results(results)
            else:
                print("Please enter at least one location detail to search for UFO sightings.")

        elif choice == '2':
            get_top_shapes()
        elif choice == '3':
            get_sightings_by_month()
        elif choice == '4':
            get_random_ufo_sighting()
        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        another_search = input("Do you want to perform another search? (yes/no): ").strip().lower()
        if another_search != 'yes':
            print("Exiting application...")
            break
