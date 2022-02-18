def neotocsv(filename, query):
    with driver.session(database="neo4j") as session:
        results = session.run(query)

        # allows to put header for csv
        i = 0
        #final = []
        file = "data/"+filename
        with open("data/test.csv", "w+") as f:

            for record in results:

                # write header keys
                if i == 0:
                    i += 1
                    head = ""

                    for k in record.keys():
                        k = str(k).replace(",","")
                        head += k + ","
                    
                    lastCommaIndex = head.rfind(",")
                    newHead = head[:lastCommaIndex] + "\n"
                    f.write(newHead)

                # addes data to CSV
                data = ""
                for v in record.values():
                    v = str(v).replace(",","")
                    data += str(v) + ","

                lastCommaIndex = data.rfind(",")
                newData = data[:lastCommaIndex] + "\n"
                f.write(newData)
                
                #final.append(record.values()[0])
                
                
            

    driver.close()