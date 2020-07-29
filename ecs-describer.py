"""Retrieves the public IP of the EC2 instance where an ECS service is running"""
import boto3
from tabulate import tabulate
import click


@click.command()
@click.option("--cluster", help="ECS cluster name")
def get_cluster_details(cluster):
    """Given a cluster name, retrieves the public IP of the ECS instances where the services are running, plus
    some extra data."""
    ecs = boto3.client("ecs")
    ec2 = boto3.client("ec2")
    task_list = ecs.list_tasks(cluster=cluster)
    click.echo("Getting cluster details...")
    task_details = ecs.describe_tasks(cluster=cluster, tasks=task_list["taskArns"])
    rows = []
    for task in task_details["tasks"]:
        group = task["group"]
        for container in task["containers"]:
            name = container["name"]
            image = container["image"]
            container_instance = ecs.describe_container_instances(
                cluster=cluster, containerInstances=[task["containerInstanceArn"]]
            )
            instance_id = container_instance["containerInstances"][0]["ec2InstanceId"]
            instance = ec2.describe_instances(InstanceIds=[instance_id])[
                "Reservations"
            ][0]["Instances"][0]
            ip = instance["PublicIpAddress"]
            rows.append([group, name, image, ip])
    click.echo(tabulate(rows, headers=["service", "container", "image", "ec2_ip"]))


if __name__ == "__main__":
    get_cluster_details()
