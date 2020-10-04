import config 

api=config.create_api

 f = open('mss.txt', 'r')
    f.read()
    a=""
        while a!= "\r\n":
            texto+=a 
            f.read(a)
    f.close()
    api.update_status(status="How to reduce your carbon footprint?"+"\r\n" + texto)
