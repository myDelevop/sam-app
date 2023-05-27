#use sh in cloud cli
aws s3 mb s3://sam-scratch-caliandro-eu-west-1 --region eu-west-1

#package cloudformation
aws cloudformation package