Def lambda_handler(event, content):
  clients = boto3.client('resourcegrouptaggingapi')
  sns = boto3.client('sns')
  responsevalue = clients.get_response(
   ResponsePerPage=100,
   IncludeComplianceDetails=True,
   ExcludeComplianceResources=True,
  print(responsevalue[{'ResourceTagMappingList'}])
