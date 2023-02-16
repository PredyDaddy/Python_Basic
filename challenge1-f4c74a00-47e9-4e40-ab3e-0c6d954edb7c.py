# A simple contacts class

class ContactsBook:

    def __init__(self):
        self.contacts = self.setupContacts()

    def setupContacts(self):
        """The key is a person's name. The value in each case is
           a 3-tuple with (email,position,extension)"""
        return \
            {'jane':('jane@acme.com','manager',1546), \
             'rod':('rod@acme.com','programmer',8724), \
             'freddy':('freddy@acme.com','support',8524) }

    def listAllContacts(self):
        """Iterate through the dictionary to show all contacts"""
        for k,v in self.contacts.items():
            email,position,extension = v
            print(f'{k}: email: {email}, position: {position}, ext: {extension}')

    def getNumberOfContacts(self):
        """Returns the number of contacts in this book"""
        return len(self.contacts.keys())

    def addNewContact(self,name,email,position,extension):
        """Add a new key/value pairing to the dictionary
           Returns True if this is a new contact and can be added
           False otherwise"""
        if name not in self.contacts.keys():
            self.contacts[name] = (email,position, extension)
            return True
        else:
            return False

    def updateEmail(self,name,newEmail):
        """Updates an email address for the named person
           Returns True if can be updated, false otherwise """
        if name in self.contacts.keys():
            v = self.contacts[name]
            email, position, extension = v
            self.contacts[name] = (newEmail, position, extension)
            return True
        else:
            return False

    def getEmail(self, name):
        """Fetches an email address for a named person. Returns
        None if the named person is not in the contacts list"""
        if name in self.contacts.keys():
            v = self.contacts[name]
            email, position, extension = v
            return email
        else:
            return None

    def searchByName(self,name):
        """Search for person by name and display contact details"""
        if name not in self.contacts.keys():
            print(f'Sorry, {name} not in the contacts list')
            return False
        else:
            v = self.contacts[name]
            email, position, extension = v
            print(f'{name}: email: {email}, position: {position}, ext: {extension}')
            return True

    def printAllKeys(self):
        """Print all keys in the dictionary """
        for k in self.contacts.keys():
            print(k)

class TestContactsbook():
    def setUp(self):
        print('test start')
    def teardown(self):
        print('test end')
    def test_1(self):
        self.name = ContactsBook()
        self.assertTrue(self.name.addNewContact('william','will@acme.com','junior','1234'))
        self.assertEqual(self.name.getNumberOfContacts(),4)
        self.assertFalse(self.name.addNewContact('william','will@acme.com','junior','1234'))
        self.assertEqual(self.name,4)
    def test_2(self):
        self.name = ContactsBook()
        self.assertEqual(self.name.getEmail('rod'),'rod@acme')
        self.assertTrue(self.name.updateEmail('rod','roddy@acme.com'))
        self.assertEqual(self.name.getEmail('rod'),'roddy@acme.com')
        self.assertTrue(self.name.searchByName('rod'))
        self.assertFalse(self.name.searchByName('luobin'))