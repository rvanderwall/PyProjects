import sys

in_file = sys.argv[1]
out_file = "Done.cs"

TRANSACTION_ID = "35259B05-366A-EA11-B83B-005056AE29FA".upper()
CUSTOMER_ID = "39259B05-366A-EA11-B83B-005056AE29FA".upper()
ENTITY_ID = "3B259B05-366A-EA11-B83B-005056AE29FA".upper()

    
def ERROR(msg):
    print("ERROR: " + msg)
    exit()


def verify_ids():
    parts_t = TRANSACTION_ID.split('-')
    parts_c = CUSTOMER_ID.split('-')
    parts_e = ENTITY_ID.split('-')
    if len(parts_t) != 5:
        ERROR("Transaction_id not properly formed")
    if len(parts_c) != 5:
        ERROR("Customer_id not properly formed")
    if len(parts_e) != 5:
        ERROR("Entity_id not properly formed")

    for component_index in [1, 2, 3, 4]:
        if parts_t[component_index] != parts_c[component_index]:
            ERROR("Mismatch between transaction and customer")
        if parts_t[component_index] != parts_e[component_index]:
            ERROR("Mismatch between transaction and entity")

    if parts_t[0] == parts_c[0]:
        ERROR("transaction id and customer id are the same")
    if parts_t[0] == parts_e[0]:
        ERROR("transaction id and entity id are the same")
    if parts_e[0] == parts_c[0]:
        ERROR("entity id and customer id are the same")


def ireplace(string1, find_str, replace_str):
    s1 = string1.replace(find_str, replace_str)
    s2 = s1.replace(find_str.lower(), replace_str)
    return s2


# Smallest fragments of IDs that we will see
first_t_fragment = TRANSACTION_ID[:8]
first_c_fragment = CUSTOMER_ID[:8]
first_e_fragment = ENTITY_ID[:8]
ID_LEN = len(TRANSACTION_ID)
common_ending = TRANSACTION_ID[8:]
end_fragment = common_ending[-8:]


def process_beginning_fragment(line):
    id_to_find = None
    id_type = None
    if first_t_fragment in line.upper():
        id_type = "TransactionId"
        id_to_find = TRANSACTION_ID
    if first_c_fragment in line.upper():
        id_type = "CustomerId"
        id_to_find = CUSTOMER_ID
    if first_e_fragment in line.upper():
        id_type = "EntityId"
        id_to_find = ENTITY_ID

    if id_to_find is None:
        return line

    #  "35259B05-366A-EA11-B83B-005056AE29FA" --> " + this.Context["TransactionId"].ToString() + "
    #  ;35259B05-366A-EA11-B83B-005056AE29FA& --> ;" + this.Context["TransactionId"].ToString() + "&
    #  {35259B05-366A-EA11-B83B-005056AE29FA} --> {" + this.Context["TransactionId"].ToString() + "}
    #  35259B05-366A-EA11-B83B-005056AE29FA --> " + this.Context["TransactionId"].ToString() + @"
    if id_to_find in line.upper():
        line = ireplace(line, f'"{id_to_find}"', f'this.Context["{id_type}"].ToString()')
        line = ireplace(line, f';{id_to_find}&', f';" + this.Context["{id_type}"].ToString() + @"&')
        line = ireplace(line, f'{{{id_to_find}}}', f'{{" + this.Context["{id_type}"].ToString() + @"}}')
        line = ireplace(line, f'{id_to_find}', f'" + this.Context["{id_type}"].ToString() + "')

    # Now look for fragments of the beginning part of the ID
    for end_index in range(ID_LEN, 10, -1):
        fragment_to_find = id_to_find[:end_index]
        if fragment_to_find in line.upper():
            line = ireplace(line, f'{fragment_to_find}"', f'" + this.Context["{id_type}"].ToString()')

    return line


def process_end_fragment(line):
    if end_fragment not in line.upper():
        return line

    # Smallest fragment to look for is 8
    for start_index in range(len(common_ending) - len(end_fragment)):
        fragment_to_find = common_ending[start_index:]
        if fragment_to_find in line.upper():
            line = ireplace(line, f'{fragment_to_find}', f'')
    return line


def process_line(line):
    line = process_beginning_fragment(line)
    line = process_end_fragment(line)
    return line


def process_file(file_to_process):
    new_lines = []
    with open(file_to_process) as f:
        file_lines = f.readlines()

    for line in file_lines:
        line = line.rstrip()
        processed_line = process_line(line)
        new_lines.append(processed_line)

    return new_lines


if __name__ == "__main__":
    verify_ids()
    processed_lines = process_file(in_file)
    for p_line in processed_lines:
        print(p_line)
