
"""
Project 12
"""
print("For the purpose of this Project, I will print out a ")
print("The below program demonstrates how to declare empty list: 'string_list=[]' ")
string_list = []
print(" The below function will add items to the list: 'string_list.append'")

string_list = ["EC2", "S3", "Elastic Cache", "Cloud9", "VPC", "SNS","RDS","DynamoDB","IAM"]
string_list.append("Cloudfront")
print(string_list)
print("The length of the list is:", len(string_list))
string_list.remove("S3")
print(string_list)
string_list.remove("SNS")
print(string_list)
print("The length of the list is:", len(string_list))