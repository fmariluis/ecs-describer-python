# ECS describer

Quick and dirty CLI tool to retrieve the public IP addresses (and other data) of the EC2 instances running your services on AWS Elastic Container Services.
Better than multiple clicks on the AWS web console!

## How to use
* Set up a virtualenv, install requirements
* Make sure your AWS credentials are available (set them in `~/.aws/credentials` for example)
* Run it:
```bash
python ecs-describer.py --cluster <ECS-CLUSTER-NAME>
```

## Example output

```
service                                    container          image                                                                               ec2_ip
-----------------------------------------  -----------------  ----------------------------------------------------------------------------------  --------------
service:example                            example            123.dkr.ecr.us-west-2.amazonaws.com/org/example:aabbcc                              19.24.126.21
```
