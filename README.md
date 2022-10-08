- Login EC2:
sudo ssh -i ~/.ssh/my-aws-c2.pem ubuntu@ec2-44-236-75-64.us-west-2.compute.amazonaws.com
- Login ECR:
sudo docker login -u AWS -p $(aws ecr get-login-password --region us-west-2) <id_ecr>.dkr.ecr.us-west-2.amazonaws.com
- ECR docker:
sudo docker tag <image_id> <id_ecr>.dkr.ecr.us-west-2.amazonaws.com
sudo push 575531465457.dkr.ecr.us-west-2.amazonaws.com/<tag_image_name>
