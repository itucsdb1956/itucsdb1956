
from model.address import AddressModel
from model.product import ProductModel
from model.customer import CustomerModel
from model.firm import FirmModel
from model.user import UserModel
from model.order import OrderModel



def DeleteAllTable():

    AddressModel().drop()
    ProductModel().drop()
    CustomerModel().drop()
    FirmModel().drop()
    UserModel().drop()
    OrderModel().drop()

def CreateAllTable():
    AddressModel().create()
    ProductModel().create()
    CustomerModel().create()
    FirmModel().create()
    UserModel().create()
    OrderModel().create()

#if user type==0 then it is type of customer otherwise "1" it is type of firm
def InsertUser():

    UserModel().insert("testcustomer", "1234", "testcustomer@mail.com", 0)
    UserModel().insert("testfirm", "1234", "testfirm@mail.com", 1)

    UserModel().insert("testcustomer1", "1234", "testcustomer1@mail.com", 0)
    UserModel().insert("testfirm1", "1234", "testfirm1@mail.com",1)

    UserModel().insert("testcustomer2", "1234", "testcustomer2@mail.com", 0)
    UserModel().insert("testfirm2", "1234", "testfirm2@mail.com",1)


def InsertAddress():

    AddressModel().insert("Altınbasak", 9, "Maslak", "Istanbul", 20)
    AddressModel().insert("Cicek", 2, "Ayazaga", "Istanbul", 21)
    AddressModel().insert("Kagıt", 3, "Besiktas", "Istanbul", 24)
    AddressModel().insert("Havuzbası", 4, "Uskudar", "Istanbul", 10)

def InsertFirm():

    FirmModel().insert("Marmara", 1, 2, 21600000)
    FirmModel().insert("Karadeniz", 2, 4, 21600001)
    FirmModel().insert("Ege", 3, 6, 21600002)

def InsertCustomer():

    CustomerModel().insert("testName", 1, 2160010, 1)
    CustomerModel().insert("testName1", 2, 2160011, 3)
    CustomerModel().insert("testName2", 3, 2160012, 5)

def InsertOrder():

    OrderModel().insert(1, 1)
    OrderModel().insert(2, 2)
    OrderModel().insert(3, 3)

def InserProduct():

    ProductModel().insert("Hamburger", 1, 10.0)
    ProductModel().insert("Sandwich", 2, 25.0)
    ProductModel().insert("Tost", 1, 5.0)

def CreateStarter():

    InsertUser()
    InsertAddress()
    InsertCustomer()
    InsertFirm()
    InsertOrder()
    InserProduct()












