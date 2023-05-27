#use sh in cloud cli
aws s3 mb s3://sam-scratch-caliandro-eu-west-1 --region eu-west-1

#package cloudformation (you can also use sam cloudformation package ... )
aws cloudformation package --template-file template.yaml --s3-bucket sam-scratch-caliandro-eu-west-1 --output-template-file gen/template-generate.yaml

#now let's use sam instead of aws cloudformation
sam deploy --template-file gen/template-generate.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM