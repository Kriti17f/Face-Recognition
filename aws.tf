provider "aws" {

    region = "ap-south-1"
    profile = "default"
}

resource "aws_instance" "MyOS" {

  ami = "ami-010aff33ed5991201"
  instance_type = "t2.micro"
  tags = {
      Name: "MyOS"
      }
}

resource "aws_ebs_volume" "EBS" {
  availability_zone = aws_instance.MyOS.availability_zone
  size = 5
  tags = {
    Name = "EBS-Volume"
  }
}

resource "aws_volume_attachment" "EBS-Attach" {
  device_name = "/dev/sdv"
  volume_id   = aws_ebs_volume.EBS.id
  instance_id = aws_instance.MyOS.id
  force_detach = true
}

