list_of_cloud = ["AWS", "Azure", "GCP" , "IBM Cloud", "Oracle Cloud"]
print(list_of_cloud)

#add a new cloud provider
list_of_cloud.append("DigitalOcean")
print(list_of_cloud)

#add a new cloud provider at the beginning
list_of_cloud.insert(0, "Alibaba Cloud")
print(list_of_cloud)

#add a new cloud provider at index 2
list_of_cloud.insert(2, "Linode")
print(list_of_cloud)

print(len(list_of_cloud))  # Print the length of the list



# Remove a cloud provider
list_of_cloud.remove("IBM Cloud")
print(list_of_cloud)

# Remove the last cloud provider
list_of_cloud.pop()
print(list_of_cloud)

print("The first cloud provider is:", list_of_cloud[0])
print("The cloud provider at index 2 is:", list_of_cloud[2])
print("The last cloud provider is:", list_of_cloud[-1])

#iteration
for cloud in list_of_cloud:
    print(cloud)


for i in range(0, 11):
    print(i)