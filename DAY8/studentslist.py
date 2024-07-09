# list

students_names = ["raji","siri","venu","raja","tirmula" ]
print(students_names)

#bucket list

s3_buckets = ["raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" ]
print(s3_buckets)

#adding new name to lists

s3_buckets_lists = ["raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" ]
s3_buckets_lists.append("pinky_demo_bucket") 
print(s3_buckets_lists)

#remove name from the lists

s3_buckets_lists = ["raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket", "pinky_demo_bucket" ]
s3_buckets_lists.remove("pinky_demo_bucket") 
print(s3_buckets_lists)

#tuple

s3_buckets = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
print(s3_buckets)

# type is used to identify the class

s3_buckets = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
print(tpye(s3_buckets))

# By using index we can identify one element name in the lists

s3_buckets = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
print(s3_buckets[0])

# To identify the length of elements in the lists

s3_buckets = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
print(len(s3_buckets))

# create a new elements to at index 0,1, and 2 (slicing a list)

s3_buckets_lists = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
new_list =  s3_buckets_lists[0:3]
print(new_list)

# sorting the list of numbers

number = [1,30,35,29,20,10]
number.sort()
print(number)

#concatenates s3_buckets_lists with [0,1]

s3_buckets_lists = ("raji_demo_bucket","siri_demo_bucket","venu_demo_bucket","raja_demo_bucket","tirmula_demo_bucket" )
print(s3_buckets_lists[0]+"---"+s3_buckets_lists[1])

