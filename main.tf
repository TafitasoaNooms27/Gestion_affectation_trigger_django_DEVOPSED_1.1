provider "aws" {
	region = "eu-west-3"
}

###aws_instance
resource "aws_instance" "web" {
	ami 			= "ami-0ef3f96c2e52355a5" ##django packaged by bitnami
	instance_type 	= "t2.micro"
	vpc_security_group_ids = [aws_security_group.web.id] ## aws_security_group
	subnet_id = aws_subnet.web.id ## aws_subnet
	associate_public_ip_address = true    ## definir IP pub avec aassociation 

	tags = {
		Name = "web_server"
	}
	#security_groups = [
	#	"webserver",
	#]
}

###aws_vpc
resource "aws_vpc" "web" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "web"
  }
}

####aws_subnet
resource "aws_subnet" "web" {
  vpc_id     = aws_vpc.web.id  #aws_vpc var 
  cidr_block = "10.0.1.0/24"
  
  availability_zone = "eu-west-3c"
  tags = {
    Name = "web"
  }
}

###aws_internet_gateway
resource "aws_internet_gateway" "web" {
  vpc_id = aws_vpc.web.id

  tags = {
    Name = "web"
  }
}


###aws_route
resource "aws_route" "web" {
  route_table_id            = aws_vpc.web.default_route_table_id ## recuperer table de routage vpc + nom vpc + 
  destination_cidr_block    = "0.0.0.0/0"  # cidr dest ouvert internet 
  gateway_id                 = aws_internet_gateway.web.id
}


##aws_security_group
resource "aws_security_group" "web" {
  name        = "allow_web"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.web.id

  ingress {
    description      = "web from VPC"
    from_port        = 80 #port web
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"] #bloc cidr des acceder en entrer à notre service , partie internet
    #ipv6_cidr_blocks = [aws_vpc.main.ipv6_cidr_block]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

###aws_eip
resource "aws_eip" "web" {
	instance = aws_instance.web.id
	vpc      = true 
}