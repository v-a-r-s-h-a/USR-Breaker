def read_n_enter():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    file = open("read/Suryast.txt", encoding="utf=8")

    read = file.read()
    file.seek(0)

    line = 1
    for word in read:
        if word == '\n':
            line += 1

    arr = []
    for i in range(line):
        arr.append(file.readline())

    sl = ""
    dis_str = ""
    l = []
    c = 1
    for x in arr:
        if "#" in x:
            dis_str += x[1:]
            c = 1
            l.append(sl)
            sl = ""

        if c <= 10:
            sl += x
            c += 1

    l.append(sl)

    # cursor.execute("INSERT INTO discourse(author_id, sentences, discourse_name) VALUES(%s, %s, %s)",
    #                (1, dis_str, "try"))

    it = 1
    for i in range(1, len(l)):
        file = open("read/out_gen/"+str(it), "w", encoding="utf=8")
        it += 1
        file.write(l[i])

    # for i in range(1, len(l)):
    #     cursor.execute(
    #         "INSERT INTO usr(author_id, discourse_id, orignal_USR_json, USR_status) VALUES(%s, %s, %s, %s)", (1, disc_id(), l[i], "In Edit"))
    mysql.connection.commit()
    return jsonify("Read and Entered")
