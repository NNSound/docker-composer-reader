import yaml
import csv

arr = []

with open("./docker-compose.yml", 'r') as stream:
    try:
        dcfile = yaml.safe_load(stream)

        for service in dcfile['services']:
            # print(service)
            # print(dcfile['services'][service]['ports'][0])
            ports = dcfile['services'][service]['ports'][0].split(':', 1)
            arr.append([service, ports[0], ports[1]])

    except yaml.YAMLError as exc:
        print(exc)

# print(arr)

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Service', 'Port-Localhost', 'Port-Docker'])
    for item in arr:
        writer.writerow([item[0], item[1], item[2]])

print('success')