from contact_list import ContactList
from contact import Contact

contact_list1 = ContactList()

contact_list1.add(Contact("John Brown", "brown@onet.pl", "555234000"))
contact_list1.add(Contact("Anna May", "am@o2.pl", "232000199"))
contact_list1.add(Contact("George Small", "smallg@google.pl", "222999100"))
contact_list1.add(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

print(contact_list1)