from app import db 
from app.models import Category 

print('Loading categories...')

cat1=Category('Biography') 
cat2=Category('Business') 
cat3=Category('Essays') 
cat4=Category('Fiction') 
cat5=Category('History') 
cat6=Category('Horror') 
cat7=Category('Humour') 
cat8=Category('Memoir') 
cat9=Category('Nonfiction') 
cat10=Category('Poetry') 
cat11=Category('Psychology') 
cat12=Category('Romance') 
cat13=Category('Self-Help') 
cat14=Category('Religion/ Spirituality') 
cat15=Category('Travel') 

print('Loaded categories...') 

print('Adding categories...') 
db.session.add([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12, cat13, cat14, cat15])

print('Saving categories...')
db.session.commit()

print('Categories added and saved! Exiting...') 

