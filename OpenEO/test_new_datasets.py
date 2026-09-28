from openeo.local import LocalConnection
import matplotlib.pyplot as plt

connection = LocalConnection('./')

# Enter the url to the collection here
url = 'https://api.stac.164.30.69.113.nip.io/collections/esacci-l4_fire-ba-avhrr-ltdr-fv1.1.openeo'

# Enter the temporal extent as needed (will need at least some kind of filtering if not using bands)
temporal_extent = ['2006-01-01','2006-12-31']

datacube = connection.load_stac(url=url, # bands are the specific variables to be loaded - can try without specifying but tends to not be supported
                                bands=['burned_area', 'fraction_of_burnable_area', 'fraction_of_observed_area', 'standard_error'])
dataset = datacube.execute()

print(dataset)