from swagger_server.repositories.base_repository import Repository
from swagger_server.models.listing import Listing as Listing_Model
from swagger_server.models.host import Host as Host_Model


class Listing(Repository):

    def get_all(self):
        query_results = self._db.execute('''
            SELECT 
                listings.id, listings.name, neighbourhood, area, latitude, longitude, room_type roomType, price, 
                min_nights minNights, num_of_reviews numOfReviews, availability, hosts.id host_id, hosts.name host_name, 
                hosts.num_of_listings
            FROM listings, hosts
            LIMIT 1000
        ''').fetchall()

        result = []
        for row in query_results:
            row = dict(row)
            listing = Listing_Model.from_dict(row)
            listing.host = Host_Model(
                id=row['host_id'],
                name=row['host_name'],
                num_of_listings=row['num_of_listings']
            )
            result.append(listing)

        return result
