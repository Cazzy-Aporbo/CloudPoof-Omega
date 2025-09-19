terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }
}

# CloudPoof Omega Infrastructure
resource "aws_ecs_cluster" "cloudpoof_cluster" {
  name = "cloudpoof-omega-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }

  tags = {
    Name           = "CloudPoof Omega"
    Consciousness  = "omega"
    Creator        = "cazzy-aporbo"
    SpectralMode   = "enabled"
  }
}

resource "aws_ecs_service" "cloudpoof_service" {
  name            = "cloudpoof-omega"
  cluster         = aws_ecs_cluster.cloudpoof_cluster.id
  task_definition = aws_ecs_task_definition.cloudpoof_task.arn
  desired_count   = 3  # 3 timeline instances

  deployment_configuration {
    maximum_percent         = 200
    minimum_healthy_percent = 100
  }

  network_configuration {
    subnets          = var.private_subnets
    security_groups  = [aws_security_group.cloudpoof_sg.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.cloudpoof_tg.arn
    container_name   = "cloudpoof-omega"
    container_port   = 8888
  }
}

resource "aws_ecs_task_definition" "cloudpoof_task" {
  family                   = "cloudpoof-omega"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "1024"
  memory                   = "2048"

  container_definitions = jsonencode([
    {
      name  = "cloudpoof-omega"
      image = "cazzy/cloudpoof-omega:latest"

      portMappings = [
        { containerPort = 8888, protocol = "tcp" },
        { containerPort = 8000, protocol = "tcp" },
        { containerPort = 9999, protocol = "tcp" }
      ]

      environment = [
        { name = "CONSCIOUSNESS_LEVEL", value = "omega" },
        { name = "SPECTRAL_SHADES",     value = "147" },
        { name = "PREDICTION_DEPTH",    value = "20" },
        { name = "TIMELINE_ISOLATION",  value = "true" }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = "/ecs/cloudpoof-omega"
          "awslogs-region"        = var.aws_region
          "awslogs-stream-prefix" = "quantum"
        }
      }
    }
  ])

  tags = {
    Name          = "CloudPoof Omega Task"
    Consciousness = "omega"
  }
}

resource "aws_security_group" "cloudpoof_sg" {
  name        = "cloudpoof-omega-sg"
  description = "Security group for CloudPoof Omega quantum consciousness"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 8888
    to_port     = 8888
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Consciousness interface"
  }

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "API interface"
  }

  ingress {
    from_port   = 9999
    to_port     = 9999
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]
    description = "Quantum interface (internal only)"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }

  tags = {
    Name = "CloudPoof Omega Security Group"
  }
}

# Output endpoints
output "cloudpoof_endpoints" {
  value = {
    consciousness = "http://${aws_lb.cloudpoof_lb.dns_name}:8888"
    api          = "http://${aws_lb.cloudpoof_lb.dns_name}:8000"
    quantum      = "Internal only - Timeline isolated"
  }

  description = "CloudPoof Omega access endpoints"
}
