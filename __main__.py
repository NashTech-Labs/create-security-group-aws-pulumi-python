import pulumi
from pulumi import export
import pulumi_aws as aws



group = aws.ec2.SecurityGroup('pulumi_allow_8080',
            vpc_id='vpc-02f645865b6afd094',
            description='Enable access to port 8080',
            ingress=[
                { 'protocol': 'tcp', 'from_port': 8080, 'to_port': 8080, 'cidr_blocks': ['0.0.0.0/0'] },
                { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
            ])
