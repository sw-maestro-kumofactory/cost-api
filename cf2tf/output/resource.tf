resource "aws_iam_instance_profile" "v3906a1507a8c11eebac62b6d7e9a1267_instance_profile_c217_abbb" {
  role = [
    "ecr-full-access"
  ]
}

resource "aws_instance" "v3906a1507a8c11eebac62b6d7e9a12672_f602788" {
  availability_zone = "ap-northeast-2a"
  iam_instance_profile = aws_iam_instance_profile.v3906a1507a8c11eebac62b6d7e9a1267_instance_profile_c217_abbb.arn
  // CF Property(ImageId) = "ami-0f6fdd05c7b50bbd6"
  instance_type = "t3.micro"
  user_data = base64encode("#!/bin/bash")
  tags = {
    Name = "ApplicationDeployEC2123"
  }
}

resource "aws_ecs_task_set" "cdk_metadata" {
  // CF Property(Analytics) = "v2:deflate64:H4sIAAAAAAAA/zPSMzQw0TNQTCwv1k1OydbNyUzSqw4uSUzO1glKLc4vLUpO1QHKxVenJhvpVXvmFZck5gGFnNPyYOxanczEXD0kgYCi/LTMHKA4UMy/tKSgtATEgplWq5OXn5Kql1WsX2ZkqGcItDqrODNTt6g0ryQzN1UvCEIDAI3DlriXAAAA"
}

