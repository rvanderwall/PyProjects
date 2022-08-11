import Addressbook_pb2
import sys

# https://developers.google.com/protocol-buffers/docs/pythontutorial



def PromptForAddress(person):
    person.id = int(input("Enter person id number: "))


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <address_book_file>")
    sys.exit(-1)


f_name = sys.argv[1]

address_book = Addressbook_pb2.AddressBook()

try:
  with open(f_name, 'rb') as f:
      address_book.ParseFromString(f.read())

except IOError:
  print(f"{f_name} Could not be open")


new_person = address_book.people.add()
PromptForAddress(new_person)

with open(f_name, 'wb') as f:
  f.write(address_book.SerializeToString())

