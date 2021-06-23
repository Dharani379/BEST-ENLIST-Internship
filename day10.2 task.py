#create a real time scenario for inheritence example ecommerce
class Brands:
    
    brand_name1="Dell"
    brand_name2="Acer"
    brand_name3="Apple"
    
class features(Brands):       #child class
    features1="kasperkey"
    features2="Avast_antivirus"
    features3="Norton security"

	
class brandings(Brands):      #grand child class
    features1_ratings=5
    features2_ratings=3
    features3_ratings=4

	
class value(Brands):
    features1_value = "Excellent value"
    features2_values = "Better value"
    features3_value = "Good value"

	
obj_1 = features()           #obj creation
obj_2 = features()
obj_3 = features()
print(obj_1.brand_name1+"is an"+obj_1.features1+"Ratings of"+str(obj_2.features1_ratings)+"having"+obj_3.features1_value)
print(obj_1.brand_name1+"is an"+obj_1.features1+"Ratings of"+str(obj_2.features2_ratings)+"having"+obj_3.features2_value)
print(obj_1.brand_name1+"is an"+obj_1.features1+"Ratings of"+str(obj_2.features3_ratings)+"having"+obj_3.features3_value)


