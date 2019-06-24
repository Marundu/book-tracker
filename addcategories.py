from app import db 
from app.models import Category 

print('Loading categories...')

cat1=Category(category='Biography') 
cat2=Category(category='Business') 
cat3=Category(category='Essays') 
cat4=Category(category='Fiction') 
cat5=Category(category='History') 
cat6=Category(category='Horror') 
cat7=Category(category='Humour') 
cat8=Category(category='Memoir') 
cat9=Category(category='Nonfiction') 
cat10=Category(category='Poetry') 
cat11=Category(category='Psychology') 
cat12=Category(category='Romance') 
cat13=Category(category='Self-Help') 
cat14=Category(category='Religion/ Spirituality') 
cat15=Category(category='Travel') 

print('Loaded categories...') 

print('Adding categories...') 
db.session.add_all([cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12, cat13, cat14, cat15])

print('Saving categories...')
db.session.commit()

print('Categories added and saved! Exiting...') 

