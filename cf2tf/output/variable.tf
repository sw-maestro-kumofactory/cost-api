variable bootstrap_version {
  description = "Version of the CDK Bootstrap resources in this environment, automatically retrieved from SSM Parameter Store. [cdk:skip]"
  type = string
  default = "/cdk-bootstrap/hnb659fds/version"
}

