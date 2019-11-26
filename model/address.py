
from model.base import Base

class AddressModel(Base):

    def __init__(self):
        super(AddressModel, self).__init__()
        self.table_name = "ADDRESSES"

    def create(self,*args,**kwargs):

        command = """CREATE TABLE IF NOT EXISTS ADDRESSES(
            address_id serial PRIMARY KEY,
            street_name varchar(50) NOT NULL,
            building_no integer NOT NULL,
            apartment_no integer NOT NULL,
            locality_name varchar(50) NOT NULL,
            city varchar(30) NOT NULL,
            postcode integer
            );
        """
        self.execute(command)
    def insert(self,*args,**kwargs):
        command ="""
        INSERT INTO ADDRESSES(street_name,building_no,
        apartment_no,locality_name,city)
        VALUES ('{}','{}','{}','{}','{}','{}')
        );""".format(*args)
        self.execute(command)
    def update(self,*args,**kwargs):

        raise NotImplementedError
    def delete(self,id):

        #args ye bak
        command="""
        DELETE FROM ADDRESSES where id = {}""".format(id)
        self.execute(command)
    def read(self,*args,**kwargs):
        command = """
        SELECT * FROM ADDRESSES"""
        return self.execute(command)

addressModelInstance = AddressModel()


def createAddress(streetName,buildingNo,apartmentNo,localityName,City,PostCode):
    addressModelInstance.insert(streetName,buildingNo,apartmentNo,localityName,City,PostCode)
    return

def getAddressById(id):
    command="""
    SELECT address_id, street_name,building_no,apartment_no,locality_name,city FROM ADDRESSES WHERE id={}
    """.format(id)
    return addressModelInstance.execute(command)


def getAllAddresses():
    command="""
    SELECT * FROM ADDRESSES"""
    return addressModelInstance.execute(command)



def updateAddres(id, streetName,buildingNo,apartmentNo,localityName,City,postcode):
    command = """
        UPDATE  ADDRESSES SET street_name = '{}',  building_no ='{}', apartment_no='{}',locality_name='{}',city='{}',postcode='{}' where address_id = {}
        """.format(streetName, buildingNo, apartmentNo, localityName,City,postcode,id)

    return addressModelInstance.execute(command)


def deleteAddress(id):
    command= """
    DELETE FROM ADDRESSES WHERE address_id= {}""".format(id)
    return addressModelInstance.execute(command)