# Install pymongo
   `pip install pymongo`

# If error occur related to dnspython
* pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
   `pip3 install 'pymongo[srv]'`
   or
   `pip install pymongo[srv]`
   or
   `pip3 install pymongo[srv]`

## Operators for mongodb

https://docs.mongodb.com/manual/reference/operator/update/